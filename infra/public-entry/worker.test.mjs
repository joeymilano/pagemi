import { test } from 'node:test';
import assert from 'node:assert/strict';
import { proxy } from './worker.mjs';
const env = { PUBLIC_ORIGIN: 'https://pagemi.example', UPSTREAM_ORIGIN: 'https://backend.example' };
test('cross-origin, missing-origin and wrong-host requests never reach backend', async () => {
  for (const [url, origin, status] of [['https://pagemi.example/api/sessions',null,403],['https://pagemi.example/api/sessions','https://evil.example',403],['https://pagemi.example/api/sessions','https://pagemi.example.evil.test',403],['https://evil.example/api/sessions','https://pagemi.example',421]]) {
    let called = false;
    const r = await proxy(new Request(url, {method:'POST', headers:origin?{origin}:{}}),env,async()=>{called=true;return new Response();});
    assert.equal(r.status,status);assert.equal(called,false);
  }
});
test('preserves body, CSRF, cookie and idempotency; routes only to fixed backend', async () => {
  const r = await proxy(new Request('https://pagemi.example/api/publish?next=https://evil.example',{method:'POST',headers:{origin:env.PUBLIC_ORIGIN,cookie:'mr-session=example','x-csrf-token':'csrf','idempotency-key':'once','x-forwarded-host':'evil.example'},body:'{"version":1}'}),env,async(req,options)=>{
    assert.equal(new URL(req.url).origin,env.UPSTREAM_ORIGIN);assert.equal(req.headers.get('origin'),env.UPSTREAM_ORIGIN);
    assert.equal(req.headers.get('x-forwarded-host'),null);assert.equal(req.headers.get('cookie'),'mr-session=example');assert.equal(req.headers.get('x-csrf-token'),'csrf');assert.equal(req.headers.get('idempotency-key'),'once');assert.equal(await req.text(),'{"version":1}');assert.equal(options.cache,'no-store');
    return new Response('ok',{headers:{'Set-Cookie':'mr-session=example; HttpOnly; Secure; SameSite=Strict','Cache-Control':'public,max-age=3600'}});
  });
  assert.match(r.headers.get('set-cookie'),/HttpOnly/);assert.equal(r.headers.get('cache-control'),'private, no-store');
});
test('returns streaming response without waiting for the stream to finish',async()=>{
  let controller;
  const stream = new ReadableStream({start(c){controller=c;c.enqueue(new TextEncoder().encode('first'));}});
  const r=await proxy(new Request(env.PUBLIC_ORIGIN+'/api/runs'),env,async()=>new Response(stream,{headers:{'content-type':'text/event-stream'}}));
  const reader=r.body.getReader();assert.equal(new TextDecoder().decode((await reader.read()).value),'first');controller.close();assert.equal((await reader.read()).done,true);
});
test('rewrites backend redirects and preserves authentication failures',async()=>{
  let r=await proxy(new Request(env.PUBLIC_ORIGIN),env,async()=>new Response(null,{status:302,headers:{location:env.UPSTREAM_ORIGIN+'/store/one'}}));
  assert.equal(r.headers.get('location'),env.PUBLIC_ORIGIN+'/store/one');
  r=await proxy(new Request(env.PUBLIC_ORIGIN+'/api/session'),env,async()=>Response.json({error:'SESSION_REQUIRED'},{status:401}));assert.equal(r.status,401);
});

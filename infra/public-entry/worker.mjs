/** Branded entry only. Application, data and model execution remain on Cloud Run. */
export async function proxy(request, env, upstreamFetch = fetch) {
  const url = new URL(request.url);
  const publicOrigin = new URL(env.PUBLIC_ORIGIN).origin;
  const upstream = new URL(env.UPSTREAM_ORIGIN).origin;
  const deny = (error, status) => Response.json({ error }, { status, headers: { 'Cache-Control': 'private, no-store' } });
  if (url.origin !== publicOrigin) return deny('HOST_REJECTED', 421);
  const write = !['GET', 'HEAD'].includes(request.method);
  const origin = request.headers.get('origin');
  // Validate before translation; do not turn cross-site writes into trusted writes.
  if ((write || origin !== null) && origin !== publicOrigin) return deny('ORIGIN_REJECTED', 403);
  if (!['GET', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'].includes(request.method)) return deny('METHOD_REJECTED', 405);
  const target = new URL(upstream);
  target.pathname = url.pathname;
  target.search = url.search;
  const headers = new Headers(request.headers);
  headers.delete('host');
  headers.delete('forwarded');
  headers.delete('x-forwarded-host');
  headers.delete('x-forwarded-proto');
  if (origin) headers.set('origin', upstream);
  try {
    const response = await upstreamFetch(new Request(target, {
      method: request.method, headers,
      body: ['GET', 'HEAD'].includes(request.method) ? undefined : request.body,
      redirect: 'manual', duplex: 'half', signal: request.signal,
    }), { cache: 'no-store' });
    const responseHeaders = new Headers(response.headers);
    responseHeaders.set('Cache-Control', 'private, no-store');
    responseHeaders.delete('CDN-Cache-Control');
    responseHeaders.delete('Cloudflare-CDN-Cache-Control');
    const location = responseHeaders.get('location');
    if (location) {
      const next = new URL(location, upstream);
      if (next.origin === upstream) responseHeaders.set('location', publicOrigin + next.pathname + next.search + next.hash);
    }
    // Pass through the stream and HttpOnly cookie; never buffer or cache session data.
    return new Response(response.body, { status: response.status, statusText: response.statusText, headers: responseHeaders });
  } catch {
    return deny('UPSTREAM_UNAVAILABLE', 502);
  }
}
export default { fetch(request, env) { return proxy(request, env); } };

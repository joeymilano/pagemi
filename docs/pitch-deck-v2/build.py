from pathlib import Path
import re,json,base64
ROOT=Path(__file__).resolve().parent
prefix=(ROOT/'template_helpers.py').read_text()
suffix=(ROOT/'template_finalize.py').read_text()
exec(prefix)
BRAND=json.loads((ROOT/'brand.json').read_text())['name']
def chrome(n,section):
 return f'<header class="chrome-min"><div class="l">{BRAND.upper()} / {section}</div><div class="r">AI BUILDER CUP 2026 &nbsp; {n:02d} / 16</div></header>'
def icon(name,size='8vw'):
 s=(ROOT/'assets/icons'/f'{name}.svg').read_text();s=re.sub(r'<svg\b',f'<svg aria-hidden="true" style="width:{size};height:{size};flex-shrink:0"',s,count=1)
 return s.replace('fill="#000000"','fill="currentColor"')
def head(title,kicker=''):
 return f'<div data-anim="head"><h2 class="h-xl">{title}</h2></div>'
def hero(theme,section,image,title,body,stats,caption='',ui=False):
 n=len(slides)+1
 image_style='contain' if ui else 'cover'
 overlay='' if ui else f'<div data-anim="title-block" class="hero-overlay-block" style="position:absolute;left:5vw;bottom:4vh;background:var(--paper);color:var(--ink);padding:2vh 2vw"><h1 style="font-size:{("9vw" if len(BRAND)<9 else "6.8vw") if n==1 else "5.2vw"};font-weight:200;line-height:.98;letter-spacing:-.055em">{title}</h1></div>'
 c=f'''<div data-anim="img" class="hero-img-wrap" style="height:66vh;flex:0 0 66vh;position:relative;overflow:hidden;background:#080808"><img src="images/{image}" data-image-slot="s22-hero-21x9" alt="{caption}" style="width:100%;height:100%;object-fit:{image_style};object-position:center 35%"><div style="position:absolute;top:3vh;left:5vw;color:white;font:500 14px var(--mono);letter-spacing:.1em">{BRAND.upper()} / {section.upper()} &nbsp; {n:02d}/16</div>{overlay}<div data-scan style="position:absolute;inset:0;border-top:1px solid var(--accent);pointer-events:none;opacity:.65"></div></div><div class="image-hero-body" data-anim="kpi" style="padding:3.5vh 5vw 4vh;gap:3vw;grid-template-columns:1.1fr 1fr"><div><h2 style="font-size:2.2vw;font-weight:300;line-height:1.15">{title if ui else body}</h2><p style="font-size:14px;font-weight:500;opacity:.65;margin-top:1.5vh">{caption}</p></div><div class="image-hero-stats">{''.join(f'<div style="border-top:1px solid currentColor;padding-top:1.2vh"><div style="font-size:3.6vw;font-weight:200;line-height:1">{v}</div><p style="font-size:16px;font-weight:400;margin-top:1.4vh">{l}</p></div>' for v,l in stats)}</div></div>'''
 slides.append(f'<section class="slide {theme}" data-layout="S22" data-animate="image-hero"><div class="canvas-card" style="padding:0">{c}</div></section>');plan.append({'page':n,'topic':section,'layout':'S22','theme':theme,'animation':'image-hero'})
# 01–04: first establish the product, then show the misunderstanding and repair.
hero('hero dark','Product-page repair','01-reflex-loop.jpg',BRAND,'Fix the page · Not just the ticket',[('1','SKU per audit'),('3','Editable fields'),('5','Live test runs passed')],'AI concept image · Finfold Growth Lab / Yue Zhao')
add('S03','light','The problem',f'''<div class="split-half" style="margin:0 -5vw -4.4vh;flex:1"><div class="half"><div data-anim="head" style="display:flex;align-items:center;gap:2vw">{icon('chat-circle-text','7vw')}<span class="t-cat">SUPPORT</span></div><h2 style="font-size:8.4vw;font-weight:200;line-height:.95;margin:5vh 0">Ticket<br>closed</h2><p class="lead">“The bottle isn’t included”</p></div><div class="half b-grey"><div data-anim="head" style="display:flex;align-items:center;gap:2vw">{icon('storefront','7vw')}<span class="t-cat">PRODUCT PAGE</span></div><h2 style="font-size:8.4vw;font-weight:200;line-height:.95;margin:5vh 0">Still<br>misleading</h2><p class="lead">Same photo · No explanation</p></div></div>''',recipe='statement')
hero('hero dark','The repair','03-rain-texture.jpg','Light rain<br>≠ waterproof','Replace the claim with supported wording',[('Before','100% waterproof'),('After','Light rain only'),('Source','Merchant specs')],'AI concept image · Synthetic example')
hero('light','The merchant','04-merchant-concept.jpg','One place<br>to fix the page','For small-store operators',[('01','Find the issue'),('02','Check the facts'),('03','Approve the edit')],'AI-generated scene')
items=[('cloud-rain','Overclaim','Rewrite'),('chat-circle-text','Missing caption','Clarify'),('ruler','Missing dimensions','Ask'),('warning-circle','Conflicting specs','Hold'),('truck','Late delivery','Hand off'),('seal-check','Broken zipper','Hand off')]
cards=''.join(f'<div class="brief-card card-fill {"is-accent" if i==0 else ""}" style="padding:2vh 2vw;height:24vh;display:flex;flex-direction:column"><div style="display:flex;justify-content:space-between;align-items:start"><h3 style="font-size:1.8vw;font-weight:400">{a}</h3><span class="t-meta">0{i+1}</span></div><div style="display:flex;align-items:end;justify-content:space-between;margin-top:auto">{icon(ic,"6vw")}<p style="font-size:1.7vw;font-weight:400">{b}</p></div></div>' for i,(ic,a,b) in enumerate(items))
add('S16','light','Decisions',head('Fix, ask or hand off')+f'<div class="brief-grid" data-anim="cards" style="display:grid;grid-template-columns:repeat(3,1fr);gap:1.5vw;margin-top:5vh">{cards}</div>',recipe='field-notes')
# 06: actual linear workflow, no simulated autonomous publish.
steps=[('magnifying-glass','Read'),('pencil-line','Draft'),('seal-check','Check'),('hand-tap','Approve'),('eye','Publish + verify')]
flow='<div class="timeline-h" style="min-height:35vh"><div class="tl-row" style="grid-template-columns:repeat(5,1fr)">'+''.join(f'<div class="th-node {"up" if i%2==0 else "down"}"><span class="dot"></span><div class="label">{icon(ic,"5vw")}<div class="name">{label}</div></div></div>' for i,(ic,label) in enumerate(steps))+'</div></div>'
add('S11','dark','Workflow',head('From feedback<br>to a published edit')+flow,recipe='timeline-walk',footer='Approval is required · Restore creates a new version')
hero('light','Workbench','07-live-workbench.jpg','See the source','',[('20','Feedback items'),('2','Images'),('5 MB','Per image')],'Prototype UI · Before audit',True)
blocks=[('cloud','Cloud Run','Interface + API'),('sparkle','Gemini 3.8 Flash','Read · Draft · Check'),('database','Firestore + Storage','Versions + images')]
add('S05','light','Google Cloud',head('Three layers')+'<div class="stack-row" data-anim="cards">'+''.join(f'<div class="stack-block {"b-accent" if i==1 else "b-grey"}" style="min-height:52vh"><div class="layer-nb">0{i+1}</div><div style="margin:5vh 0">{icon(ic,"9vw")}</div><h3 class="layer-ttl" style="font-size:2.5vw">{label}</h3><p class="layer-desc">{d}</p></div>' for i,(ic,label,d) in enumerate(blocks))+'</div>',recipe='stack-build')
hero('hero dark','Approval','09-evidence-concept.jpg','New evidence<br>New approval','Changed facts invalidate the old approval',[('8','Model calls max'),('6','Tool calls max'),('90 s','Run deadline')],'AI concept image')
# 10: visually dominant budget rather than an explanatory ledger.
add('S21','light','Demo limits',head('Small demo<br>Fixed limits')+'''<div class="spec-kpi-grid" data-anim="kpi" style="display:grid;grid-template-columns:repeat(3,1fr);gap:4vw;margin-top:8vh"><div style="border-top:1px solid;padding-top:3vh"><div style="font-size:8vw;font-weight:200">~$0.70</div><p class="lead">Model usage estimate</p></div><div style="border-top:1px solid;padding-top:3vh"><div style="font-size:8vw;font-weight:200">$1</div><p class="lead">Model-call budget</p></div><div style="border-top:1px solid;padding-top:3vh"><div style="font-size:8vw;font-weight:200">0–2</div><p class="lead">Cloud Run instances</p></div></div>'''+ '<div class="spec-bars" style="position:absolute;bottom:10vh;right:5vw;height:8vh;width:18vw;display:flex;gap:1vw;align-items:end">'+''.join(f'<div class="bar-vert" style="background:currentColor;width:1vw;height:{h}%"></div>' for h in [20,30,40,55,70,85,100,75,45])+'</div>',recipe='tech-spec',footer='18 Oct estimate · Infrastructure billed separately')
hero('dark','Published page','11-historical-storefront.jpg','Read it back','',[('Publish','Approved text'),('Verify','Served page'),('Restore','New version')],'Historical UI · 13 Oct 2026',True)
vals=[34.830,69.479,29.209,20.244,30.874]
bars=''.join(f'<div class="row-lbl">{i+1:02d}</div><div class="row-track"><div data-anim="bar" class="row-fill {"accent" if i==1 else ""}" style="width:{v/90*100:.2f}%"></div></div><div class="row-val">{v:.1f}<span class="unit">s</span></div>' for i,v in enumerate(vals))
add('S07','light','Measured execution',head('5 live runs passed')+f'<div class="h-bar-chart" style="margin-top:8vh;gap:3vh 2vw">{bars}</div><div style="display:flex;justify-content:space-between;margin-top:6vh"><p class="lead">35 local tests passed</p><p class="lead">2 earlier timeouts</p></div>',recipe='bar-grow',footer='18 Oct · Audit → approve → publish → verify → restore · Run 02 includes retry')
future=[('seal-check','Grade answers'),('users','Watch users'),('link','Connect a store'),('timer','Measure time saved')]
add('S19','hero light','Next tests',head('Take it to merchants')+'<div class="four-cards" data-anim="cards" style="display:grid;grid-template-columns:repeat(4,1fr);gap:3vw;margin-top:9vh">'+''.join(f'<div class="fc-col" style="border-top:1px solid;padding-top:3vh"><div class="t-meta">0{i+1}</div><div style="margin:5vh 0">{icon(ic,"10vw")}</div><h3 style="font-size:2.3vw;font-weight:300">{label}</h3></div>' for i,(ic,label) in enumerate(future))+'</div>',recipe='four-cards')
add('S10','dark','Try it',f'''<div class="split-half" style="flex:1"><div class="half" style="padding-left:0"><h2 style="font-size:9vw;font-weight:200;line-height:.95;letter-spacing:-.05em">Your turn</h2><p class="lead" style="margin-top:auto">Load the backpack example</p></div><div class="half" style="gap:4vh"><div style="color:var(--accent)">{icon('arrow-up-right','18vw')}</div><a href="https://merchreflex-927668522599.asia-southeast1.run.app" style="font-size:3vw;color:var(--accent)">Open the demo ↗</a><a href="https://github.com/joeymilano/merchreflex" style="font-size:1.7vw;color:inherit">View the code ↗</a><p class="body-sm">Video link pending</p></div></div>''',recipe='split-statement')
add('S19','light','Still to validate',head('What’s untested')+'<div class="four-cards" data-anim="cards" style="display:grid;grid-template-columns:repeat(4,1fr);gap:3vw;margin-top:9vh">'+''.join(f'<div class="fc-col" style="border-top:1px solid;padding-top:3vh">{icon(ic,"9vw")}<h3 style="font-size:2.4vw;font-weight:300;margin-top:5vh">{label}</h3><p class="body-sm" style="margin-top:2vh">{desc}</p></div>' for ic,label,desc in [('database','Real store data','Synthetic demo'),('seal-check','Answer accuracy','Human grading pending'),('users','Merchant use','Task tests pending'),('timer','Business impact','Not measured')])+'</div>',recipe='four-cards')
add('S09','hero dark','Closing',f'''<div data-anim="title" style="flex:1;display:flex;flex-direction:column;justify-content:center"><h2 style="font-size:10vw;font-weight:200;line-height:.95;letter-spacing:-.055em">Fix the page<br><span style="color:var(--accent)">Not just the ticket</span></h2><div style="display:flex;align-items:center;justify-content:space-between;margin-top:7vh"><p style="font-size:4vw;font-weight:200">{BRAND}</p><div class="cross-mat" style="width:18vw;height:17vh;color:var(--accent)"></div></div></div>''',recipe='statement')
exec(suffix)
p=ROOT/'index.html';s=p.read_text().replace('MerchReflex — Product-page repair',BRAND+' — Product-page repair')
css='''
.h-xl{font-size:min(6.7vw,11.9vh);line-height:.98}
.canvas-card .chrome-min{margin-bottom:5vh}
.brief-card.is-accent{background:var(--accent);color:var(--ink)}
.timeline-h .th-node .label svg{margin-bottom:2vh}
.timeline-h .th-node .name{font-size:2vw}
.timeline-h .th-node .dot{border-radius:0}
[data-scan]{transform:translateY(20%);animation:none}
.reflex-active [data-scan]{animation:scan 8s ease-in-out infinite}
.reflex-active .cross-mat{animation:matrix-shift 8s linear infinite}
.reflex-active .hero-img-wrap>img{animation:breathe 14s ease-in-out infinite;transform-origin:60% 50%}
@keyframes scan{0%,100%{transform:translateY(8%);opacity:0}25%,70%{opacity:.55}90%{transform:translateY(90%);opacity:0}}
@keyframes matrix-shift{0%,100%{opacity:.3;transform:translateX(0)}50%{opacity:.8;transform:translateX(-16px)}}
@keyframes breathe{0%,100%{scale:1}50%{scale:1.025}}
body.low-power [data-scan]{display:none}
@media(prefers-reduced-motion:reduce){[data-scan]{display:none}*{animation:none!important;transition:none!important}}
@media print{[data-scan]{display:none!important}.hero-img-wrap>img{scale:1!important}}
'''
s=s.replace('</style>',css+'</style>',1)
s=s.replace('window.__currentSlideIndex = idx;','window.__currentSlideIndex = idx; document.querySelectorAll("#deck > .slide").forEach((s,i)=>s.classList.toggle("reflex-active",i===idx));')
s=s.replace('</body>','<script>document.querySelector("#deck > .slide")?.classList.add("reflex-active");</script></body>')
p.write_text(s)

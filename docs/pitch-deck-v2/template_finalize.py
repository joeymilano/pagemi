start=template.index('<div id="deck">')
end=template.index('<div id="nav"',start)
template=template[:start]+'<div id="deck">\n'+'\n'.join(slides)+'\n</div>\n'+template[end:]
template=template.replace('[必填] 替换为 PPT 标题 · Deck Title','MerchReflex — Product-page repair')
template=template.replace('lang="zh-CN"','lang="en"')
template=re.sub(r'<link[^>]+(?:fonts.googleapis.com|fonts.gstatic.com)[^>]*>','',template)
template=template.replace('--accent:#002FA7','--accent:#BFFF00').replace('--accent-rgb:0,47,167','--accent-rgb:191,255,0').replace('--accent-on:#ffffff','--accent-on:#0a0a0a').replace('--accent-bright:#5B7BFF','--accent-bright:#BFFF00')
template=template.replace('翻页','Slides').replace('动态','Motion').replace('静态','Static').replace('索引','Index')
template=template.replace('<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>','').replace('<script>lucide.createIcons();</script>','')
# Fully local Motion module; no CDN fallback is needed for the packaged deck.
template=template.replace("motion = await import('https://cdn.jsdelivr.net/npm/motion@11.11.17/+esm');","throw new Error('Local motion unavailable; static fallback');")
css='''
/* Presentation-specific overrides: shared grid and readable type. */
.h-xl{font-size:min(5.5vw,9.7vh);font-weight:200;line-height:1.02;letter-spacing:-.045em}
.lead{font-size:clamp(18px,1.4vw,26px);font-weight:400}
.body{font-size:clamp(18px,1.15vw,22px);opacity:.86;line-height:1.5}
.body-sm{font-size:16px;font-weight:400}
.canvas-card .chrome-min{margin-bottom:4vh}
.sub-card,.dot,.geo-dot,.geo-circle-o{border-radius:0!important}
.timeline-h .th-node .name{font-size:24px;font-weight:400}
.timeline-h .th-node .desc{font-size:16px}
.slide.dark .timeline-h .th-node .name{color:var(--paper)}
.slide.dark .timeline-h .th-node .desc,.slide.dark .timeline-h .th-node .yr{color:#ccc}
.slide.dark .timeline-h .th-node .dot{background:var(--accent)}
.slide.dark .image-hero-body{color:var(--paper)}
.slide.hero.light .canvas-card{background:var(--paper)}
.slide[data-layout="S03"] .half{padding-bottom:10vh}
.slide[data-layout="S10"] .half{padding-top:2vh;padding-bottom:8vh}
.h-bar-chart .row-track{height:3vh}
.slide[data-layout="S19"] .four-cards{margin-top:7vh!important}
.slide[data-layout="S19"] .body{font-size:19px}
a{text-decoration:none}
@media print{
 @page{size:1600px 900px;margin:0}
 html,body{width:1600px;height:auto;overflow:visible;background:var(--paper);print-color-adjust:exact;-webkit-print-color-adjust:exact}
 #deck{position:relative!important;display:block!important;width:1600px!important;height:auto!important;transform:none!important;transition:none}
 .slide{width:1600px;height:900px;break-after:page;page-break-after:always;overflow:hidden}
 .slide:last-child{break-after:auto;page-break-after:auto}
 .canvas-card{width:1600px;height:900px}
 #nav,#hint,#overview,canvas{display:none!important}
 [data-anim]{opacity:1!important;transform:none!important}
 *{animation:none!important;transition:none!important}
}
'''
template=template.replace('</style>',css+'\n</style>',1)
template=template.replace("'./assets/motion.min.js'", "'data:text/javascript;base64,"+base64.b64encode((ROOT/'assets/motion.min.js').read_bytes()).decode()+"'")
(ROOT/'index.html').write_text(template)
(ROOT/'slide-plan.json').write_text(json.dumps(plan,indent=2))
print('Created',len(slides),'slides')

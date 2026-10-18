from pathlib import Path
import re, json, shutil, base64

ROOT=Path(__file__).resolve().parent
SKILL=Path('/Users/joeyzhao/.codex/skills/guizang-ppt-skill')
template=(ROOT/'assets/template-swiss.html').read_text()
slides=[]
plan=[]
def chrome(n,section):
    return f'<header class="chrome-min"><div class="l">MERCHREFLEX / {section}</div><div class="r">AI BUILDER CUP 2026 &nbsp; {n:02d} / 16</div></header>'
def head(title,kicker=''):
    return f'<div data-anim="head"><h2 class="h-xl" style="margin-top:1.5vh">{title}</h2></div>'
def note(text):
    return f'<footer class="foot" style="letter-spacing:0;text-transform:none;opacity:.8;font-size:14px">{text}</footer>'
def add(layout,theme,section,content,recipe='grid-reveal',footer='',split=False):
    n=len(slides)+1
    slides.append(f'<section class="slide {theme}{" split" if split else ""}" data-layout="{layout}" data-animate="{recipe}" aria-label="{n}. {section}"><div class="canvas-card">{chrome(n,section) if not split else ""}{content}{note(footer) if footer else ""}</div></section>')
    plan.append({'page':n,'topic':section,'layout':layout,'theme':theme,'animation':recipe})
def imgslide(theme,section,image,title,body,stats,caption,ui=False):
    n=len(slides)+1
    style='object-fit:contain;object-position:center center' if ui else 'object-fit:cover;object-position:center 35%'
    # S22: image area, title block, explanation and three factual anchors.
    content=f'''<div data-anim="img" class="hero-img-wrap" style="height:56vh;flex:0 0 56vh;position:relative;overflow:hidden;background:var(--ink)">
      <img data-image-slot="s22-hero-21x9" src="images/{image}" alt="{caption}" style="width:100%;height:100%;{style}">
      <div style="position:absolute;left:5vw;top:3vh;background:var(--ink);color:var(--paper);padding:.8vh 1vw;font-family:var(--mono);font-size:14px">MERCHREFLEX / {section.upper()} &nbsp; {n:02d}/16</div>
      {'' if ui else f'<div data-anim="title-block" class="hero-overlay-block" style="position:absolute;left:5vw;bottom:3.6vh;background:var(--paper);color:var(--ink);padding:2vh 2vw;max-width:43vw"><h1 style="font-size:min(4.9vw,8.6vh);font-weight:200;line-height:.98;letter-spacing:-.045em">{title}</h1></div>'}
    </div><div class="image-hero-body" data-anim="kpi" style="padding-top:3.6vh;padding-bottom:8vh;gap:3vw;grid-template-columns:1.1fr 1fr">
      <div><h2 style="font-size:min(2.6vw,4.5vh);font-weight:300;line-height:1.1;margin-bottom:1vh">{title if ui else 'Fix the page · Not just the ticket' if n==1 else section}</h2><p class="lead" style="font-size:20px">{body}</p><p style="font-size:14px;margin-top:1.5vh;opacity:.65">{caption}</p></div>
      <div class="image-hero-stats">{''.join(f'<div style="border-top:1px solid currentColor;padding-top:1.4vh"><div style="font-size:min(3.8vw,6.7vh);font-weight:200;line-height:1.05">{v}</div><div style="font-size:16px;margin-top:1.2vh;line-height:1.35">{l}</div></div>' for v,l in stats)}</div>
    </div>'''
    slides.append(f'<section class="slide {theme}" data-layout="S22" data-animate="image-hero" aria-label="{n}. {section}"><div class="canvas-card" style="padding:0">{content}</div></section>')
    plan.append({'page':n,'topic':section,'layout':'S22','theme':theme,'animation':'image-hero'})
def four(items):
    return '<div class="four-cards" data-anim="cards" style="display:grid;grid-template-columns:repeat(4,1fr);gap:2.2vw;margin-top:9vh">'+''.join(f'<div class="fc-col" style="border-top:2px solid currentColor;padding-top:2vh"><div class="t-meta">0{i+1}</div><h3 style="font-size:min(3vw,5.2vh);font-weight:300;line-height:1.1;margin:3vh 0 2vh">{a}</h3><p class="body">{b}</p></div>' for i,(a,b) in enumerate(items))+'</div>'
def timeline(items):
    return '<div class="timeline-h" style="min-height:30vh"><div class="tl-row" style="grid-template-columns:repeat('+str(len(items))+',1fr)">'+''.join(f'<div class="th-node {"up" if i%2==0 else "down"}"><span class="dot" style="border-radius:0"></span><div class="label"><div class="yr">0{i+1}</div><div class="name">{a}</div><div class="desc">{b}</div></div></div>' for i,(a,b) in enumerate(items))+'</div></div>'


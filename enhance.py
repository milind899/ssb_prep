import re

SRC = "index.html"
OUT = "index.html"

with open(SRC, encoding="utf-8") as f:
    html = f.read()

CSS = """<style id="redesign-v2">
:root{--bg:#f7f8f9;--surface:#fff;--surface-2:#f0f1f3;--surface-3:#e6e8eb;--ink:#1a1b1e;--ink-2:#3d4044;--muted:#6c737a;--border:#dde0e4;--accent:#2563a8;--accent-bg:#edf3fb;--accent-2:#1d6b40;--accent-2-bg:#e8f4ee;--warm:#9b3523;--warm-bg:#fdf0ed;--shadow:none;--shadow-strong:0 2px 12px rgba(0,0,0,.08);--radius:5px;--hh:56px;--font:-apple-system,BlinkMacSystemFont,'Segoe UI',system-ui,'Helvetica Neue',Arial,sans-serif;--mono:ui-monospace,'Cascadia Mono','Fira Code',Consolas,'Courier New',monospace}
[data-theme="dark"]{--bg:#111316;--surface:#1a1d21;--surface-2:#22262b;--surface-3:#2b303a;--ink:#e2e6ea;--ink-2:#c0c6cc;--muted:#80888f;--border:#2e333a;--accent:#60a5e0;--accent-bg:#152030;--accent-2:#5aaa7a;--accent-2-bg:#0f2518;--warm:#d47060;--warm-bg:#2a1210;--shadow-strong:0 2px 16px rgba(0,0,0,.3)}
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:calc(var(--hh) + 1.5rem)}
body{margin:0;background:var(--bg);color:var(--ink);font:400 15px/1.65 var(--font);-webkit-font-smoothing:antialiased}
h1,h2,h3,h4{margin:0;font-weight:600}
a{color:inherit}
button,input,textarea,select{font:inherit}
button{cursor:pointer}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:3px}
.top{position:sticky;top:0;z-index:30;height:var(--hh);background:var(--surface);border-bottom:1px solid var(--border);padding:0 1.5rem}
.top-inner{max-width:1600px;margin:0 auto;height:100%}
.row{display:flex;align-items:center;gap:.75rem;height:100%;flex-wrap:nowrap}
.brand{display:flex;align-items:center;gap:.65rem;text-decoration:none;flex-shrink:0}
.brand-mark{width:36px;height:36px;display:grid;place-items:center;background:var(--accent);color:#fff;border-radius:6px;font:700 .72rem var(--mono);letter-spacing:0}
.brand-copy{display:grid;gap:0}
.brand-copy strong{font-size:.95rem;font-weight:700;letter-spacing:-.01em;color:var(--ink)}
.brand-copy span{font-size:.65rem;font-weight:500;color:var(--muted);text-transform:uppercase;letter-spacing:.08em}
.search-wrap{flex:1;max-width:420px;position:relative}
.search{display:block;width:100%;height:36px;border:1px solid var(--border);border-radius:6px;padding:0 .9rem 0 2.2rem;background:var(--surface-2);color:var(--ink);font-size:.84rem;outline:none;transition:border-color .15s,background .15s}
.search:focus{background:var(--surface);border-color:var(--accent)}
.btn{display:inline-flex;align-items:center;gap:.4rem;border:1px solid var(--border);background:var(--surface);color:var(--ink);border-radius:5px;padding:.4rem .75rem;font-size:.78rem;font-weight:500;cursor:pointer;transition:background .12s,border-color .12s;white-space:nowrap;text-decoration:none;line-height:1.4}
.btn:hover{background:var(--surface-2);border-color:var(--accent)}
.btn.primary{background:var(--accent);color:#fff;border-color:var(--accent)}
.btn.primary:hover{opacity:.9}
.btn[aria-pressed="true"]{background:var(--accent);color:#fff;border-color:var(--accent)}
.btn.danger{color:var(--warm)}
.actions{display:flex;align-items:center;gap:.4rem;margin-left:auto}
.main-links{display:flex;gap:.2rem;align-items:center}
.main-links a{font-size:.82rem;font-weight:500;color:var(--muted);text-decoration:none;padding:.35rem .65rem;border-radius:5px;transition:color .12s,background .12s}
.main-links a:hover{color:var(--ink);background:var(--surface-2)}
.progress-row,.portal-links{display:none}
.shell{display:grid;grid-template-columns:260px minmax(0,1fr);gap:0;max-width:1400px;margin:0 auto;min-height:calc(100vh - var(--hh))}
nav{position:sticky;top:var(--hh);height:calc(100vh - var(--hh));overflow-y:auto;border-right:1px solid var(--border);background:var(--surface);padding:1rem .75rem;scrollbar-width:thin;scrollbar-color:var(--border) transparent}
main{min-width:0;padding:2rem 2.5rem 4rem;max-width:900px}
.nav-head{display:flex;justify-content:space-between;align-items:center;padding:0 .4rem .75rem;border-bottom:1px solid var(--border);margin-bottom:.75rem}
.nav-head strong{font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--muted)}
nav ul{list-style:none;padding:0;margin:0}
.np{margin:0 0 .5rem}
.npn{display:flex;align-items:center;justify-content:space-between;padding:.35rem .5rem;border-radius:4px;font-size:.72rem;font-weight:700;color:var(--ink-2);cursor:pointer;user-select:none;border-left:3px solid var(--pc,var(--border))}
.npn:hover{background:var(--surface-2)}
.npp{font-size:.62rem;color:var(--muted);font-weight:500;font-family:var(--mono)}
.np>ul{display:none;padding-left:0;margin-top:.2rem}
.np.open>ul{display:block}
.nc a{display:flex;align-items:baseline;gap:.4rem;padding:.32rem .4rem .32rem .75rem;color:var(--muted);text-decoration:none;border-radius:4px;font-size:.75rem;transition:color .12s,background .12s}
.nc a:hover{color:var(--ink);background:var(--surface-2)}
.nc.active a{color:var(--ink);background:var(--accent-bg);font-weight:600}
.nc .code{font-family:var(--mono);font-size:.64rem;font-weight:600;color:var(--pc,var(--accent));flex-shrink:0;min-width:1.8rem}
.nt{flex:1;line-height:1.35}
.ncnt{font-family:var(--mono);font-size:.62rem;color:var(--muted);flex-shrink:0}
.nc[data-tier="1"] .nt::after{content:" \u2605";color:var(--warm);font-size:.58rem}
.atlas-hero{display:grid;grid-template-columns:1fr 1fr;gap:2rem;padding:2.5rem 0 2rem;border-bottom:1px solid var(--border);margin-bottom:2rem}
.atlas-hero h1{font-size:clamp(1.8rem,3.5vw,2.8rem);font-weight:700;line-height:1.1;letter-spacing:-.025em;margin:.5rem 0 1rem}
.atlas-hero .lead{font-size:1rem;color:var(--muted);line-height:1.65;margin:0 0 1.25rem;max-width:42rem}
.kicker{font-size:.7rem;font-weight:600;text-transform:uppercase;letter-spacing:.1em;color:var(--accent);margin-bottom:.5rem;display:block}
.hero-actions{display:flex;gap:.6rem;flex-wrap:wrap}
.hero-note{font-size:.78rem;color:var(--muted);margin-top:.75rem}
.method h2{font-size:.9rem;font-weight:700;border-bottom:1px solid var(--border);padding-bottom:.5rem;margin-bottom:.75rem}
.method ol{list-style:none;counter-reset:m}
.method li{counter-increment:m;display:grid;grid-template-columns:1.8rem 1fr;gap:0 .5rem;padding:.6rem 0;border-bottom:1px solid var(--border);font-size:.88rem}
.method li::before{content:counter(m,decimal-leading-zero);font-family:var(--mono);font-size:.72rem;color:var(--accent);font-weight:700;padding-top:.2rem}
.method b{display:block;font-weight:600;margin-bottom:.15rem}
.method span{color:var(--muted);line-height:1.5}
.domain-section{margin-bottom:2rem}
.section-eyebrow{font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:var(--accent);display:block;margin-bottom:.3rem}
.section-heading h2{font-size:1.3rem;font-weight:700}
.section-heading p{font-size:.88rem;color:var(--muted);margin-top:.25rem}
.domain-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:.75rem}
.domain-card{display:block;padding:1rem 1.1rem;background:var(--surface);border:1px solid var(--border);border-top:3px solid var(--domain,var(--accent));border-radius:6px;text-decoration:none;transition:transform .12s,box-shadow .12s}
.domain-card:hover{transform:translateY(-1px);box-shadow:0 4px 16px rgba(0,0,0,.07)}
.domain-code{font-family:var(--mono);font-size:.62rem;font-weight:700;color:var(--domain,var(--accent));display:block;margin-bottom:.4rem;text-transform:uppercase;letter-spacing:.06em}
.domain-card strong{display:block;font-size:.95rem;font-weight:700;color:var(--ink);margin-bottom:.3rem}
.domain-desc{font-size:.78rem;color:var(--muted);line-height:1.5;display:block}
.domain-foot{display:none}
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:.75rem;margin-bottom:1rem}
.metric{background:var(--surface);border:1px solid var(--border);border-radius:6px;padding:.9rem 1rem}
.metric span{font-size:.65rem;font-weight:600;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);display:block;margin-bottom:.4rem}
.metric strong{font-size:1.75rem;font-weight:700;display:block;line-height:1;font-family:var(--mono)}
.metric small{font-size:.7rem;color:var(--muted);display:block;margin-top:.25rem}
.planner{display:flex;align-items:center;justify-content:space-between;gap:1rem;border:1px solid var(--border);border-radius:6px;background:var(--surface);padding:1rem 1.25rem;flex-wrap:wrap}
.planner h3{font-size:.95rem;font-weight:700;margin-bottom:.2rem}
.planner p{font-size:.82rem;color:var(--muted);margin:0}
.plan-date{display:grid;gap:.3rem}
.plan-date span{font-size:.65rem;font-weight:600;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
.plan-date input{padding:.4rem .6rem;border:1px solid var(--border);border-radius:4px;background:var(--surface-2);color:var(--ink);font-size:.84rem}
.practice{border:1px solid var(--border);border-radius:6px;background:var(--surface);padding:1rem 1.25rem;margin-top:.75rem}
.practice-kicker{font-size:.65rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--accent-2);display:block;margin-bottom:.3rem}
.practice h3{font-size:.95rem;margin-bottom:.3rem}
.practice p{font-size:.82rem;color:var(--muted);margin-bottom:.75rem}
.question-box{min-height:60px;border-left:3px solid var(--accent-2);padding:.65rem .9rem;background:var(--accent-2-bg);border-radius:0 4px 4px 0;font-size:.88rem;line-height:1.55;margin-bottom:.75rem}
.practice-controls{display:flex;align-items:center;gap:.5rem;flex-wrap:wrap}
.timer{font-family:var(--mono);font-size:1.1rem;font-weight:700;color:var(--accent);margin-left:auto}
.pt{font-size:1.5rem;font-weight:700;margin:2rem 0 1rem;padding-bottom:.65rem;border-bottom:2px solid var(--pc,var(--border));display:flex;align-items:baseline;gap:.75rem;letter-spacing:-.01em}
.chap{background:var(--surface);border:1px solid var(--border);border-left:3px solid var(--pc,var(--border));border-radius:6px;margin:.5rem 0;overflow:hidden}
.chap[open]{border-left-width:4px}
.chap summary{display:flex;align-items:center;gap:.65rem;padding:.8rem 1rem;cursor:pointer;list-style:none;min-height:52px;transition:background .1s}
.chap summary:hover{background:var(--surface-2)}
.chap summary::-webkit-details-marker{display:none}
.chap summary::before{content:'';width:5px;height:5px;border-right:1.5px solid var(--muted);border-bottom:1.5px solid var(--muted);transform:rotate(-45deg);transition:transform .15s;flex-shrink:0}
.chap[open]>summary::before{transform:rotate(45deg)}
.chap h3{font:600 .92rem/1.3 var(--font);margin:0;flex:1;letter-spacing:-.01em}
.code{display:inline-flex;align-items:center;padding:.18rem .4rem;background:var(--surface-2);border-radius:3px;font:700 .68rem var(--mono);color:var(--pc,var(--accent));flex-shrink:0}
.cnt{font:500 .68rem var(--mono);color:var(--muted);flex-shrink:0}
.tier{font:600 .6rem var(--mono);border-radius:3px;padding:.18rem .42rem;border:1px solid var(--border);color:var(--muted);flex-shrink:0;text-transform:uppercase}
.t1{background:var(--warm-bg);border-color:var(--warm);color:var(--warm)}
.t2,.t3{background:var(--surface-2)}
.chap .all{width:1rem;height:1rem;accent-color:var(--accent);flex-shrink:0;cursor:pointer}
.chap.complete{border-left-color:var(--accent-2)}
.chap.complete h3{color:var(--muted)}
.cb{padding:.25rem 1.1rem 1.1rem 1.25rem;border-top:1px solid var(--border)}
.cb>*{max-width:72ch}
.cb p{margin:.6rem 0;color:var(--ink-2);font-size:.92rem}
.cb strong{font-weight:700;color:var(--ink)}
.cb em{color:var(--accent);font-style:normal;font-weight:600}
.cb ul{list-style:none;padding:0;margin:.3rem 0 .8rem}
.cb ol{padding-left:1.5rem;margin:.3rem 0 .8rem}
.cb li{margin:.22rem 0;color:var(--ink-2)}
.blk{margin:1.2rem 0 0}
.blk>h4{font:600 .68rem var(--font);text-transform:uppercase;letter-spacing:.1em;color:var(--accent);margin:0 0 .5rem;padding-bottom:.35rem;border-bottom:1px solid var(--border)}
.blk.write{background:var(--surface-2);padding:.85rem 1rem;border-radius:4px;border-left:3px solid var(--accent-2)}
.blk.write>h4{border:0;padding:0;color:var(--accent-2)}
.blk.write p{margin:.3rem 0 0;font-size:.88rem;color:var(--ink-2)}
.blk.context{background:var(--accent-bg);padding:.85rem 1rem;border-radius:4px;border-left:3px solid var(--accent);margin-top:.8rem}
.blk.context>h4{border:0;padding:0;color:var(--accent);margin-bottom:.35rem;font:600 .68rem var(--font);text-transform:uppercase;letter-spacing:.1em}
.blk.context p{margin:0;font-size:.84rem;color:var(--ink-2);line-height:1.6}
.blk.leads>h4{color:var(--accent)}
.blk.cross>h4{color:var(--warm)}
.item{border-bottom:1px solid var(--border)}
.item:last-child{border-bottom:0}
.item label{display:grid;grid-template-columns:1.2rem 1fr;gap:.6rem;padding:.55rem 0;cursor:pointer;align-items:start}
.item label:hover span{color:var(--ink)}
.item input[type="checkbox"]{margin-top:.33rem;accent-color:var(--accent-2);width:1rem;height:1rem;cursor:pointer}
.item.done span{color:var(--muted);text-decoration:line-through;text-decoration-color:var(--border)}
.item span{font-size:.88rem;line-height:1.55;color:var(--ink-2)}
.blk.cross ol{counter-reset:q;padding:0}
.blk.cross .item{counter-increment:q}
.blk.cross .item label{grid-template-columns:1.8rem 1fr}
.blk.cross .item label::before{content:counter(q);font:700 1rem/1.4 var(--font);color:var(--warm);grid-column:1;padding-top:.05rem}
.blk.cross .item input{display:none}
.blk.cross .item span{grid-column:2;font-size:.92rem;line-height:1.55}
.blk.cross .item:has(input:checked) label::before{color:var(--muted)}
.blk.cross .item:has(input:checked) span{color:var(--muted)}
.drill-btn{margin-top:.75rem;width:100%;text-align:center;border-color:var(--accent);color:var(--accent);font-weight:600;border-radius:4px;padding:.5rem 1rem}
.drill-btn:hover{background:var(--accent-bg)}
.topic-tools{display:flex;align-items:center;gap:.5rem;flex-wrap:wrap;border-top:1px solid var(--border);margin-top:1rem;padding-top:.75rem}
.bookmark{font-size:.75rem;font-weight:500;padding:.35rem .7rem;border:1px solid var(--border);border-radius:4px;background:var(--surface);color:var(--muted);cursor:pointer}
.bookmark:hover,.bookmark[aria-pressed="true"]{border-color:var(--accent);color:var(--accent);background:var(--accent-bg)}
.notes-box summary{display:inline-flex;padding:.35rem .7rem;border:1px solid var(--border);border-radius:4px;font-size:.75rem;font-weight:500;cursor:pointer;color:var(--ink);list-style:none}
.notes-box summary::before{display:none}
.notes-box[open] summary{border-color:var(--accent);color:var(--accent)}
.notes-box textarea{display:block;width:100%;min-height:90px;resize:vertical;margin-top:.5rem;background:var(--surface-2);border:1px solid var(--border);border-radius:4px;color:var(--ink);padding:.65rem .75rem;font-size:.84rem;line-height:1.55}
.note-status{font-size:.65rem;color:var(--muted);margin-top:.2rem}
.hidedone .item.done{display:none}
.t1only .chap:not([data-tier="1"]):not([data-tier="info"]){display:none}
.t1only .nc:not([data-tier="1"]):not([data-tier="info"]){display:none}
.focusonly .chap:not(.bookmarked){display:none}
.focusonly .nc:not(.is-bookmarked){display:none}
.results,.crumbs{display:none}
.crumbs{gap:.5rem;align-items:center;flex-wrap:wrap;font-size:.82rem;color:var(--muted);margin-bottom:1.2rem}
.crumbs a{color:var(--muted)}
.crumbs b{font-weight:600;color:var(--ink)}
.empty{display:none;color:var(--muted);padding:1.25rem;background:var(--surface);border:1px dashed var(--border);border-radius:6px;font-size:.88rem}
.res{display:block;padding:.9rem 0;border-bottom:1px solid var(--border);text-decoration:none;color:var(--ink)}
.res b{font:600 1rem var(--font);display:block}
.res small{display:block;color:var(--muted);font-size:.82rem}
.res span{color:var(--muted);font-size:.88rem}
.v-part .crumbs,.v-topic .crumbs,.v-search .crumbs{display:flex}
.v-search .results{display:block}
.pager{justify-content:space-between;gap:1rem;margin:2rem 0 0;padding-top:1rem;border-top:1px solid var(--border)}
.pager a{flex:1;text-decoration:none;color:var(--ink);padding:.6rem 0;font-weight:600;font-size:.95rem}
.pager a small{display:block;font-size:.75rem;color:var(--muted);font-weight:400}
.pager a:last-child{text-align:right}
#drill{position:fixed;inset:0;z-index:100;background:var(--surface);display:flex;flex-direction:column;overflow:auto}
#drill[hidden]{display:none}
.dr-head{display:flex;align-items:center;gap:1rem;padding:.9rem 1.5rem;border-bottom:1px solid var(--border);position:sticky;top:0;background:var(--surface);z-index:1;flex-shrink:0}
#drT{flex:1;font:600 .85rem var(--mono);color:var(--muted);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
#drN{font:400 .78rem var(--mono);color:var(--muted)}
.dr-body{flex:1;padding:2rem 1.5rem;max-width:680px;margin:0 auto;width:100%}
#drQ{font-size:1.5rem;line-height:1.4;font-weight:500;margin-bottom:1.5rem}
#drC{margin-bottom:1rem;padding:.75rem 1rem;border-left:3px solid var(--accent-2);background:var(--accent-2-bg);border-radius:0 4px 4px 0;font-size:.88rem;line-height:1.55}
#drRate{display:flex;gap:.5rem;flex-wrap:wrap;margin:.75rem 0;align-items:center}
#drRate button{font:600 .82rem var(--font);border:1px solid var(--border);background:var(--surface);color:var(--ink);padding:.4rem .9rem;border-radius:4px;cursor:pointer}
#drRate button[aria-pressed="true"]{background:var(--ink);color:var(--surface);border-color:var(--ink)}
.drill-stat{font:400 .78rem var(--mono);color:var(--muted);margin-top:.3rem}
#drAud{display:block;margin-top:.75rem;width:100%;border-radius:4px}
.dr-foot{display:flex;align-items:center;gap:.5rem;padding:1rem 1.5rem;border-top:1px solid var(--border);position:sticky;bottom:0;background:var(--surface);flex-wrap:wrap}
.dr-foot .timer{margin:0 auto 0 .5rem}
.rate{display:flex;flex-wrap:wrap;gap:.4rem;align-items:center;font-size:.88rem;margin:.5rem 0}
.linkbtn{background:none;border:0;color:var(--muted);text-decoration:underline;cursor:pointer;font-size:.82rem;padding:0}
#pal{position:fixed;inset:0;z-index:200;background:rgba(0,0,0,.4);display:flex;align-items:flex-start;justify-content:center;padding-top:8vh}
#pal[hidden]{display:none}
.pal-box{background:var(--surface);border:1px solid var(--border);border-radius:8px;box-shadow:0 20px 60px rgba(0,0,0,.2);width:540px;max-width:90vw;overflow:hidden}
.pal-box input{display:block;width:100%;padding:.9rem 1rem;border:0;border-bottom:1px solid var(--border);background:transparent;color:var(--ink);font:.95rem var(--font);outline:none}
#palList{list-style:none;max-height:340px;overflow-y:auto}
#palList li{display:flex;align-items:center;gap:.75rem;padding:.65rem 1rem;cursor:pointer;border-bottom:1px solid var(--border);font-size:.88rem}
#palList li:last-child{border-bottom:0}
#palList li:hover,#palList li[aria-selected="true"]{background:var(--accent-bg)}
.pal-empty{padding:1.5rem;text-align:center;color:var(--muted);font-size:.88rem}
.more>summary{list-style:none;cursor:pointer}
.more>summary::-webkit-details-marker{display:none}
.more-panel{position:absolute;right:0;top:calc(100% + .4rem);z-index:50;min-width:14rem;background:var(--surface);border:1px solid var(--border);border-radius:5px;padding:.4rem;box-shadow:0 8px 24px rgba(0,0,0,.1)}
.more-panel .btn{text-align:left;width:100%}
.more{position:relative}
.schedule-intro{margin-bottom:1.5rem;padding:1rem 1.1rem;background:var(--surface-2);border-left:3px solid var(--accent);border-radius:0 4px 4px 0}
.schedule-kicker,.routine-label{display:block;font-size:.65rem;font-weight:600;text-transform:uppercase;letter-spacing:.1em;color:var(--accent);margin-bottom:.3rem}
.schedule-intro h3{font-size:1rem;margin-bottom:.3rem}
.schedule-intro p{font-size:.84rem;color:var(--muted);margin:0}
.schedule-grid,.routine-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:.75rem;margin-bottom:1.2rem}
.track-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:.75rem;margin-bottom:1.2rem}
.schedule-group,.track-card,.routine-card{background:var(--surface);border:1px solid var(--border);border-radius:6px;padding:.9rem 1rem}
.schedule-group h4,.track-card h4,.routine-card h4{font-size:.9rem;margin-bottom:.65rem}
.schedule-list{list-style:none}
.schedule-entry{display:grid;grid-template-columns:72px 1fr auto;align-items:baseline;gap:.4rem;padding:.4rem 0;border-top:1px solid var(--border);font-size:.8rem}
.schedule-entry:first-child{border-top:0}
.schedule-day{font:700 .68rem var(--mono);color:var(--accent)}
.schedule-entry a,.track-card a,.routine-card a{color:var(--ink);text-decoration:none;font-weight:500}
.schedule-entry a:hover,.track-card a:hover{text-decoration:underline}
.schedule-ref{font:600 .6rem var(--mono);background:var(--surface-2);padding:.15rem .35rem;border-radius:3px;color:var(--muted)}
.track-head{display:flex;justify-content:space-between;align-items:flex-start;gap:.5rem}
.track-head span{font:700 .62rem var(--mono);color:var(--accent);background:var(--accent-bg);padding:.18rem .38rem;border-radius:3px}
.track-card p,.routine-card p{font-size:.78rem;color:var(--muted);margin:.3rem 0 .6rem}
.track-card ul{list-style:none}
.track-card li{display:flex;justify-content:space-between;gap:.4rem;padding:.3rem 0;border-top:1px solid var(--border);font-size:.78rem}
.track-card li small{font:600 .62rem var(--mono);color:var(--muted)}
.routine-links{display:flex;flex-wrap:wrap;gap:.3rem}
.routine-links a{font-size:.72rem;background:var(--surface-2);border-radius:4px;padding:.28rem .5rem;color:var(--ink);text-decoration:none}
.routine-links a:hover{background:var(--accent-bg);color:var(--accent)}
.routine-wide{grid-column:1/-1}
.sprint{margin-bottom:2rem;padding-top:1.5rem;border-top:1px solid var(--border)}
.sp-head p{font-size:.68rem;font-weight:600;text-transform:uppercase;letter-spacing:.1em;color:var(--accent);margin-bottom:.3rem}
.sp-head h2{font-size:1.5rem;font-weight:700;margin-bottom:1.2rem}
.sp-grid{display:grid;grid-template-columns:1fr 280px;gap:2rem}
.sp-meta{display:flex;gap:1.5rem;margin-bottom:.75rem;padding-bottom:.75rem;border-bottom:1px solid var(--border)}
.sp-meta div b{display:block;font-size:1.8rem;font-weight:700;line-height:1}
.sp-meta div span{font-size:.65rem;text-transform:uppercase;letter-spacing:.07em;color:var(--muted);display:block;margin-top:.2rem}
.sp-list{list-style:none}
.sp-list li{display:grid;grid-template-columns:3rem 1fr auto;gap:.5rem 1rem;padding:.65rem 0;border-bottom:1px solid var(--border);font-size:.88rem;align-items:baseline}
.sp-list .c{font-family:var(--mono);font-size:.72rem;font-weight:700;color:var(--accent);letter-spacing:.04em}
.sp-list a{font-weight:600;color:var(--ink);text-decoration:none}
.sp-list a:hover{text-decoration:underline}
.sp-list .p{font-size:.78rem;color:var(--muted);white-space:nowrap}
.sp-stats{display:grid;grid-template-columns:1fr 1fr;border:1px solid var(--border);border-radius:6px;overflow:hidden;margin-bottom:1rem}
.sp-stats div{padding:.65rem .8rem;background:var(--surface)}
.sp-stats div:nth-child(2n){border-left:1px solid var(--border)}
.sp-stats div:nth-child(n+3){border-top:1px solid var(--border)}
.sp-stats dt{font-size:.62rem;font-weight:600;text-transform:uppercase;letter-spacing:.07em;color:var(--muted)}
.sp-stats dd{font-size:1.35rem;font-weight:700;margin:.15rem 0 0}
.sp-proj{padding:.6rem .8rem;border-left:3px solid var(--accent-2);background:var(--accent-2-bg);font-size:.84rem;line-height:1.5;border-radius:0 4px 4px 0}
.sp-road summary{cursor:pointer;padding:.6rem 0;font-weight:600;font-size:.88rem}
.sp-road{margin-top:1rem;padding-top:.75rem;border-top:1px solid var(--border)}
.sp-day{display:grid;grid-template-columns:7rem 1fr 4rem;gap:.75rem;padding:.4rem 0;border-bottom:1px solid var(--border);font-size:.82rem}
.sp-day a{color:var(--ink)}
.sp-day span:last-child{text-align:right;color:var(--muted)}
.sp-status.ok{color:var(--accent-2)}
.sp-status.late{color:var(--warm)}
.sp-note{font-size:.82rem;color:var(--muted);margin-top:.6rem}
.sp-rev,.sp-revn{font-size:.84rem}
.sp-revn{color:var(--muted)}
.site-foot{border-top:1px solid var(--border);margin-top:3rem;padding-top:1.5rem;display:grid;grid-template-columns:repeat(auto-fit,minmax(15rem,1fr));gap:1.5rem;font-size:.84rem;color:var(--muted)}
.site-foot h4{font-size:.95rem;color:var(--ink);margin-bottom:.3rem}
.site-foot p{margin:0}
.footnote{color:var(--muted);font-size:.75rem;margin:2rem 0 0;padding:1rem 0;border-top:1px solid var(--border)}
.home-progress{margin:1rem 0 0;font:400 .82rem var(--mono);color:var(--muted)}
.home-progress i{display:block;height:3px;background:var(--border);margin-top:.4rem;border-radius:2px}
.home-progress i b{display:block;height:100%;background:var(--accent);width:var(--p,0%);border-radius:2px}
.part{max-width:820px}
.v-part .part.current,.v-topic .part.current{display:block}
.v-topic .part.current>:not(.chap){display:none}
.v-topic .chap:not(.current){display:none}
.v-topic .pager{display:flex}
.v-part .chap{border-left:0!important;border:0;border-bottom:1px solid var(--border);border-radius:0;background:none;margin:0}
.v-part .chap>summary{padding:.9rem .4rem}
.v-part .chap>summary:hover{background:var(--surface-2)}
.v-part .chap>summary::before{display:none}
.v-part .chap>summary::after{content:"\u203a";font-size:1.3rem;color:var(--muted);line-height:1}
.v-part .chap .cb,.v-part .all{display:none}
.v-part .chap h3{font-size:1.1rem}
.v-topic .chap{border:0!important;background:none!important}
.v-topic .chap>summary{pointer-events:none;padding:0 0 1rem;border-bottom:2px solid var(--ink);margin-bottom:1.5rem}
.v-topic .chap>summary .all{pointer-events:auto}
.v-topic .chap h3{font-size:clamp(1.5rem,3vw,2.2rem);line-height:1.15}
.v-topic .chap .cb{padding:0}
.v-topic .item label{padding:.4rem 0}
.v-part .part.current .pt{font-size:1.75rem}
.part-meta{font:400 .84rem var(--mono);color:var(--muted);margin:-.4rem 0 1.2rem}
.ladder{margin:1rem 0}
.ladder ol{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;align-items:flex-start;border-left:2px solid var(--border);padding-left:.75rem}
.ladder li{padding:.3rem .5rem;font-size:.82rem;background:var(--surface-2);border-radius:3px;margin-bottom:2px}
.ladder figcaption{font-size:.72rem;color:var(--muted);margin-top:.5rem}
.item[data-conf="1"] span{color:var(--warm)!important}
.item[data-conf="2"] span{color:var(--accent)!important}
.item[data-conf="3"] span{color:var(--accent-2)!important}
#menu{display:none}
.nav-backdrop{display:none}
.navopen .nav-backdrop{display:block;position:fixed;inset:0;background:rgba(0,0,0,.35);z-index:45}
.navopen nav{transform:translateX(0)}
.bar,.stat,.tool-row{display:none}
[hidden]{display:none!important}
.skip{position:absolute;left:-99rem;top:.5rem;z-index:99;background:var(--ink);color:var(--surface);padding:.5rem .8rem}
.skip:focus{left:.5rem}
.dprog{display:block;margin-top:.6rem;font-size:.68rem;color:var(--muted)}
.dprog i{display:block;height:2px;background:var(--border);margin-bottom:.3rem;border-radius:1px;position:relative}
.dprog i::after{content:'';position:absolute;left:0;top:0;height:100%;width:var(--p,0%);background:var(--domain,var(--accent));border-radius:1px}
@media(max-width:1050px){.shell{grid-template-columns:240px minmax(0,1fr)}.domain-grid{grid-template-columns:repeat(2,1fr)}.track-grid{grid-template-columns:repeat(2,1fr)}main{padding:1.5rem 1.75rem 3rem}.metrics{grid-template-columns:repeat(2,1fr)}}
@media(max-width:860px){#menu{display:inline-flex}.shell{display:block}nav{position:fixed;inset:0 auto 0 0;width:min(320px,85vw);height:100%;border-radius:0;border-right:1px solid var(--border);transform:translateX(-105%);transition:transform .2s ease;z-index:50;box-shadow:0 2px 24px rgba(0,0,0,.18)}.navopen nav{transform:translateX(0)}main{padding:1.25rem 1rem 3rem}.atlas-hero{grid-template-columns:1fr;gap:1.5rem}.sp-grid{grid-template-columns:1fr}.domain-grid{grid-template-columns:repeat(2,1fr)}.schedule-grid,.track-grid,.routine-grid{grid-template-columns:1fr}.routine-wide{grid-column:auto}.main-links{display:none}}
@media(max-width:540px){.metrics{grid-template-columns:1fr 1fr}.domain-grid{grid-template-columns:1fr}.planner{flex-direction:column;align-items:flex-start}.practice-controls .btn{flex:1;justify-content:center}}
@media print{.top,nav,.study-hub,.nav-backdrop,.topic-tools,.drill-btn,.sprint,.domain-section,[id="dashboard"]{display:none!important}.shell{display:block}main{padding:0;max-width:none}.chap{break-inside:avoid;border:1px solid #ccc!important;border-left:3px solid var(--pc,#666)!important;box-shadow:none!important;margin-bottom:1rem!important}.chap:not([open])>.cb{display:block}.pt{break-after:avoid}body{background:#fff;color:#000;font-size:10pt}.tier.t1{background:#ffd}.item.done span{text-decoration:none;color:#999}}
@media(prefers-reduced-motion:reduce){*,nav{transition:none!important}html{scroll-behavior:auto}}
</style>"""

ENHANCEMENT_JS = """<script id="enh-v2">
(function(){
var T={
"A1":{ctx:"IOs test whether you understand force structure beyond just counting regiments — they look for command hierarchy awareness, modern reforms, and theatre command implications.",leads:["Research the Integrated Theatre Commands proposal: Army's role under proposed land theatre structure","Trace how Indian Army regimental system differs from corps-based Western armies — pros/cons under IO scrutiny","Study Agniveer scheme: its impact on regimental ethos, short-service tenure trade-offs, operational readiness debate","Examine how defence budget allocates between capital and revenue heads — what it means for Army modernisation pace","Explore Mountain Strike Corps (XVII Corps): raising status, Himalayan logistics constraints, China deterrence logic"]},
"A2":{ctx:"IOs probe tactical understanding — not just what infantry does, but how modern infantry fights: night combat, counter-insurgency transitions, and light vs mechanised trade-offs.",leads:["Study FICV (Future Infantry Combat Vehicle) programme: delay reasons, operational requirement vs DRDO capability gap","Research Rashtriya Rifles: dual-role (CI/conventional) doctrine and its strain on Army manpower","Examine Ghatak Platoons: role in special forces spectrum, operational use in surgical strikes narrative","Explore infantry rifle replacement debate: AK-203 Korwa factory, Make-in-India compliance, quantity vs quality","Study how sub-conventional warfare (J&K, NE) shapes infantry training priorities differently from conventional doctrine"]},
"A3":{ctx:"IOs expect you to link armour capability to terrain — Himalayan limitations, plains blitzkrieg doctrine, and future battlefield relevance amid drone dominance.",leads:["Research Zorawar light tank programme: high-altitude armour gap post-Galwan, development timeline and specs","Study T-90 Bhishma vs Arjun MBT: operational preference reasons, logistics, and indigenisation debate","Examine FINSAS (Future Infantry Soldier As a System): integration with armoured formations","Trace how drone warfare (Ukraine lessons) is reshaping armour doctrine — active protection systems, decoy use","Explore Mechanised Infantry vs Armoured Corps command debate in joint operations planning"]},
"A4":{ctx:"IOs check whether you understand artillery as a system — not just guns but ISR, targeting, and strategic coercion linkages.",leads:["Study Dhanush howitzer: its development from Bofors, production delays, field trials and induction status","Research Pinaka MRLS: multi-calibre evolution, export potential, and role in integrated fire support","Examine counter-battery radar (Swathi, Arthur): how they enable precision artillery response","Trace artillery modernisation gaps: ageing Bofors inventory, shell production shortfalls, import dependency","Explore loitering munitions (Nagastra-1): how they blur the line between artillery and air power"]},
"A5":{ctx:"IOs look for understanding of layered air defence — not just systems but integration, IAF-Army coordination, and threats from adversary air and missile power.",leads:["Study SHORAD gap: how man-portable and short-range systems integrate with Akash and S-400 layers","Research Project Kusha (Indian LRSAM): its significance for strategic air defence independence","Examine anti-drone systems: DRDO's Counter-UAS portfolio, C-UAS doctrine gaps exposed by Jammu drone attacks","Trace S-400 Triumf delivery status: US CAATSA threat, India's strategic autonomy argument, operational integration","Explore air defence in Himalayan terrain: radar coverage gaps, altitude limitations, Aksai Chin monitoring"]},
"A6":{ctx:"IOs test understanding of support arms as force multipliers — especially bridging, signals, and logistics in a two-front scenario.",leads:["Study Army's logistics modernisation: Base Workshop system, Integrated Logistics Nodes concept","Research military engineering role in Galwan context: Darbuk-Shyok-DBO road, BRO expansion mandate","Examine Corps of Signals: satellite dependence vs battlefield communication survivability","Trace Army Aviation Corps: role of Dhruv ALH, Rudra attack helicopter in mountain warfare","Explore NBC (Nuclear Biological Chemical) defence preparedness: doctrine, detection, decontamination capacity"]},
"A7":{ctx:"This is the highest IO-pressure topic — expect detailed questions on 1962 failure, 1971 civil-military coordination, and Kargil intelligence failure.",leads:["Study Henderson Brooks Report: why it remains classified, what leaked portions reveal about 1962 planning failures","Research Operation Vijay (Kargil): 527 KIA, tactical surprise, air power authorisation debate, Nawaz Sharif account","Examine 1971 war: Eastern Command's planning under Manekshaw, Mukti Bahini integration, surrender ceremony significance","Trace Operation Bluestar: Army's constitutional dilemma, lessons for civil-military relations","Explore Siachen conflict: Meghdoot 1984, logistics cost (\u20b910 crore/day), diplomatic settlement obstacles"]},
"A8":{ctx:"IOs probe whether you understand doctrine as a living document — Cold Start debate, two-front planning, and escalation management.",leads:["Study Cold Start Doctrine: official denial vs operational reality, Pakistan's tactical nuclear response (TNWs)","Research Integrated Battle Groups (IBGs): reorganisation rationale, challenges of maintaining operational cohesion","Examine two-front war planning: how Army allocates strike corps between western and northern fronts","Trace sub-conventional doctrine: Army's Counter Insurgency and Jungle Warfare School (CIJWS) curriculum","Explore information warfare doctrine: Army's cyber and EW integration with kinetic operations"]},
"A9":{ctx:"IOs test historical pattern recognition — they want to see if you draw lessons, not just list events.",leads:["Study Op Pawan (IPKF): mission creep lessons, ROE failures, strategic overreach in Sri Lanka","Research Op Meghdoot (Siachen): intelligence-based pre-emption, highest battlefield operational logistics","Examine Op Cactus (Maldives): rapid deployment lessons for India's HADR-to-combat spectrum","Trace Op Rakshak: how Rashtriya Rifles were raised as dedicated CI force from operational necessity","Explore Op Parakram (2001-02): coercive diplomacy lessons, mobilisation cost, diplomatic outcomes"]},
"A10":{ctx:"IOs look for forward thinking — autonomous systems, AI-enabled C2, and hypersonic threats.",leads:["Research AI in military decision-making: MoD's AI roadmap, Defence AI Council, ethical red lines","Study autonomous UGVs: DRDO's MUNTRA programme, counter-mine and surveillance variants","Examine hypersonic glide vehicles: BrahMos-II development, adversary hypersonic capability (DF-17, Kinzhal)","Trace electronic warfare modernisation: Army's SAMYUKTA EW system, spectrum dominance concept","Explore multi-domain operations concept: how Army is integrating space, cyber, and EW into land warfare"],},
"N1":{ctx:"IOs test whether you understand naval strategy beyond ships — SLOC protection, Quad maritime coordination, and IOR power politics.",leads:["Study India's Maritime Security Strategy 2015 (Ensuring Secure Seas): its three concentric circles concept","Research IOR choke points: Strait of Hormuz, Malacca, Bab-el-Mandeb — India's dependency and patrol posture","Examine Project 75-I submarine programme: AIP technology requirement, L&T-TKMS collaboration status","Trace Mission-Based Deployment (MBD): how Navy pre-positions ships across IOR for rapid response","Explore Quad maritime exercises (Malabar): interoperability goals, China's reaction, anti-submarine focus"]},
"N2":{ctx:"IOs probe surface fleet strategy — aircraft carrier doctrine, destroyer escort logic, and shipbuilding indigenisation.",leads:["Study INS Vikrant (IAC-1): significance as first indigenously built carrier, air wing composition (MiG-29K/TEJAS-N)","Research Project 15B destroyers (Visakhapatnam class): stealth features, weapons fit, delivery timeline","Examine Corvette gap: Kamorta-class limitations vs need for more ASW platforms in IOR","Trace Project 17A frigates (Nilgiri class): modular construction, delayed delivery, sensor suite","Explore carrier battle group (CBG) operations: escort doctrine, anti-ship missile defence layering"]},
"N3":{ctx:"IOs expect understanding of undersea warfare as India's strategic deterrent backbone and ASW challenge.",leads:["Study INS Arihant class: SSBN vs SSN distinction, K-15 Sagarika/K-4 missile range, second-strike credibility","Research Project 75 (Scorpene submarines): air-independent propulsion retrofit plans, operational status","Examine Chinese PLAN submarine activity in IOR: frequency, entry patterns, India's detection challenges","Trace anti-submarine warfare: P-8I Poseidon's role, LRASM integration, sonar buoy network","Explore undersea domain awareness: seabed sensors, SOSUS-equivalent Indian network concept, QUAD cooperation"]},
"N4":{ctx:"IOs check if you understand naval aviation as a force multiplier — not just carrier aircraft but maritime patrol, ASW helicopters, and UAVs.",leads:["Study MQ-9B Sea Guardian acquisition: significance for maritime domain awareness, LEMOA enabling factor","Research TEJAS Naval variant: arrested landing trials, ski-jump to catapult transition, IOC timeline","Examine P-8I Poseidon: multi-mission capability (ASW, ISR, anti-surface), Indian Ocean patrol patterns","Trace Kamov Ka-31 AEW helicopter: fleet air defence limitation, replacement need","Explore MH-60R Seahawk: ASW and SAR role in carrier battle group, US interoperability"]},
"N5":{ctx:"IOs look for weapons system integration understanding — not just BrahMos but layered naval strike capability.",leads:["Study BrahMos-A (air-launched): SU-30MKI integration, range extension to 450km, hypersonic BrahMos-II","Research Varunastra heavyweight torpedo: indigenous development, anti-submarine role, export interest","Examine MRSAM (Barak-8) naval variant: fleet air defence layering with Point Defence systems","Trace anti-ship missile gap: Exocet replacement, INS Kolkata class Harpoon vs newer threats","Explore Mine warfare: India's mine inventory, minelaying doctrine, Strait of Malacca contingency"]},
"N6":{ctx:"IOs test knowledge of unconventional naval capability — MARCOS, Sagarika missile submarines, and information warfare.",leads:["Study MARCOS (Marine Commandos): selection, training, operational roles (CT, hostage rescue, underwater demolition)","Research Naval Information Warfare: SIGINT ships, electromagnetic spectrum dominance","Examine HADR missions: Operation Rahat (Yemen), Operation Madad (Kerala floods), Navy's soft power role","Trace Naval diplomacy: SIMBEX, JIMEX, RIMPAC participation — India's multilateral naval engagement","Explore white-hull vs grey-hull debate: Coast Guard vs Navy jurisdictional boundaries in EEZ"]},
"N7":{ctx:"IOs probe operational history to test lessons-learned mindset — INS Khukri sinking, Op Talwar coercive deterrence.",leads:["Study Operation Talwar (1999): carrier positioning during Kargil, coercive effect on Pakistan Navy","Research INS Khukri sinking (1971): anti-submarine failure lessons, torpedo vulnerability of frigates","Examine Operation Leech (1998): counter-insurgency naval operation in Andamans, interagency coordination","Trace HADR: Tsunami 2004 response — Navy's first large HADR op, lessons for future deployment","Explore Operation Cactus (Maldives): rapid naval response, amphibious readiness demonstration"]},
"N8":{ctx:"IOs expect strategic thinking — IOR power competition, island territory significance, QUAD maritime security architecture.",leads:["Study China's String of Pearls: Hambantota, Gwadar, Djibouti — India's counter-access strategy","Research A&N (Andaman & Nicobar) Command: joint command structure, strategic location astride Malacca, underinvestment","Examine Indian Ocean Naval Symposium (IONS): India's maritime leadership framework","Trace IORA (Indian Ocean Rim Association) vs IONS: diplomatic vs operational maritime engagement","Explore seapower theory application: Mahan vs Corbett — which better describes Indian naval strategy?"]},
"N9":{ctx:"IOs check indigenisation awareness — P75-I, warship construction capacity, and strategic dependency reduction.",leads:["Study Mazagon Docks: warship construction backlog, submarine building capacity, private sector entry","Research GRSE (Garden Reach): landing craft, survey vessel, frigate building — export success (Bangladesh, Sri Lanka)","Examine Cochin Shipyard: IAC-1 significance, dry dock expansion, future carrier plans (IAC-2)","Trace DRDO naval projects: Varunastra, MRSAM, torpedo decoy systems — delivery record","Explore private sector entry: L&T shipbuilding, Pipavav, Reliance Defence — policy barriers and progress"]},
"F1":{ctx:"IOs test whether you understand IAF's force structure rationally — squadron strength, threat assessment, modernisation sequencing.",leads:["Study IAF's 42-squadron requirement vs current ~31 squadrons: fighter gap implications for two-front war","Research MRFA (108 fighters): why tender is stalled, Rafale vs F-35 vs F/A-18 political considerations","Examine Su-30MKI as backbone: upgrade roadmap (BrahMos integration, AESA radar, avionics refresh)","Trace MiG-21 phase-out timeline: replacement gap, Tejas Mk1A delivery delays from HAL","Explore AMCA (Advanced Medium Combat Aircraft): 5th gen features, DRDO-ADA design, IOC target year"]},
"F2":{ctx:"IOs probe fighter capability in terms of real combat performance — Balakot, BVR missile effectiveness, and electronic warfare.",leads:["Study Balakot air strike (2019): legal basis under Article 51 (anticipatory self-defence), Rafale's role in DEAD","Research BVR combat: Meteor missile (Rafale), why lock-on before launch changes engagement dynamics","Examine Tejas Mk1A: AESA radar (EL/M-2052), DRDO electronic warfare suite, 83-aircraft order status","Trace IAF's SEAD capability: suppression of enemy air defences — Mirage 2000 role, anti-radiation missile need","Explore stealth vs standoff: why India's current force is standoff-heavy and what 5th-gen changes"]},
"F3":{ctx:"IOs test multi-role understanding — airlift, VVIP transport, force projection beyond combat.",leads:["Study C-17 Globemaster III: strategic airlift for Ladakh logistics, Siachen supply, HADR (Nepal earthquake)","Research C-130J Super Hercules: special operations support, HALO/HAHO insertion, austere field ops","Examine Il-76 fleet ageing: replacement need, Antonov options, MTA (Medium Transport Aircraft) programme","Trace AN-32 upgrade: Ukrainian engine replacement, IAF's Russia dependency tension","Explore airborne refuelling: IL-78MKI tanker fleet — importance for long-range maritime patrol, Rafale range extension"]},
"F4":{ctx:"IOs look for understanding of IAF's support enablers — AEW&C, SIGINT, strategic ISR.",leads:["Study Phalcon AWACS: Israeli-Indian-Russian deal, force multiplier effect, 2 of 3 needed in theatre","Research NETRA AEW&C: Embraer-based Indian system, range limitations vs Phalcon, delivery status","Examine SIGINT aircraft: Boeing 737 BBJ conversion, strategic intelligence gathering role","Trace UAV fleet: Heron, Rustom-2, Tapas — surveillance role over Ladakh and LoC","Explore satellite-ISR: RISAT-2B SAR satellite, Cartosat, GSAT-7A — how IAF integrates space-based ISR"]},
"F5":{ctx:"IOs expect layered air defence understanding — from point defence to area denial to strategic deterrence.",leads:["Study S-400 Triumf: 400km range, multi-target engagement, A2/AD bubble over Delhi-NCR and Ladakh","Research Project Kusha (LRSAM): DRDO's domestic equivalent to Patriot, development phase","Examine Akash missile system: Mk1 vs Mk1S, export sales (Armenia), production ramp-up","Trace SPYDER (Israeli SHORAD): rapid reaction role, integration with IAF air defence network","Explore anti-ballistic missile defence: Prithvi Defence Vehicle (PDV) — exo-atmospheric intercept test"]},
"F6":{ctx:"IOs check precision strike capability depth — not just weapons but ISR-strike integration.",leads:["Study Crystal Maze-2 standoff bomb: 100km range, used in Balakot — GPS/INS guidance, Israeli origin","Research SPICE-2000: IAF's primary PGM, 60km range, scene-matching terminal guidance, operational record","Examine BrahMos air-launch (SU-30MKI): 300km reach, Mach 3 terminal, anti-ship and land-attack modes","Trace Astra BVR missile: Mk1 operational, Mk2 development, ramjet propulsion goal, IAF's indigenisation priority","Explore Rudram anti-radiation missile: DRDO-developed, SEAD role, passive homing on radar emissions"]},
"F7":{ctx:"IOs test operational campaign thinking — Balakot was IAF's first cross-border strike since 1971.",leads:["Study Balakot strike detail: target selection, timing, route, response management next 24 hours","Research Operation Safed Sagar (Kargil): CAS limitations at high altitude, Mig-27 accuracy, Mirage 2000 precision","Examine Operation Meghdoot air supply: highest maintained airlift — logistics over Siachen glacier","Trace air power in 1971: IAF's role in blinding PakAF radars, ground support in East Pakistan","Explore no-fly zone enforcement: IAF's SRINAGAR air defence readiness posture"]},
"F8":{ctx:"IOs probe doctrinal thinking — IAF's shift from defensive to offensive airpower, joint doctrine with Army and Navy.",leads:["Study IAF's Doctrine Document 2012 and updates: air superiority, strategic attack, information warfare pillars","Research joint air-land operations: Air Support Coordination, TACP (Tactical Air Control Party) effectiveness","Examine anti-access/area-denial (A2/AD): IAF's response to PLAN air build-up in Tibet — dispersal airfield use","Trace fifth-generation warfare integration: how IAF plans to operate in cognitive and electromagnetic spectrum","Explore escalation management: IAF's protocols for surgical strike — avoiding escalation spiral"]},
"F9":{ctx:"IOs check Make-in-India awareness — HAL production record, private aerospace entry, and strategic import dependency.",leads:["Study HAL's production challenges: Tejas Mk1A delivery slippage, Dhruv quality issues, workforce constraints","Research Hindustan Aeronautics Limited vs private sector: TATA Advanced Systems, L&T — MRO, components","Examine AMCA programme: DRDO ADA design, GE-414 engine licensing, timeline vs operational need","Trace indigenisation roadmap: LCA Tejas, Dhruv, IMRH (Indian Multi-Role Helicopter) — make-in-India defence target","Explore aerospace exports: Tejas to Malaysia (stalled), Dornier DO-228 export, HTFE-25 engine market"],},
"J1":{ctx:"IOs expect you to understand jointness not as a buzzword but as a real operational challenge — command, doctrine, communication.",leads:["Study Theaterisation proposals: five theatre commands plan, Army-Navy-IAF turf battles delaying implementation","Research Chief of Defence Staff (CDS): Gen Bipin Rawat's legacy, vacancy after crash, role evolution","Examine Department of Military Affairs (DMA): created under CDS, what it handles vs Ministry of Defence","Trace Integrated Defence Staff (IDS): paper jointness vs real integration — what has changed since 2001","Explore joint logistics: Integrated Logistics Nodes concept, common depots, reducing service duplication"]},
"J2":{ctx:"IOs probe nuclear doctrine deeply — No First Use credibility, tactical nuclear response, and second-strike survivability.",leads:["Study India's No First Use doctrine: NFU credibility debate after Rajnath Singh statement, strategic ambiguity argument","Research Pakistan's battlefield TNW (Nasr/Hatf-IX): how it complicates India's Cold Start and NFU","Examine triad completeness: Agni-V MIRV status, Arihant second-strike, air delivery survivability","Trace nuclear command authority: PM as NCA chairman, role of CDS, information flow in crisis","Explore China's nuclear build-up: silo construction, DF-41 road-mobile, implications for India's deterrence"]},
"J3":{ctx:"IOs test space-cyber awareness as these are now war-fighting domains, not just support enablers.",leads:["Study ASAT test (Mission Shakti, 2019): L-1 orbit intercept, debris cloud controversy, diplomatic fallout","Research Defence Space Agency (DSA): role, current satellite protection mandate, offensive space capability gap","Examine DRDO's cyber warfare: NTRO (National Technical Research Organisation), CERT-In military interface","Trace China's ASAT and EW capability in Tibet: jamming Indian satellites, ground-based laser threats","Explore information warfare: deep-fake, psychological operations, enemy narrative control — IO strategy"]},
"J4":{ctx:"IOs check if you understand procurement as a strategic issue — Make-in-India vs operational urgency tension.",leads:["Study Defence Acquisition Procedure 2020: categories (Buy Indian, Make), Acceptance of Necessity, long timelines","Research emergency procurement powers: how Galwan 2020 fast-tracked orders worth \u20b920,000 crore","Examine DRDO reform: Technology Development Fund, iDEX (Innovations for Defence Excellence) startup ecosystem","Trace offset policy: 30% offset requirement history, compliance failures, impact on FDI in defence","Explore FDI cap increase to 74% automatic route: private sector investment vs technology control concerns"]},
"J5":{ctx:"IOs probe counter-insurgency deeply — AFSPA, human rights balance, and strategic communication.",leads:["Study AFSPA: legal provisions, Supreme Court scrutiny, Manipur extra-judicial killings, partial withdrawal implications","Research NE insurgency evolution: ULFA-I vs ULFA(ATF), NSCN factions, Naga peace accord status","Examine J&K counter-terrorism: Operation All Out, changed demographic, proxy war tactics post-370 abrogation","Trace LWE (Left Wing Extremism) decline: SAMADHAN strategy, NIA role, development-security nexus","Explore strategic communication: how government narratives contest insurgent propaganda in information space"]},
"J6":{ctx:"IOs expect understanding of civil-military relations as a constitutional, not just administrative, matter.",leads:["Study civil-military imbalance: IAS seniority over military officers, budget process civil dominance","Research Kargil Review Committee: 1999 recommendations, how many implemented, Naresh Chandra Task Force 2012","Examine veterans issues: OROP (One Rank One Pension) history, implementation gaps, ex-servicemen welfare","Trace CDS creation: significance, Rawat's death, vacancy gap, appointment of Gen Anil Chauhan","Explore military-media interface: operational security vs transparency, embedded journalism, PAO system"],},
"G1":{ctx:"IOs probe Pakistan beyond border incidents — internal fragility, Army-civil power balance, and nuclear risk.",leads:["Study Pakistan's civil-military equation: Army's role in economy (Fauji Foundation), political interference pattern","Research FATF grey-listing: how Pakistan's terror financing monitoring affects India-Pakistan dynamics","Examine PTI-Army split (2022-23): Imran Khan removal, street protests, military institutional autonomy challenge","Trace Balochistan insurgency: BLA, BRAS activity, CPEC security implications for Chinese workers","Explore Pakistan's economic crisis: IMF bailout cycle, default risk, impact on military spending and nuclear maintenance"]},
"G2":{ctx:"IOs test China threat understanding beyond LAC — technology competition, BRI strategic logic, Taiwan contingency.",leads:["Study Galwan 2020: what China gained/lost diplomatically, PLA Western Theatre Command response","Research BRI (Belt and Road): debt diplomacy critique vs genuine infrastructure gap argument — 60+ countries","Examine CPEC: Gwadar port military potential, Karakoram Highway vulnerability, India's objections","Trace PLA modernisation: Xi's CMC control, corruption purge, real vs paper warfighting capability","Explore Taiwan Strait: how a contingency there affects India — supply chains, US attention shift, South China Sea"]},
"G3":{ctx:"IOs check understanding of India-US relations as a complex strategic partnership, not an alliance.",leads:["Study Foundational Agreements: LEMOA, COMCASA, BECA — what each enables operationally","Research CAATSA tension: S-400 purchase, US waiver debate, strategic autonomy vs technology access trade-off","Examine Quad: not a formal alliance, what each member gains, China's characterisation as 'Asian NATO'","Trace defence technology deals: GE-414 engine, MQ-9B, Javelin — Make-in-India compliance","Explore 2+2 Dialogue: NSA + Defence Minister format, strategic signalling function vs transactional outcomes"]},
"G4":{ctx:"IOs probe Russia relationship deeply — it's under stress but structurally deep.",leads:["Study S-400 and India's Russia dependency: 60% of military equipment Russian-origin, spares vulnerability","Research India-Russia trade in rupee: post-Ukraine sanctions, oil imports surge, western pressure on India","Examine AK-203 Korwa factory: Indo-Russian JV, 100% Make-in-India rifle, delivery timeline","Trace BrahMos Corporation: template for joint development — India's rising share in programme","Explore Russia-China rapprochement: Vostok exercises, what it means for India's strategic calculations"]},
"G5":{ctx:"IOs test Indo-Pacific strategic thinking — ASEAN centrality, Quad, and India's Act East pivot.",leads:["Study Indo-Pacific concept: who coined it, US Free and Open Indo-Pacific vs India's inclusive version","Research ASEAN centrality: why India doesn't bypass ASEAN even in Quad context — regional legitimacy","Examine India-Vietnam defence: BrahMos sale, submarine training, counter-China alignment without formal alliance","Trace India-Japan: Logistics Support Agreement, joint manufacturing (US-2 aircraft), Malabar exercise","Explore AUKUS implications: nuclear submarine transfer to Australia — IOR balance shift, India's reaction"]},
"G6":{ctx:"IOs test real-time conflict awareness — expect questions on current hot spots.",leads:["Study Russia-Ukraine war: drone warfare lessons, artillery importance resurgence, Western weapons supply chain","Research Israel-Gaza conflict: urban warfare, hostage dynamics, international humanitarian law debates","Examine Red Sea crisis: Houthi anti-ship missile attacks, US-UK strikes, Indian Navy escort missions","Trace Sudan civil war: RSF vs SAF — India's evacuation (Op Kaveri), African Union response failure","Explore Taiwan strait tension: PLA air incursions, US arms sales, India's silent observer position"]},
"G7":{ctx:"IOs check Afghanistan awareness — it directly connects to Pakistan, terrorism export, and India's regional strategy.",leads:["Study Taliban 2.0 governance: IS-K vs Taliban conflict, women's rights regression, international recognition","Research India-Taliban engagement: reopened Kabul embassy, wheat shipments — pragmatic vs principled tension","Examine Durand Line: Taliban refusal to recognise, Pakistan-Taliban border clashes, strategic implications","Trace IS-K (ISKP): Khorasan Province — attacks in Pakistan, Iran, Russia — India's concern","Explore SCO-Afghanistan linkage: how India uses SCO to maintain Afghanistan engagement without bilateral recognition"]},
"G8":{ctx:"IOs test breadth — ability to connect multiple conflict zones to India's interests.",leads:["Study Myanmar coup: Chin State proximity to Mizoram, India's tightrope walk, infrastructure projects at risk","Research Ethiopia-Eritrea: Horn of Africa stability, India's Red Sea interest, humanitarian implications","Examine Yemen civil war: Iran-Saudi proxy, Houthi evolution, India's large diaspora (NRIs) risk","Trace Sahel coups (Niger, Mali, Burkina Faso): French exit, Russian Wagner entry — India's Africa policy","Explore Korean Peninsula: North Korea ICBM tests, Japan-South Korea-US trilateral — India's Korean peninsula interests"]},
"G9":{ctx:"IOs test cross-cutting analytical thinking — single events that touch multiple domains.",leads:["Study climate-security nexus: IPCC reports, glacial melt and Himalayan water security, climate migration","Research AI arms race: autonomous lethal systems debate, UN CCW talks, India's position on LAWS","Examine pandemic-security interface: COVID-19 exposing supply chain vulnerabilities, medical stockpile strategy","Trace demographic security: youth bulge in conflict zones, radicalisation pipeline in Pakistan, India's dividend","Explore energy security: India's 85% oil import dependence, strategic petroleum reserves, refinery location strategy"]},
"G10":{ctx:"IOs test Geneva Convention awareness — especially in context of surgical strikes, hybrid warfare, and POW handling.",leads:["Study Laws of Armed Conflict (LOAC): distinction, proportionality, precaution — application to Balakot","Research Geneva Conventions: Common Article 3, POW treatment, India's record — Hague vs Geneva distinction","Examine cyber warfare legal framework: Tallinn Manual 2.0, state attribution problem, India's position","Trace international humanitarian law in COIN: AFSPA as derogation mechanism, compliance monitoring","Explore R2P (Responsibility to Protect): India's consistent non-interventionist stance, Bangladesh 1971 exception"],},
"P1":{ctx:"IOs test neighbourhood policy beyond SAARC — why India struggles to convert geographic advantage into strategic dominance.",leads:["Study SAARC vs BIMSTEC: why India effectively shifted bet — Pakistan spoiler role, BIMSTEC connectivity projects","Research Neighbourhood First Policy: Modi's 2014 inauguration signal, achievements vs limitations 10 years on","Examine connectivity diplomacy: Bangladesh-Bhutan-India-Nepal (BBIN) corridor, power grid interconnection","Trace diaspora as leverage: Indian diaspora in Nepal, Sri Lanka, Fiji — foreign policy tool or liability?","Explore China's neighbourhood inroads: Hambantota, Kyaukphyu port, Nepal hydro projects — India's counter moves"]},
"P2":{ctx:"IOs test depth of major power understanding — not headlines but structural relationships.",leads:["Study India-US defence technology: iCET (Initiative on Critical and Emerging Technology) — semiconductor, AI, quantum","Research India-France: Rafale negotiation lessons, OSIAN satellite, Scorpene submarine technology transfer depth","Examine India-Israel: Phalcon, Heron, Iron Dome interest, Spike ATGM — strategic tech dependency","Trace India-Japan: Official Security Assistance (OSA), 2+2 dialogue, FOIP convergence","Explore India-Australia: Mutual Logistics Support Agreement, AUSINDEX exercise, uranium supply"]},
"P3":{ctx:"IOs probe geopolitics beyond military — economic coercion, information operations, and diplomatic isolation attempts.",leads:["Study China's grey-zone tactics: Bhutan boundary claims, Nepal map issue, Maldives pro-China tilt","Research Pakistan's diplomatic offensive: Kashmir internationalisation at UNGA, OIC mobilisation","Examine India's counter-strategy: bilateral border talks with Bhutan, development aid to Maldives, Colombo port partnership","Trace Turkey-Pakistan nexus: Bayraktar TB2 drone supply to Pakistan, Erdogan's Kashmir rhetoric","Explore Saudi-Iran normalisation (2023 Chinese mediated): implications for India's West Asia balancing act"]},
"P4":{ctx:"IOs check economic-security linkage — defence exports, Atma Nirbhar targets, and strategic import dependencies.",leads:["Study \u20b925,000 crore defence export target by 2025: current status (~\u20b921,083 crore in FY24), top buyers","Research critical mineral dependency: QUAD Critical Minerals partnership, Australia uranium, lithium for batteries","Examine rare earth dependency on China: 90% global processing in China — India's alternative strategy","Trace defence FDI: 74% automatic route, \u20b98,500 crore FDI received, what sectors attract investment","Explore Make-in-India defence: iDEX startups, positive indigenisation list (PAL) — 300+ items reserved"]},
"P5":{ctx:"IOs test multilateral thinking — UN reform, SCO membership, BRICS expansion.",leads:["Study India's UNSC permanent membership bid: G4, China veto, reform roadmap at 2024 Summit of Future","Research SCO membership: India-Pakistan both inside — terrorism definition disagreement, counter-narcotics","Examine BRICS expansion: Iran, Saudi, UAE, Ethiopia joining — dilution vs consolidation debate","Trace G20 India presidency (2023): key outcomes, Global South voice amplification, Ukraine war disagreement","Explore Non-Aligned Movement vs Strategic Autonomy: how India explains its position to allies"],},
"T1":{ctx:"IOs expect you to explain emerging warfare without jargon — drones, information ops, hybrid tactics.",leads:["Study drone warfare: Nagorno-Karabakh 2020 as case study — cheap UAS defeating expensive armour","Research electronic warfare: GPS jamming over Baltic states, India's EW modernisation programme","Examine information operations: Russia's dezinformatsiya, China's United Front Work — India as target","Trace autonomous weapons debate: lethal autonomous weapon systems (LAWS), UN Group of Governmental Experts","Explore grey-zone operations: actions below armed conflict threshold — how China uses it in South China Sea"]},
"T2":{ctx:"IOs check if you can explain technology without being tech-heavy — focus on strategic implications.",leads:["Study hypersonic weapons: glide vehicles vs scramjet, detection challenge for existing missile defence","Research AI in warfare: target recognition, autonomous navigation, logistics optimisation — dual-use risks","Examine quantum sensing for military: gravity sensors for submarine detection, secure quantum communication","Trace directed energy weapons: DRDO DURGA laser, counter-UAS application, power requirement constraints","Explore 6G military application: low-latency mesh networks, battlefield communication, C2 node resilience"]},
"T3":{ctx:"IOs test indigenisation understanding as a strategic rather than just economic issue.",leads:["Study positive indigenisation list (PAL): 300+ items reserved, strategic logic vs industry capacity gap","Research DRDO reform: Technology Development Fund, Acing Development of Innovative Technologies with iDEX","Examine critical technology gaps: jet engine, gas turbine, advanced semiconductor — why India cannot indigenise yet","Trace joint ventures: Boeing India (F/A-18 wing), Lockheed-TATA (F-16 fuselage), Airbus India (C295)","Explore private sector growth: TATA, Mahindra, L&T, Bharat Forge — from ancillary to prime contractor"],},
"CA1":{ctx:"IOs test current affairs application to defence — not just what happened but its strategic implications for India.",leads:["Study Modi 3.0 defence priorities: budget allocation trend, theatre command progress, diplomatic outcomes","Research India's \u20b96.21 lakh crore defence budget (FY25): capital vs revenue ratio, pension burden","Examine defence industrial corridor: UP corridor (Lucknow-Agra) and Tamil Nadu corridor — investment status","Trace IPOI (Indo-Pacific Oceans Initiative): India's seven pillars, comparison with US FOIP","Explore India's vote patterns at UNSC: Ukraine war abstentions — strategic autonomy or strategic ambiguity?"],},
"Q1":{ctx:"IOs probe your self-awareness — why you, why Army/Navy/IAF, what have you done that shows officer potential.",leads:["Research OLQ framework: 15 officer-like qualities — which three do you genuinely demonstrate with specific examples?","Study GTO tasks: Group Discussion, Group Planning Exercise, Lecturette — what subjects can you speak on for 3 minutes?","Examine PIQ (Personal Information Questionnaire): how to frame each answer as evidence of OLQs","Trace your educational choices: how do they align with the service you've opted for?","Explore current affairs bridge: pick 3 current defence events you can speak on for 3 minutes each with a view"]},
"Q2":{ctx:"IOs look for consistency between your PIQ and verbal answers — any gap raises flags.",leads:["Study PIQ preparation: family background, hobbies, NCC/Sports — have specific numbers, dates, achievements","Research your state's contribution to defence: regiment, famous alumni, battle honours","Examine extracurricular analysis: leadership roles held — President/Captain/Head, not just participant","Trace failure-and-learning narratives: prepare 2 genuine failures and what you learned — IOs value self-awareness","Explore service-specific motivation: Army (team leadership), Navy (technology + sea), IAF (aviation + precision)"]},
"Q3":{ctx:"IOs use SBQ to test problem-solving under ambiguity — there is no single right answer, consistency matters.",leads:["Study common SBQ scenarios: lost in jungle, team conflict, witnessing corruption, national emergency","Research decision frameworks: SWOT, OODA loop — apply structured thinking without sounding robotic","Examine group dynamics: how to lead without dominating, how to contribute without being passive","Trace ethical dilemma patterns: duty vs loyalty, personal cost vs institutional integrity","Explore current-affairs SBQ: be ready for 'If you were the Defence Minister, what would you do about...' questions"]},
"Q4":{ctx:"IOs test values consistency — your answers across GTO, interview, and psych tests should form a coherent value profile.",leads:["Study Indian Constitution: Fundamental Duties, Preamble values — how they link to military ethos","Research ethics of military force: when is use of force justified, proportionality in COIN operations","Examine corruption in defence: Bofors, Rafale controversy — form your own analytical (not political) view","Trace whistle-blower dilemmas: Col Purohit case, Sohrabuddin encounter — institutional loyalty vs rule of law","Explore social media and military: operational security, political opinion expression — where should officers draw the line?"]},
"Q5":{ctx:"IOs test social awareness — poverty, gender, caste, urban-rural divide — as a future officer interacts with soldiers from all backgrounds.",leads:["Study Indian social realities: OBC-SC-ST representation in armed forces, Hoshangabad Report insights","Research women in armed forces: Permanent Commission, NDA entry, combat role debate","Examine economic inequality: how poverty in recruitment catchment areas affects soldier quality","Trace farmer distress: Jawan-Kisan connection — most soldiers come from agricultural families","Explore social cohesion: how regimental system binds diverse India — Madras Regiment, Dogra Regiment, Kumaon Regiment"]},
"Q6":{ctx:"IOs test rapid fluency — expect 1-line answers, then 'why', then 'what should India do'.",leads:["Prepare rapid-fire: 50 defence acronyms (DRDO, ADA, DAP, AMCA, FICV, IBG, NCA, CDS, DMA, PAL)","Research operational code names: Op Vijay, Op Shakti, Op Talwar, Op Parakram, Op Rahat, Op Kaveri","Examine rank structure both Indian and adversary forces: PLA rank equivalent to Indian Army equivalents","Trace treaty literacy: NPT, CTBT, MTCR, Wassenaar, BECA, COMCASA, LEMOA — one-line each","Explore chiefs: current Chiefs of Army, Navy, IAF, CDS, NSA, Defence Minister, Defence Secretary"]
}
};

function makeCtx(id,d){
  var div=document.createElement('div');
  div.className='blk context';
  div.innerHTML='<h4>SSB Perspective</h4><p>'+d.ctx+'</p>';
  return div;
}

function makeLeads(id,d){
  var items='';
  d.leads.forEach(function(l,i){
    var k=id+'.enh'+(i+1);
    items+='<li class="item" data-k="'+k+'"><label><input type="checkbox" data-k="'+k+'"><span>\u2295 '+l+'</span></label></li>';
  });
  return items;
}

Object.keys(T).forEach(function(id){
  var el=document.getElementById(id);
  if(!el)return;
  var cb=el.querySelector('.cb');
  if(!cb)return;
  var writeBlk=cb.querySelector('.blk.write');
  var ctx=makeCtx(id,T[id]);
  if(writeBlk&&writeBlk.nextSibling){
    cb.insertBefore(ctx,writeBlk.nextSibling);
  } else {
    cb.insertBefore(ctx,cb.firstChild);
  }
  var leadsUl=cb.querySelector('.blk.leads ul');
  if(leadsUl){
    leadsUl.insertAdjacentHTML('beforeend',makeLeads(id,T[id]));
  }
});
})();
</script>"""

if "<style id=\"redesign-v2\">" not in html:
    html = html.replace("</head>", CSS + "\n</head>", 1)

if "<script id=\"enh-v2\">" not in html:
    html = html.replace("</body>", ENHANCEMENT_JS + "\n</body>", 1)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print("Done. Output written to", OUT)
print("File size:", len(html), "bytes")

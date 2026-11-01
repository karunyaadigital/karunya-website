const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 390, height: 844 }, isMobile:true, hasTouch:true });
const errs=[]; pg.on('pageerror',e=>errs.push(e.message));
for (const p of ['index.html','audit.html','404.html','about.html','services.html','work.html','contact.html','gynae.html','ivf.html','ortho.html','dental.html','blog.html','blog-social-media-agency-for-doctors.html','blog-google-business-profile-for-doctors.html']) {
 await pg.goto('http://localhost:8765/'+p); await pg.waitForTimeout(1500);
 const H = await pg.evaluate(()=>document.body.scrollHeight);
 for (let y=0;y<H;y+=500){ await pg.evaluate(y=>scrollTo(0,y),y); await pg.waitForTimeout(60); }
 const ow = await pg.evaluate(()=>{ const w=document.documentElement.clientWidth; return [...document.querySelectorAll('body *')].filter(e=>{const r=e.getBoundingClientRect(); return r.right>w+1 && getComputedStyle(e).position!=='fixed' && !e.closest('.reel-strip,.ticker,.f-marquee,.scene,.strip,.ghat,.f-scene,.og-bg,.tk-track,.lotus-wrap,.hero,.nav')}).slice(0,5).map(e=>e.className||e.tagName)});
 const sw = await pg.evaluate(()=>document.documentElement.scrollWidth);
 console.log(p, 'scrollWidth', sw, 'overflow', JSON.stringify(ow));
 if (p==='index.html'){ for (const [sel,n] of [['.bridge-sec','b'],['.originals','o'],['.site-footer','f']]) { await pg.$eval(sel,e=>e.scrollIntoView()); await pg.waitForTimeout(900); await pg.screenshot({path:`/tmp/cs/m-${n}.png`}); } }
 if (p==='about.html'){ await pg.$eval('.founder',e=>e.scrollIntoView()); await pg.waitForTimeout(800); await pg.screenshot({path:'/tmp/cs/m-a.png'}); }
}
console.log('errors', errs); await b.close(); })();

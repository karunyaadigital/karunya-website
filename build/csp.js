const { chromium } = require('playwright'); const fs=require('fs');
const csp = fs.readFileSync('/home/claude/site/_headers','utf8').match(/Content-Security-Policy: (.*)/)[1].replace(' upgrade-insecure-requests','');
(async()=>{ const b=await chromium.launch(); 
for (const p of ['index.html','audit.html','404.html','about.html','services.html','work.html','contact.html','gynae.html','ivf.html','ortho.html','dental.html','blog.html','blog-social-media-agency-for-doctors.html','blog-google-business-profile-for-doctors.html']) {
 const pg=await b.newPage(); const errs=[];
 pg.on('console',m=>{ if(/Content Security Policy|Refused/.test(m.text())) errs.push(m.text().slice(0,160)); });
 await pg.route('**/*', async r=>{ const res=await r.fetch(); const h={...res.headers()}; if(r.request().resourceType()==='document') h['content-security-policy']=csp; r.fulfill({response:res, headers:h}); });
 await pg.goto('http://localhost:8765/'+p,{waitUntil:'networkidle'}); await pg.evaluate(()=>window.scrollTo(0,3000)); await pg.waitForTimeout(1500);
 const js = await pg.evaluate(()=>document.documentElement.classList.contains('js'));
 console.log(p, 'jsClass', js, errs.length?errs:'no CSP errors'); await pg.close(); }
await b.close(); })();

const { chromium } = require('playwright');
(async () => { const b = await chromium.launch();
for (const [w,h,tag] of [[1440,900,'d'],[390,844,'m']]) {
 const pg = await b.newPage({ viewport: { width: w, height: h }, isMobile: w<600, hasTouch: w<600 });
 const errs=[]; pg.on('pageerror',e=>errs.push(e.message));
 let posted=null; await pg.route('**/', async r=>{ if(r.request().method()==='POST'){ posted=r.request().postData(); return r.fulfill({status:200,body:'ok'});} return r.continue(); });
 await pg.goto('http://localhost:8765/audit.html'); await pg.waitForTimeout(800);
 await pg.click('.a-go'); await pg.waitForTimeout(400);
 const err1 = await pg.textContent('.a-err');
 const qs = await pg.$$('.aq'); 
 for (let i=0;i<qs.length;i++){ const opts = await qs[i].$$('label'); await opts[Math.min(i%3, opts.length-1)].click(); }
 await pg.waitForTimeout(900);
 await pg.screenshot({path:`/tmp/cs/au-${tag}1.png`});
 await pg.click('.a-go'); await pg.waitForTimeout(1200);
 const score = await pg.textContent('[data-score]'); const fixes = await pg.$$eval('[data-fixes] li', l=>l.map(x=>x.querySelector('b').textContent));
 await pg.screenshot({path:`/tmp/cs/au-${tag}2.png`});
 await pg.fill('#l-name','Dr. Test'); await pg.fill('#l-phone','9876543210'); await pg.fill('#l-city','Varanasi');
 await pg.click('#lead button'); await pg.waitForTimeout(800);
 const done = await pg.isVisible('.l-done');
 console.log(tag, 'err1:', err1, '| score', score, '| fixes', fixes, '| posted', (posted||'').slice(0,160), '| done', done, '| errs', errs);
 await pg.close(); }
await b.close(); })();

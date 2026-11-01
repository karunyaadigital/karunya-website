const { chromium } = require('playwright');
(async () => { const b = await chromium.launch();
for (const [w,h,tag] of [[1440,900,'d'],[390,844,'m']]) {
 const pg = await b.newPage({ viewport: { width: w, height: h }, isMobile: w<600, hasTouch: w<600 });
 const errs=[]; pg.on('pageerror',e=>errs.push(e.message));
 const posts=[]; await pg.route('**/', async r=>{ if(r.request().method()==='POST'){ posts.push(r.request().postData()); return r.fulfill({status:200,body:'ok'});} return r.continue(); });
 await pg.goto('http://localhost:8765/audit.html'); await pg.waitForTimeout(1500);
 await pg.screenshot({path:`/tmp/cs/a2-${tag}0.png`});
 await pg.click('.s-go'); const e1 = await pg.textContent('.s-err');
 await pg.fill('#s-name','Dr. Test Sharma'); await pg.fill('#s-phone','98765 43210'); await pg.fill('#s-city','Meerut'); await pg.click('.s-go'); await pg.waitForTimeout(900);
 const qs = await pg.$$('.aq'); for (let i=0;i<qs.length;i++){ const o = await qs[i].$$('label'); await o[(i+1)%o.length].click(); }
 await pg.click('.a-go'); await pg.waitForTimeout(1400);
 await pg.screenshot({path:`/tmp/cs/a2-${tag}1.png`});
 console.log(tag, e1, '| posts', posts.length, posts.map(p=>p.match(/stage=\w+/)[0]), '| greet', await pg.textContent('[data-greet]'), '| errs', errs);
 await pg.close(); }
const pg = await b.newPage({ viewport: { width: 1440, height: 900 } }); await pg.goto('http://localhost:8765/404.html'); await pg.waitForTimeout(1500); await pg.mouse.move(700,500); await pg.mouse.move(760,560,{steps:10}); await pg.waitForTimeout(300); await pg.screenshot({path:'/tmp/cs/nf.png'});
await b.close(); })();

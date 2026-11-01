const { chromium } = require('playwright');
(async () => { const b = await chromium.launch();
for (const [w,h,t] of [[1440,900,'d'],[390,844,'m']]) { const pg = await b.newPage({ viewport:{width:w,height:h}, isMobile:w<600 });
 const errs=[]; pg.on('pageerror',e=>errs.push(e.message)); pg.on('console',m=>{if(/Refused|Content Security/.test(m.text()))errs.push(m.text().slice(0,100))});
 await pg.goto('http://localhost:8765/blog-nmc-new-guidelines-doctors-social-media.html'); await pg.waitForTimeout(1500);
 const H = await pg.evaluate(()=>document.body.scrollHeight); for (let y=0;y<H;y+=500){await pg.evaluate(y=>scrollTo(0,y),y); await pg.waitForTimeout(50);}
 await pg.evaluate(()=>scrollTo(0,0)); await pg.waitForTimeout(400);
 await pg.screenshot({path:`/tmp/cs/bp-${t}.png`, fullPage:true});
 await pg.goto('http://localhost:8765/blog.html'); await pg.waitForTimeout(1500); await pg.screenshot({path:`/tmp/cs/bi-${t}.png`});
 console.log(t, errs, await pg.evaluate(()=>document.documentElement.scrollWidth)); await pg.close(); }
await b.close(); })();

const { chromium } = require('playwright');
(async () => { const b = await chromium.launch();
const shots=[['index','.duo-sec',1440],['index','.profiles-sec',1440],['index','.site-footer',1440],['services','#pricing',1440],['about','.founder',1440],['index','.bridge-sec',390],['index','.duo-sec',390],['index','.site-footer',390]];
let i=0; for (const [p,sel,w] of shots) { const pg = await b.newPage({ viewport:{width:w,height:w<600?844:900}, isMobile:w<600 });
 await pg.goto(`http://localhost:8765/${p}.html`); await pg.waitForTimeout(700);
 await pg.$eval(sel, e=>e.scrollIntoView({block:'start'})); await pg.waitForTimeout(1600);
 await pg.screenshot({path:`/tmp/cs/sec${i++}.png`}); await pg.close(); }
await b.close(); })();

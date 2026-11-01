const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const pg = await b.newPage({ viewport:{width:1440,height:900} });
await pg.goto('http://localhost:8765/index.html'); await pg.waitForTimeout(800);
await pg.$eval('.stat-row', e=>e.scrollIntoView({block:'center'})); await pg.waitForTimeout(1500);
console.log(await pg.$eval('.stat-row', e=>JSON.stringify({h:e.offsetHeight, disp:getComputedStyle(e).display, op:getComputedStyle(e.children[0]).opacity})));
await pg.screenshot({path:'/tmp/cs/tot.png'}); await b.close(); })();

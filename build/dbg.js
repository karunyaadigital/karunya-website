const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 390, height: 844 } });
await pg.goto('http://localhost:8765/index.html'); await pg.waitForTimeout(3000);
console.log(await pg.$eval('.scene', e => JSON.stringify(e.getBoundingClientRect())), await pg.$eval('.hero', e => e.offsetHeight));
await pg.screenshot({path:'/tmp/cs/hm.png', clip:{x:0,y:0,width:390,height:1000}, fullPage:true}); await b.close(); })();

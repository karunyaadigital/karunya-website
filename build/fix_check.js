const { chromium } = require('playwright');
(async () => { const b = await chromium.launch();
let pg = await b.newPage({ viewport:{width:390,height:844}, isMobile:true, hasTouch:true });
await pg.goto('http://localhost:8765/index.html'); await pg.waitForTimeout(3000); await pg.screenshot({path:'/tmp/cs/fx1.png', fullPage:true, clip:{x:0,y:0,width:390,height:1200}});
pg = await b.newPage({ viewport:{width:1440,height:900} });
await pg.goto('http://localhost:8765/about.html'); await pg.waitForTimeout(800); await pg.$eval('.about-reel', e=>e.scrollIntoView({block:'center'})); await pg.waitForTimeout(900); await pg.screenshot({path:'/tmp/cs/fx2.png'});
await pg.goto('http://localhost:8765/gynae.html'); await pg.waitForTimeout(800); await pg.$eval('#sd-h', e=>e.scrollIntoView({block:'center'})); await pg.waitForTimeout(900); await pg.screenshot({path:'/tmp/cs/fx3.png'});
await b.close(); })();

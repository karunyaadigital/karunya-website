const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1440, height: 900 } });
await pg.goto('http://localhost:8765/index.html'); await pg.waitForTimeout(1000);
await pg.$eval('#faces-h', e=>e.scrollIntoView()); await pg.waitForTimeout(1200); await pg.evaluate(()=>scrollBy(0,-60)); await pg.waitForTimeout(400);
await pg.screenshot({path:'/tmp/cs/fc1.png', fullPage:false});
await pg.evaluate(()=>scrollBy(0,800)); await pg.waitForTimeout(500); await pg.screenshot({path:'/tmp/cs/fc2.png'});
await pg.goto('http://localhost:8765/gynae.html'); await pg.waitForTimeout(800); await pg.$eval('.docs', e=>e.scrollIntoView()); await pg.waitForTimeout(900); await pg.screenshot({path:'/tmp/cs/fc3.png'});
await b.close(); })();

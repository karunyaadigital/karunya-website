const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1440,height:900}});const errs=[];pg.on('pageerror',e=>errs.push(e.message));
await pg.goto('http://localhost:8765/index.html');await pg.waitForTimeout(800);
const el=await pg.$('.testi');await el.scrollIntoViewIfNeeded();await pg.waitForTimeout(1500);await el.screenshot({path:'/tmp/cs/testi.png'});
console.log(errs);await b.close();})();

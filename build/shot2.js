const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const w = +process.argv[2];
  const pg = await b.newPage({ viewport: { width: w, height: w<600?844:900 } });
  await pg.goto('http://localhost:8765/index.html', { waitUntil: 'networkidle' });
  await pg.waitForTimeout(3300);
  await pg.screenshot({ path: `/tmp/cs/h-${w}.png` });
  const ys = await pg.$$eval('[data-step]', els => els.map(e => e.getBoundingClientRect().top + scrollY + e.offsetHeight/2));
  for (let i=0;i<ys.length;i++){ await pg.evaluate(y=>scrollTo(0,y-innerHeight/2),ys[i]); await pg.waitForTimeout(1900); await pg.screenshot({ path: `/tmp/cs/st${i+1}-${w}.png` }); }
  await b.close();
})();

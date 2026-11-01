const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const pages = process.argv[2].split(',');
  const w = +process.argv[3] || 1440, h = w < 600 ? 844 : 900;
  for (const p of pages) {
    const pg = await b.newPage({ viewport: { width: w, height: h } });
    const errs = []; pg.on('pageerror', e => errs.push(e.message)); pg.on('console', m => m.type()==='error' && errs.push(m.text()));
    await pg.goto('http://localhost:8765/' + p, { waitUntil: 'networkidle' });
    await pg.waitForTimeout(3200);
    await pg.screenshot({ path: `/tmp/cs/s-${p}-${w}-top.png` });
    // scroll through to trigger observers
    const H = await pg.evaluate(() => document.body.scrollHeight);
    for (let y = 0; y < H; y += 400) { await pg.evaluate(y => window.scrollTo(0, y), y); await pg.waitForTimeout(120); }
    await pg.waitForTimeout(800);
    await pg.evaluate(() => window.scrollTo(0, 0));
    await pg.screenshot({ path: `/tmp/cs/s-${p}-${w}-full.png`, fullPage: true });
    console.log(p, w, 'height', H, errs.join(' | '));
    await pg.close();
  }
  await b.close();
})();

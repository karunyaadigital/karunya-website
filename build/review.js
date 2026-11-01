const { chromium } = require('playwright');
(async () => { const b = await chromium.launch();
const pages=['index','audit','services','work','about','contact','gynae','ivf','ortho','dental','404','blog','blog-social-media-agency-for-doctors'];
for (const [w,h,t] of [[1440,900,'d'],[390,844,'m']]) {
 for (const p of pages) {
  const pg = await b.newPage({ viewport:{width:w,height:h}, isMobile:w<600, hasTouch:w<600 });
  await pg.goto(`http://localhost:8765/${p}.html`); await pg.waitForTimeout(1200);
  const H = await pg.evaluate(()=>document.body.scrollHeight);
  for (let y=0;y<H;y+=400){ await pg.evaluate(y=>scrollTo(0,y),y); await pg.waitForTimeout(70); }
  await pg.waitForTimeout(900); await pg.evaluate(()=>scrollTo(0,0)); await pg.waitForTimeout(300);
  await pg.screenshot({path:`/tmp/cs/rv-${t}-${p}.png`, fullPage:true}); await pg.close();
 }}
await b.close(); })();

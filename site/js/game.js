/* Karunya Digital — "Doctor Saheb Famous Kaise Bane?" game */
(() => {

  const C = {blue:'#0251B0',navy:'#012A5E',lime:'#D1FF42',lb:'#B0E0E6',grey:'#C7D1DD',paper:'#F3F6FA',red:'#E0475B',white:'#fff'};
  const GOOD = [
    {e:'🎬',t:'Reel',pts:10,msg:'Reel viral! 🔥'},
    {e:'⭐',t:'5★ Review',pts:15,msg:'Asli review mila!'},
    {e:'📍',t:'GMB',pts:15,msg:'Google Maps pe top!'},
    {e:'🔍',t:'SEO',pts:10,msg:'Google pe #1!'},
    {e:'📢',t:'Meta Ad',pts:10,msg:'Leads aa rahi hain!'},
    {e:'💬',t:'WhatsApp',pts:10,msg:'Patient ne message kiya!'},
    {e:'🌐',t:'Website',pts:10,msg:'Trust badh gaya!'}
  ];
  const BAD = [
    {e:'🤥',t:'Fake Review',msg:'Fake review pakda gaya!',lesson:'Fake reviews se Google aapki GMB listing suspend kar sakta hai. Asli patients se review maango.'},
    {e:'🚫',t:'"100% Cure"',msg:'NMC guideline todi!',lesson:'"100% cure / guarantee" jaise claims NMC guidelines ke khilaaf hain. Awareness content banao, daave nahi.'},
    {e:'😴',t:'Inactive Page',msg:'Page so gaya…',lesson:'Mahino tak post na karna = patients aapko bhool jaate hain. Regular Reels zaroori hain.'},
    {e:'💸',t:'Random Boost',msg:'Paisa barbaad!',lesson:'Bina targeting ke "Boost Post" dabana = paisa barbaad. Sahi audience pe sahi ad chalao.'},
    {e:'🙈',t:'DM Ignore',msg:'Patient chala gaya!',lesson:'Patient ka DM ya comment ignore kiya, toh woh competitor ke paas chala jaata hai. Jaldi reply karo.'}
  ];
  const RANKS = [
    [0,'Naye Doctor Saheb'],[120,'Mohalle ke Famous'],[260,'Shehar ke Top Doctor'],
    [450,'UP ke Star Doctor'],[700,'India ke Famous Doctor']
  ];
  const GAME_TIME = 60;

  const wrap = document.getElementById('kg');
  if (!wrap) return;
  const cv = wrap.querySelector('canvas');
  const ctx = cv.getContext('2d');
  const $ = id => document.getElementById('kg-' + id);
  let W=0,H=0,DPR=1;

  function resize(){
    DPR = Math.min(window.devicePixelRatio||1, 2.5);
    W = wrap.clientWidth; H = wrap.clientHeight;
    cv.width = W*DPR; cv.height = H*DPR;
    ctx.setTransform(DPR,0,0,DPR,0,0);
    if (player) { player.y = H - 18; player.x = Math.min(Math.max(player.x, 50), W-50); }
  }

  // ---------- Sound ----------
  let actx=null, muted=false;
  try { muted = localStorage.getItem('kd_game_muted')==='1'; } catch(e){}
  $('mute').textContent = muted ? '🔇' : '🔊';
  function initAudio(){ try{ if(!actx) actx = new (window.AudioContext||window.webkitAudioContext)(); if(actx.state==='suspended') actx.resume(); }catch(e){} }
  function beep(freq,dur=0.08,type='sine',vol=0.15,slide=0){
    if(muted||!actx) return;
    try{
      const o=actx.createOscillator(), g=actx.createGain(), t=actx.currentTime;
      o.type=type; o.frequency.setValueAtTime(freq,t);
      if(slide) o.frequency.exponentialRampToValueAtTime(Math.max(40,freq+slide),t+dur);
      g.gain.setValueAtTime(vol,t); g.gain.exponentialRampToValueAtTime(0.001,t+dur);
      o.connect(g).connect(actx.destination); o.start(t); o.stop(t+dur+0.02);
    }catch(e){}
  }
  const sfx = {
    good(){ beep(660,.07,'triangle',.14); setTimeout(()=>beep(990,.09,'triangle',.12),55); },
    bad(){ beep(220,.25,'sawtooth',.10,-120); },
    gold(){ [523,659,784,1047].forEach((f,i)=>setTimeout(()=>beep(f,.1,'square',.07),i*70)); },
    shield(){ beep(400,.12,'sine',.12,300); },
    end(){ [784,659,523,392].forEach((f,i)=>setTimeout(()=>beep(f,.14,'triangle',.12),i*110)); }
  };
  $('mute').addEventListener('click', e => {
    e.stopPropagation(); muted=!muted; $('mute').textContent = muted?'🔇':'🔊';
    try{ localStorage.setItem('kd_game_muted', muted?'1':'0'); }catch(err){}
    if(!muted) initAudio();
  });

  // ---------- State ----------
  let player=null, items=[], floats=[], particles=[], state='menu';
  let score=0, lives=3, timeLeft=GAME_TIME, spawnT=0, last=0, boostT=0, shield=0, combo=0, hitFlash=0, shake=0;
  let caughtBad = new Set();
  let keys={left:false,right:false};
  let best=0; try{ best = +localStorage.getItem('kd_game_best')||0; }catch(e){}

  // background dots
  let dots=[];
  function makeDots(){ dots=[]; for(let i=0;i<40;i++) dots.push({x:Math.random(),y:Math.random(),r:Math.random()*1.8+0.6,s:Math.random()*0.02+0.01}); }

  function reset(){
    player = {x:W/2, tx:W/2, y:H-18, w:96, tilt:0};
    items=[]; floats=[]; particles=[]; caughtBad=new Set();
    score=0; lives=3; timeLeft=GAME_TIME; spawnT=0.4; boostT=0; shield=0; combo=0; hitFlash=0; shake=0;
    updateHUD();
  }

  function progress(){ return 1 - timeLeft/GAME_TIME; } // 0..1
  function spawn(){
    const p = progress();
    const r = Math.random();
    let kind, data;
    if (r < 0.045 && boostT<=0) { kind='gold'; data={e:'K',t:'Karunya Team'}; }
    else if (r < 0.045 + 0.28 + p*0.14) { kind='bad'; data=BAD[Math.floor(Math.random()*BAD.length)]; }
    else { kind='good'; data=GOOD[Math.floor(Math.random()*GOOD.length)]; }
    const size = Math.max(54, Math.min(66, W*0.14));
    items.push({
      kind, data, size,
      x: size/2 + 8 + Math.random()*(W - size - 16),
      y: -size,
      vy: (H*0.26 + p*H*0.34) * (0.85 + Math.random()*0.3) * (kind==='gold'?0.9:1),
      rot: (Math.random()-.5)*0.4, vr:(Math.random()-.5)*1.2,
      wob: Math.random()*6
    });
  }

  function addFloat(text,x,y,color){ floats.push({text,x,y,color,life:1}); }
  function burst(x,y,color,n=14){
    for(let i=0;i<n;i++){ const a=Math.random()*Math.PI*2, s=80+Math.random()*220;
      particles.push({x,y,vx:Math.cos(a)*s,vy:Math.sin(a)*s-80,life:1,color,r:2+Math.random()*3}); }
  }

  function catchItem(it){
    if (it.kind==='good'){
      combo++;
      let pts = it.data.pts * (boostT>0?2:1);
      if (combo>=5) pts += 5;
      score += pts;
      addFloat(`+${pts} ${it.data.msg}`, it.x, it.y, C.lime);
      burst(it.x,it.y,C.lime,12); sfx.good();
    } else if (it.kind==='gold'){
      score += 30; boostT = 6; shield = 1;
      addFloat('⚡ Karunya Team aa gayi! +30', it.x, it.y, C.lime);
      burst(it.x,it.y,C.lime,30); burst(it.x,it.y,'#fff',16); sfx.gold();
    } else {
      combo = 0;
      if (shield>0){
        shield=0; addFloat('🛡️ Karunya ne bacha liya!', it.x, it.y, C.lb);
        burst(it.x,it.y,C.lb,16); sfx.shield();
      } else {
        lives--; caughtBad.add(it.data.t);
        score = Math.max(0, score-10);
        addFloat(`❌ ${it.data.msg} -10`, it.x, it.y, '#ffb3bd');
        burst(it.x,it.y,C.red,18); sfx.bad(); hitFlash=1; shake=0.35;
        try{ navigator.vibrate && navigator.vibrate(80); }catch(e){}
      }
    }
    updateHUD();
    if (lives<=0) endGame();
  }

  function updateHUD(){
    $('score').textContent = score;
    $('patients').textContent = Math.floor(score*1.7);
    $('lives').textContent = '❤️'.repeat(Math.max(0,lives)) + '🤍'.repeat(Math.max(0,3-lives));
    $('timefill').style.width = (timeLeft/GAME_TIME*100)+'%';
    $('boostTag').style.display = boostT>0 ? 'block':'none';
  }

  // ---------- Loop ----------
  function loop(ts){
    const dt = Math.min(0.05, (ts-last)/1000 || 0); last=ts;
    if (state==='play') update(dt);
    draw(dt);
    requestAnimationFrame(loop);
  }

  function update(dt){
    timeLeft -= dt;
    if (timeLeft<=0){ timeLeft=0; updateHUD(); endGame(); return; }
    if (boostT>0){ boostT-=dt; if(boostT<=0){ boostT=0; } }
    hitFlash = Math.max(0, hitFlash-dt*2.5); shake=Math.max(0,shake-dt);

    // movement
    const spd = W*1.5;
    if (keys.left) player.tx -= spd*dt;
    if (keys.right) player.tx += spd*dt;
    player.tx = Math.min(Math.max(player.tx, player.w/2), W-player.w/2);
    const prev = player.x;
    player.x += (player.tx - player.x) * Math.min(1, dt*14);
    player.tilt += (((player.x-prev)/Math.max(dt,0.001))*0.0006 - player.tilt) * Math.min(1,dt*10);
    player.tilt = Math.max(-0.25, Math.min(0.25, player.tilt));

    // spawn
    spawnT -= dt;
    if (spawnT<=0){ spawn(); const p=progress(); spawnT = (0.95 - p*0.5) * (0.75+Math.random()*0.5); }

    // items
    const trayY = player.y - 128, trayW = 104;
    for (let i=items.length-1;i>=0;i--){
      const it = items[i];
      it.y += it.vy*dt; it.rot += it.vr*dt; it.wob += dt*3;
      const bottom = it.y + it.size/2;
      if (bottom >= trayY && bottom <= trayY + 34 && Math.abs(it.x - player.x) < trayW/2 + it.size*0.3){
        items.splice(i,1); catchItem(it); if(state!=='play') return; continue;
      }
      if (it.y - it.size/2 > H){
        if (it.kind==='good') combo=0;
        items.splice(i,1);
      }
    }
    for (let i=floats.length-1;i>=0;i--){ const f=floats[i]; f.y -= 60*dt; f.life -= dt*0.9; if(f.life<=0) floats.splice(i,1); }
    for (let i=particles.length-1;i>=0;i--){ const p=particles[i]; p.x+=p.vx*dt; p.y+=p.vy*dt; p.vy+=500*dt; p.life-=dt*1.6; if(p.life<=0) particles.splice(i,1); }
    updateHUD();
  }

  // ---------- Drawing ----------
  function rr(x,y,w,h,r){ ctx.beginPath(); ctx.moveTo(x+r,y); ctx.arcTo(x+w,y,x+w,y+h,r); ctx.arcTo(x+w,y+h,x,y+h,r); ctx.arcTo(x,y+h,x,y,r); ctx.arcTo(x,y,x+w,y,r); ctx.closePath(); }

  function drawBG(dt){
    const g = ctx.createLinearGradient(0,0,0,H);
    g.addColorStop(0,'#0a63cf'); g.addColorStop(0.55,C.blue); g.addColorStop(1,C.navy);
    ctx.fillStyle=g; ctx.fillRect(0,0,W,H);
    // dot grid
    ctx.fillStyle='rgba(199,209,221,0.13)';
    const gap=26;
    for(let x=gap/2;x<W;x+=gap) for(let y=gap/2;y<H;y+=gap){ ctx.beginPath(); ctx.arc(x,y,1.1,0,Math.PI*2); ctx.fill(); }
    // drifting sparkles
    for(const d of dots){ d.y += d.s*dt*3; if(d.y>1) d.y=0;
      ctx.fillStyle='rgba(209,255,66,0.35)'; ctx.beginPath(); ctx.arc(d.x*W,d.y*H,d.r,0,Math.PI*2); ctx.fill(); }
    // skyline: hospital + ghats silhouette
    ctx.fillStyle='rgba(1,42,94,0.85)';
    const base=H-0;
    ctx.beginPath(); ctx.moveTo(0,base);
    const blocks=[[0,70],[0.08,95],[0.16,60],[0.24,120],[0.34,85],[0.44,140],[0.56,100],[0.66,75],[0.76,130],[0.86,90],[0.94,65],[1,65]];
    for(let i=0;i<blocks.length-1;i++){ const [x1,h1]=blocks[i]; const [x2]=blocks[i+1]; ctx.lineTo(x1*W,base-h1); ctx.lineTo(x2*W,base-h1); }
    ctx.lineTo(W,base); ctx.closePath(); ctx.fill();
    // hospital cross on tallest
    const hx=0.50*W, hy=base-140+20;
    ctx.fillStyle='rgba(209,255,66,0.5)'; ctx.fillRect(hx-3,hy-9,6,18); ctx.fillRect(hx-9,hy-3,18,6);
    // windows
    ctx.fillStyle='rgba(176,224,230,0.18)';
    for(let i=0;i<blocks.length-1;i++){ const [x1,h1]=blocks[i]; const [x2]=blocks[i+1];
      for(let wx=x1*W+8; wx<x2*W-8; wx+=14) for(let wy=base-h1+14; wy<base-20; wy+=18) ctx.fillRect(wx,wy,5,7); }
  }

  function drawItem(it){
    const s=it.size;
    ctx.save(); ctx.translate(it.x, it.y); ctx.rotate(it.rot*0.5 + Math.sin(it.wob)*0.05);
    // shadow
    ctx.fillStyle='rgba(1,20,50,0.3)'; rr(-s/2+3,-s/2+5,s,s,14); ctx.fill();
    if (it.kind==='good'){ ctx.fillStyle=C.white; rr(-s/2,-s/2,s,s,14); ctx.fill(); ctx.strokeStyle=C.lime; ctx.lineWidth=3; ctx.stroke(); }
    else if (it.kind==='bad'){ ctx.fillStyle=C.red; rr(-s/2,-s/2,s,s,14); ctx.fill(); ctx.strokeStyle='rgba(255,255,255,0.6)'; ctx.lineWidth=2; ctx.stroke(); }
    else {
      const pulse=1+Math.sin(performance.now()/120)*0.06; ctx.scale(pulse,pulse);
      ctx.shadowColor=C.lime; ctx.shadowBlur=22;
      ctx.fillStyle=C.lime; rr(-s/2,-s/2,s,s,14); ctx.fill(); ctx.shadowBlur=0;
      ctx.fillStyle=C.navy; ctx.font=`700 ${s*0.55}px Figtree`; ctx.textAlign='center'; ctx.textBaseline='middle';
      ctx.fillText('K',-2,-s*0.08);
      ctx.fillStyle=C.blue; ctx.save(); ctx.translate(s*0.2,-s*0.26); ctx.rotate(0.45); ctx.fillRect(-2.5,-6,5,12); ctx.restore();
      ctx.fillStyle=C.navy; ctx.font=`700 ${s*0.16}px Figtree`; ctx.fillText('BOOST',0,s*0.33);
      ctx.restore(); return;
    }
    ctx.textAlign='center'; ctx.textBaseline='middle';
    ctx.font=`${s*0.42}px "Apple Color Emoji","Segoe UI Emoji","Noto Color Emoji",sans-serif`;
    ctx.fillText(it.data.e,0,-s*0.1);
    ctx.fillStyle = it.kind==='good'? C.navy : C.white;
    let fs = s*0.17; ctx.font=`700 ${fs}px Figtree`;
    while (ctx.measureText(it.data.t).width > s-8 && fs>8){ fs-=0.5; ctx.font=`700 ${fs}px Figtree`; }
    ctx.fillText(it.data.t,0,s*0.31);
    ctx.restore();
  }

  function drawPlayer(){
    const x=player.x, y=player.y;
    ctx.save(); ctx.translate(x,y); ctx.rotate(player.tilt*0.4);
    // shadow
    ctx.fillStyle='rgba(0,0,0,0.25)'; ctx.beginPath(); ctx.ellipse(0,2,38,6,0,0,Math.PI*2); ctx.fill();
    // legs
    ctx.fillStyle=C.navy; ctx.fillRect(-14,-26,11,26); ctx.fillRect(3,-26,11,26);
    ctx.fillStyle='#1b1b1b'; rr(-17,-5,15,7,3); ctx.fill(); rr(2,-5,15,7,3); ctx.fill();
    // coat body
    ctx.fillStyle=C.white; ctx.beginPath();
    ctx.moveTo(-24,-24); ctx.lineTo(-20,-74); ctx.quadraticCurveTo(0,-82,20,-74); ctx.lineTo(24,-24); ctx.closePath(); ctx.fill();
    // shirt / tie
    ctx.fillStyle=C.lb; ctx.beginPath(); ctx.moveTo(-7,-78); ctx.lineTo(7,-78); ctx.lineTo(0,-56); ctx.closePath(); ctx.fill();
    ctx.fillStyle=C.blue; ctx.beginPath(); ctx.moveTo(-3,-74); ctx.lineTo(3,-74); ctx.lineTo(4,-58); ctx.lineTo(0,-54); ctx.lineTo(-4,-58); ctx.closePath(); ctx.fill();
    // coat line + pocket
    ctx.strokeStyle=C.grey; ctx.lineWidth=1.5; ctx.beginPath(); ctx.moveTo(0,-54); ctx.lineTo(0,-26); ctx.stroke();
    ctx.strokeRect(8,-50,9,7);
    // stethoscope
    ctx.strokeStyle='#333'; ctx.lineWidth=2.5; ctx.beginPath(); ctx.moveTo(-9,-76); ctx.quadraticCurveTo(-16,-50,-4,-44); ctx.stroke();
    ctx.fillStyle='#888'; ctx.beginPath(); ctx.arc(-4,-43,3.5,0,Math.PI*2); ctx.fill();
    // arms up
    ctx.strokeStyle=C.white; ctx.lineWidth=9; ctx.lineCap='round';
    ctx.beginPath(); ctx.moveTo(-18,-70); ctx.lineTo(-34,-96); ctx.lineTo(-38,-118); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(18,-70); ctx.lineTo(34,-96); ctx.lineTo(38,-118); ctx.stroke();
    ctx.fillStyle='#E9B98A'; ctx.beginPath(); ctx.arc(-38,-120,5,0,Math.PI*2); ctx.fill(); ctx.beginPath(); ctx.arc(38,-120,5,0,Math.PI*2); ctx.fill();
    // head
    ctx.fillStyle='#E9B98A'; ctx.beginPath(); ctx.arc(0,-92,15,0,Math.PI*2); ctx.fill();
    ctx.fillStyle=C.navy; ctx.beginPath(); ctx.arc(0,-96,15.5,Math.PI*1.05,Math.PI*1.95); ctx.fill();
    ctx.fillRect(-15,-99,4,8);ctx.fillRect(11,-99,4,8);
    // face
    ctx.fillStyle=C.navy; ctx.beginPath(); ctx.arc(-5,-91,1.8,0,Math.PI*2); ctx.arc(5,-91,1.8,0,Math.PI*2); ctx.fill();
    ctx.strokeStyle=C.navy; ctx.lineWidth=1.8; ctx.beginPath();
    if (hitFlash>0.2){ ctx.arc(0,-81,4,Math.PI*1.15,Math.PI*1.85); } else { ctx.arc(0,-86,5,0.15*Math.PI,0.85*Math.PI); }
    ctx.stroke();
    // phone tray (catch zone)
    const tw=104, th=26, ty=-128-6;
    ctx.fillStyle='rgba(0,0,0,0.25)'; rr(-tw/2+2,ty+3,tw,th,9); ctx.fill();
    ctx.fillStyle=C.navy; rr(-tw/2,ty,tw,th,9); ctx.fill();
    ctx.fillStyle=boostT>0? C.lime : C.blue; rr(-tw/2+4,ty+4,tw-8,th-8,6); ctx.fill();
    ctx.fillStyle=boostT>0? C.navy : C.white; ctx.font='700 11px Figtree'; ctx.textAlign='center'; ctx.textBaseline='middle';
    ctx.fillText(boostT>0?'⚡ DOUBLE POINTS':'Dr. Saheb ka Phone', 0, ty+th/2+0.5);
    // shield
    if (shield>0){
      ctx.strokeStyle='rgba(176,224,230,'+(0.5+Math.sin(performance.now()/150)*0.3)+')'; ctx.lineWidth=3;
      ctx.beginPath(); ctx.ellipse(0,-70,62,82,0,0,Math.PI*2); ctx.stroke();
    }
    ctx.restore();
  }

  function draw(dt){
    ctx.save();
    if (shake>0){ ctx.translate((Math.random()-.5)*10*shake/0.35,(Math.random()-.5)*10*shake/0.35); }
    drawBG(dt||0);
    if (state==='play' || state==='over'){
      for(const it of items) drawItem(it);
      if (player) drawPlayer();
      for(const p of particles){ ctx.globalAlpha=Math.max(0,p.life); ctx.fillStyle=p.color; ctx.beginPath(); ctx.arc(p.x,p.y,p.r,0,Math.PI*2); ctx.fill(); }
      ctx.globalAlpha=1;
      for(const f of floats){
        ctx.globalAlpha=Math.max(0,Math.min(1,f.life*1.5));
        ctx.font='700 15px Figtree'; ctx.textAlign='center'; ctx.textBaseline='middle';
        const tx=Math.min(Math.max(f.x,90),W-90);
        ctx.lineWidth=4; ctx.strokeStyle=C.navy; ctx.strokeText(f.text,tx,f.y);
        ctx.fillStyle=f.color; ctx.fillText(f.text,tx,f.y);
      }
      ctx.globalAlpha=1;
      if (combo>=5 && state==='play'){
        ctx.font='700 13px Figtree'; ctx.textAlign='center'; ctx.fillStyle=C.lime;
        ctx.fillText(`🔥 ${combo} combo! +5 bonus`, W/2, 96);
      }
    }
    if (hitFlash>0){ ctx.fillStyle=`rgba(224,71,91,${hitFlash*0.28})`; ctx.fillRect(0,0,W,H); }
    ctx.restore();
  }

  // ---------- Flow ----------
  function startGame(){
    initAudio();
    reset();
    $('startScreen').hidden = true; $('endScreen').hidden = true;
    $('hud').style.display='block';
    if (window.innerWidth < 861) wrap.scrollIntoView({behavior:'smooth', block:'center'});
    state='play';
  }

  function endGame(){
    if (state!=='play') return;
    state='over'; sfx.end();
    setTimeout(showResult, 650);
  }

  function rankFor(s){ let r=RANKS[0][1]; for(const [min,name] of RANKS) if(s>=min) r=name; return r; }

  function showResult(){
    $('hud').style.display='none';
    if (score>best){ best=score; try{ localStorage.setItem('kd_game_best',best); }catch(e){} }
    const rank = rankFor(score);
    $('rankName').innerHTML = `<span>${rank}</span>`;
    $('fScore').textContent = score;
    $('fPatients').textContent = Math.floor(score*1.7);
    $('fBest').textContent = best;
    const L = $('lessons');
    if (caughtBad.size===0){
      L.innerHTML = `<h4>👏 Ek bhi galti nahi!</h4>Aapki marketing sense ekdum sahi hai. Ab bas consistency chahiye — Reels, GMB aur reviews har hafte.`;
    } else {
      const items = BAD.filter(b=>caughtBad.has(b.t)).slice(0,3).map(b=>`<li><b>${b.e} ${b.t}:</b> ${b.lesson}</li>`).join('');
      L.innerHTML = `<h4>💡 Asli zindagi ki seekh</h4><ul>${items}</ul>`;
    }
    const msg = `Namaste Karunya Digital! Maine "Doctor Saheb Famous Kaise Bane?" game mein ${score} score kiya (${rank}). Mujhe apni clinic/hospital ki marketing ke baare mein baat karni hai.`;
    $('waBtn').href = 'https://wa.me/916386492334?text=' + encodeURIComponent(msg);
    $('endScreen').hidden = false;
    $('endScreen').scrollTop = 0;
  }

  function toast(t){ const el=$('toast'); el.textContent=t; el.style.display='block'; clearTimeout(toast._t); toast._t=setTimeout(()=>el.style.display='none',2000); }

  $('playBtn').addEventListener('click', startGame);
  $('againBtn').addEventListener('click', startGame);
  $('copyBtn').addEventListener('click', async () => {
    const t = `Maine "Doctor Saheb Famous Kaise Bane?" game mein ${score} score kiya — rank: ${rankFor(score)}! 🩺 Aap try karo. — Karunya Digital (karunyadigital.online)`;
    try { await navigator.clipboard.writeText(t); toast('✅ Score copy ho gaya!'); }
    catch(e){ toast('Copy nahi ho paya — screenshot le lo 📸'); }
  });

  // ---------- Fullscreen ----------
  const fsBtn = $('fs');
  if (fsBtn) {
    if (!(wrap.requestFullscreen || wrap.webkitRequestFullscreen)) fsBtn.style.display='none';
    fsBtn.addEventListener('click', e => {
      e.stopPropagation();
      try {
        if (document.fullscreenElement || document.webkitFullscreenElement) (document.exitFullscreen || document.webkitExitFullscreen).call(document);
        else (wrap.requestFullscreen || wrap.webkitRequestFullscreen).call(wrap);
      } catch(err){}
    });
    ['fullscreenchange','webkitfullscreenchange'].forEach(ev => document.addEventListener(ev, () => setTimeout(resize, 60)));
  }

  // ---------- Input ----------
  function setTarget(clientX){ if(!player) return; const r=cv.getBoundingClientRect(); player.tx = clientX - r.left; }
  cv.addEventListener('pointerdown', e => { setTarget(e.clientX); });
  cv.addEventListener('pointermove', e => { if (e.pointerType==='mouse' || e.buttons || e.pressure>0) setTarget(e.clientX); });
  cv.addEventListener('touchmove', e => { e.preventDefault(); if(e.touches[0]) setTarget(e.touches[0].clientX); }, {passive:false});
  window.addEventListener('keydown', e => {
    if (e.key==='ArrowLeft'||e.key==='a'||e.key==='A') keys.left=true;
    if (e.key==='ArrowRight'||e.key==='d'||e.key==='D') keys.right=true;
    if (state==='play' && (e.key==='ArrowLeft'||e.key==='ArrowRight')) e.preventDefault();
  });
  window.addEventListener('keyup', e => {
    if (e.key==='ArrowLeft'||e.key==='a'||e.key==='A') keys.left=false;
    if (e.key==='ArrowRight'||e.key==='d'||e.key==='D') keys.right=false;
  });
  document.addEventListener('visibilitychange', () => { last = performance.now(); });

  window.addEventListener('resize', resize);
  try { new ResizeObserver(() => resize()).observe(wrap); } catch(e){}
  resize(); makeDots();
  requestAnimationFrame(ts => { last=ts; loop(ts); });
})();

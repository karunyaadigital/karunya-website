/* Karunya Digital — "Doctor Saheb Famous Kaise Bane?" game, v2 (levels, power-ups, quiz, badges) */
(() => {
  const C = {blue:'#0251B0',navy:'#012A5E',lime:'#D1FF42',lb:'#B0E0E6',grey:'#C7D1DD',paper:'#F3F6FA',red:'#E0475B',white:'#fff'};

  const LEVELS = [
    {name:'Mohalla', sub:'Pehle apne mohalle mein pehchaan banao', time:22, speed:.26, gap:.95, bad:.22, zig:0,
      sky:['#0a63cf','#0251B0','#012A5E'], blocks:[[0,46],[.1,64],[.2,42],[.3,78],[.42,56],[.55,92],[.68,52],[.8,70],[.92,48],[1,48]]},
    {name:'Shehar', sub:'Ab poora shehar aapko jaane', time:24, speed:.33, gap:.8, bad:.28, zig:.18,
      sky:['#0858bd','#0247a0','#012A5E'], blocks:[[0,70],[.08,95],[.16,60],[.24,120],[.34,85],[.44,140],[.56,100],[.66,75],[.76,130],[.86,90],[.94,65],[1,65]]},
    {name:'Pradesh', sub:'UP aur Bihar tak naam pahunchao', time:24, speed:.4, gap:.66, bad:.32, zig:.32, homing:true,
      sky:['#063f8f','#02377f','#011f47'], blocks:[[0,90],[.07,130],[.15,80],[.22,160],[.32,110],[.42,185],[.54,125],[.63,95],[.72,170],[.83,120],[.92,85],[1,85]]},
    {name:'Poora India', sub:'Desh bhar ke patients aapko dhoondh rahe hain', time:26, speed:.47, gap:.55, bad:.34, zig:.42, homing:true,
      sky:['#012A5E','#011f47','#000f26'], blocks:[[0,110],[.06,160],[.13,100],[.2,200],[.3,140],[.4,230],[.52,150],[.6,115],[.69,210],[.8,150],[.9,105],[1,105]]}
  ];
  const GOOD = [
    {e:'🎬',t:'Reel',pts:10,msg:'Reel chal padi!',lv:0},
    {e:'⭐',t:'5★ Review',pts:15,msg:'Asli review mila!',lv:0},
    {e:'📍',t:'GMB',pts:15,msg:'Google Maps pe dikhe!',lv:0},
    {e:'💬',t:'WhatsApp',pts:10,msg:'Patient ka message!',lv:0},
    {e:'🔍',t:'SEO',pts:10,msg:'Google pe upar aaye!',lv:1},
    {e:'📢',t:'Meta Ad',pts:10,msg:'Leads aa rahi hain!',lv:1},
    {e:'🌐',t:'Website',pts:10,msg:'Trust badh gaya!',lv:1},
    {e:'▶️',t:'YouTube',pts:15,msg:'Video ne samjhaya!',lv:2},
    {e:'🤝',t:'Patient Story',pts:20,msg:'Sahmati ke saath story!',lv:2},
    {e:'📰',t:'PR / News',pts:20,msg:'Akhbaar mein naam!',lv:3}
  ];
  const BAD = [
    {e:'🤥',t:'Fake Review',msg:'Fake review pakda gaya!',lv:0,lesson:'Fake reviews se Google aapki GMB listing suspend kar sakta hai. Asli patients se review maango.'},
    {e:'😴',t:'Inactive Page',msg:'Page so gaya…',lv:0,lesson:'Mahino tak post na karna = patients aapko bhool jaate hain. Regular Reels zaroori hain.'},
    {e:'🙈',t:'DM Ignore',msg:'Patient chala gaya!',lv:0,lesson:'Patient ka DM ya comment ignore kiya, toh woh kisi aur doctor ke paas chala jaata hai. Jaldi reply karo.'},
    {e:'🚫',t:'"100% Cure"',msg:'NMC guideline todi!',lv:1,lesson:'"100% cure / guarantee" jaise claims NMC guidelines ke khilaaf hain. Awareness content banao, daave nahi.'},
    {e:'💸',t:'Random Boost',msg:'Paisa barbaad!',lv:1,lesson:'Bina targeting ke "Boost Post" dabana = paisa barbaad. Sahi audience pe sahi ad chalao.'},
    {e:'🤖',t:'Fake Followers',msg:'Nakli followers!',lv:2,lesson:'Kharide hue followers kabhi patient nahi bante. Asli log tabhi judte hain jab content kaam ka ho.'},
    {e:'🖼️',t:'Bina Ijazat Photo',msg:'Patient ki privacy tooti!',lv:2,lesson:'Patient ki photo ya video unki likhit sahmati ke bina kabhi post mat karo.'},
    {e:'🕴️',t:'Competitor',msg:'Competitor aage nikal gaya!',lv:2,homing:true,lesson:'Aap online nahi dikhte, toh patient usi doctor ke paas jaata hai jo dikhta hai.'}
  ];
  const POWER = {
    k:{e:'K',t:'BOOST',msg:'⚡ Karunya Team aa gayi! +30'},
    magnet:{e:'🧲',t:'Strong Hook',msg:'🧲 Strong hook! Sab khinche aa rahe hain'},
    slow:{e:'🗓️',t:'Content Plan',msg:'🗓️ Plan ready — sab aasaan!'},
    life:{e:'❤️',t:'Patient Trust',msg:'❤️ Bharosa badha! +1 life'}
  };
  const QUIZ = [
    {q:'Google review ke badle patient ko discount ya gift dena theek hai.',a:false,why:'Google ki policy review ke badle koi bhi laalach dene se mana karti hai. Bas imaandaari se review maango.'},
    {q:'Patient ki photo ya video unki sahmati ke bina post kar sakte hain.',a:false,why:'Patient ki likhit sahmati ke bina unki photo, video ya report kabhi post nahi karni chahiye.'},
    {q:'Negative review ka shaant aur polite jawab dena chahiye.',a:true,why:'Shaant jawab padhne wale naye patients ka bharosa badhata hai. Jawab mein patient ki bimari ki baat mat likho.'},
    {q:'"100% guaranteed ilaaj" likhna doctor ke liye theek hai.',a:false,why:'Guarantee ya cure ke daave NMC guidelines ke khilaaf hain. Jaankari do, daave nahi.'},
    {q:'Google profile pe clinic ka sahi time aur phone number hona zaroori hai.',a:true,why:'Galat time ya number se patient clinic tak pahunch hi nahi paata, aur bharosa bhi toot-ta hai.'},
    {q:'Followers kharidne se asli patients badhte hain.',a:false,why:'Nakli followers appointment nahi lete. Kaam ka content hi asli logon ko laata hai.'},
    {q:'Har hafte thoda post karna, mahine mein ek din 10 post karne se behtar hai.',a:true,why:'Regular dikhne se log yaad rakhte hain. Ek din ki bheed agle hafte tak bhool jaati hai.'},
    {q:'Patient ke DM ka jawab 2-3 din baad dena chalta hai.',a:false,why:'Bimaar insaan intezaar nahi karta. Jo pehle jawab deta hai, patient aksar usi ke paas jaata hai.'}
  ];
  const RANKS = [[0,'Naye Doctor Saheb'],[400,'Mohalle ke Famous'],[1000,'Shehar ke Top Doctor'],[2000,'Pradesh ke Star Doctor'],[3500,'India ke Famous Doctor']];
  const BADGES = [
    {id:'clean',e:'🧼',n:'Zero Galti'},
    {id:'combo',e:'🔥',n:'Combo King'},
    {id:'quiz',e:'🎓',n:'Quiz Topper'},
    {id:'kteam',e:'⚡',n:'Karunya Partner'},
    {id:'india',e:'🇮🇳',n:'India Famous'}
  ];
  const MAX_LIVES = 4;

  const wrap = document.getElementById('kg');
  if (!wrap) return;
  const cv = wrap.querySelector('canvas');
  const ctx = cv.getContext('2d');
  const $ = id => document.getElementById('kg-' + id);
  const store = {
    get(k,d){ try{ const v=localStorage.getItem('kd_game_'+k); return v===null?d:v; }catch(e){ return d; } },
    set(k,v){ try{ localStorage.setItem('kd_game_'+k,v); }catch(e){} }
  };
  let W=0,H=0,DPR=1;

  function resize(){
    DPR = Math.min(window.devicePixelRatio||1, 2.5);
    W = wrap.clientWidth; H = wrap.clientHeight;
    cv.width = W*DPR; cv.height = H*DPR;
    ctx.setTransform(DPR,0,0,DPR,0,0);
    if (player) { player.y = H - 18; player.x = Math.min(Math.max(player.x, 50), W-50); }
  }

  // ---------- Sound ----------
  let actx=null, muted = store.get('muted','0')==='1';
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
  const seq = (arr,gap,type,vol) => arr.forEach((f,i)=>setTimeout(()=>beep(f,.11,type,vol),i*gap));
  const sfx = {
    good(m){ const b=600+Math.min(m,4)*60; beep(b,.07,'triangle',.14); setTimeout(()=>beep(b*1.5,.09,'triangle',.12),55); },
    bad(){ beep(220,.25,'sawtooth',.10,-120); },
    gold(){ seq([523,659,784,1047],70,'square',.07); },
    power(){ seq([440,660,880],60,'sine',.12); },
    shield(){ beep(400,.12,'sine',.12,300); },
    level(){ seq([523,659,784,1047,1319],90,'triangle',.12); },
    viral(){ seq([784,988,1175,1568],55,'square',.06); },
    right(){ seq([659,880],90,'triangle',.14); },
    wrong(){ seq([300,220],120,'sawtooth',.08); },
    end(){ seq([784,659,523,392],110,'triangle',.12); },
    win(){ seq([523,659,784,1047,784,1047,1319],100,'triangle',.13); }
  };
  $('mute').addEventListener('click', e => {
    e.stopPropagation(); muted=!muted; $('mute').textContent = muted?'🔇':'🔊';
    store.set('muted', muted?'1':'0'); if(!muted) initAudio();
  });

  // ---------- State ----------
  let player=null, items=[], floats=[], particles=[], state='menu', last=0;
  let score=0, lives=3, level=0, levelT=0, spawnT=0, combo=0, maxCombo=0, hitFlash=0, shake=0, bannerT=0;
  let boostT=0, shield=0, magnetT=0, slowT=0, viralT=0;
  let goodCaught=0, goodMissed=0, kCaught=0, quizRight=0, quizAsked=0, quizSet=[], won=false;
  let caughtBad = new Set();
  let keys={left:false,right:false};
  let avatar = store.get('avatar','m');
  let best = +store.get('best',0) || 0;
  let badges = new Set((store.get('badges','')||'').split(',').filter(Boolean));
  let dots=[];
  function makeDots(){ dots=[]; for(let i=0;i<46;i++) dots.push({x:Math.random(),y:Math.random(),r:Math.random()*1.8+0.6,s:Math.random()*0.02+0.01}); }
  const mult = () => combo>=20?4 : combo>=10?3 : combo>=5?2 : 1;
  const rankFor = s => { let r=RANKS[0][1]; for(const [min,name] of RANKS) if(s>=min) r=name; return r; };

  function reset(){
    player = {x:W/2, tx:W/2, y:H-18, w:96, tilt:0};
    items=[]; floats=[]; particles=[]; caughtBad=new Set();
    score=0; lives=3; level=0; combo=0; maxCombo=0; hitFlash=0; shake=0;
    boostT=0; shield=0; magnetT=0; slowT=0; viralT=0;
    goodCaught=0; goodMissed=0; kCaught=0; quizRight=0; quizAsked=0; won=false;
    quizSet = QUIZ.slice().sort(()=>Math.random()-.5).slice(0,LEVELS.length-1);
  }
  function beginLevel(n){
    level=n; levelT=LEVELS[n].time; spawnT=.5; items=[]; bannerT=2.4; state='banner';
    if(n>0) sfx.level();
    updateHUD();
  }

  function spawn(){
    const L = LEVELS[level], lp = 1 - levelT/L.time;
    const r = Math.random();
    let kind, data, pid=null;
    if (viralT>0) { kind='good'; }
    else if (r < 0.075) {
      kind='power';
      const pool=['k','k','magnet','slow']; if (lives<MAX_LIVES) pool.push('life'); if (level===0) pool.push('k');
      pid = pool[Math.floor(Math.random()*pool.length)];
      if ((pid==='k'&&boostT>0)||(pid==='magnet'&&magnetT>0)||(pid==='slow'&&slowT>0)) { kind='good'; pid=null; }
      else data = POWER[pid];
    }
    else if (r < 0.075 + L.bad + lp*0.06) kind='bad';
    else kind='good';
    if (kind==='good'){ const pool=GOOD.filter(g=>g.lv<=level); data=pool[Math.floor(Math.random()*pool.length)]; }
    if (kind==='bad'){ const pool=BAD.filter(b=>b.lv<=level && (!b.homing || L.homing)); data=pool[Math.floor(Math.random()*pool.length)]; }
    const size = Math.max(54, Math.min(66, W*0.14));
    const x = size/2 + 8 + Math.random()*(W - size - 16);
    items.push({
      kind, data, pid, size, x, bx:x, y:-size,
      vy: H*L.speed*(1+lp*.15) * (0.85 + Math.random()*0.3) * (kind==='power'?0.9:1),
      zig: (kind!=='power' && !data.homing && Math.random()<L.zig) ? 30+Math.random()*45 : 0, zp: Math.random()*6,
      rot:(Math.random()-.5)*0.4, vr:(Math.random()-.5)*1.2, wob:Math.random()*6
    });
  }

  function addFloat(text,x,y,color){ floats.push({text,x,y,color,life:1}); }
  function burst(x,y,color,n=14){
    for(let i=0;i<n;i++){ const a=Math.random()*Math.PI*2, s=80+Math.random()*220;
      particles.push({x,y,vx:Math.cos(a)*s,vy:Math.sin(a)*s-80,life:1,color,r:2+Math.random()*3}); }
  }
  function confetti(){
    const cols=[C.lime,C.white,C.lb,'#7fb6ff'];
    for(let i=0;i<90;i++) particles.push({x:Math.random()*W,y:-10-Math.random()*H*.4,vx:(Math.random()-.5)*120,vy:60+Math.random()*160,life:2.2,color:cols[i%4],r:2.5+Math.random()*3});
  }

  function catchItem(it){
    if (it.kind==='good'){
      combo++; goodCaught++; if(combo>maxCombo) maxCombo=combo;
      const m = mult();
      const pts = it.data.pts * m * (boostT>0?2:1) * (viralT>0?2:1);
      score += pts;
      addFloat(`+${pts} ${viralT>0?'🔥':it.data.msg}`, it.x, it.y, C.lime);
      burst(it.x,it.y,C.lime,10); sfx.good(m);
      if (combo%12===0 && viralT<=0){ viralT=5; addFloat('🔥 VIRAL MODE!', W/2, H*.4, C.lime); burst(W/2,H*.4,C.lime,40); sfx.viral(); }
    } else if (it.kind==='power'){
      if (it.pid==='k'){ score+=30; boostT=6; shield=1; kCaught++; sfx.gold(); burst(it.x,it.y,'#fff',16); }
      else if (it.pid==='magnet'){ magnetT=6; sfx.power(); }
      else if (it.pid==='slow'){ slowT=5; sfx.power(); }
      else { lives=Math.min(MAX_LIVES,lives+1); sfx.power(); }
      addFloat(it.data.msg, it.x, it.y, C.lime); burst(it.x,it.y,C.lime,26);
    } else {
      combo=0;
      if (shield>0){ shield=0; addFloat('🛡️ Karunya ne bacha liya!', it.x, it.y, C.lb); burst(it.x,it.y,C.lb,16); sfx.shield(); }
      else {
        lives--; caughtBad.add(it.data.t); score=Math.max(0,score-10);
        addFloat(`❌ ${it.data.msg}`, it.x, it.y, '#ffb3bd');
        burst(it.x,it.y,C.red,18); sfx.bad(); hitFlash=1; shake=0.35;
        try{ navigator.vibrate && navigator.vibrate(80); }catch(e){}
      }
    }
    updateHUD();
    if (lives<=0) endGame(false);
  }

  function updateHUD(){
    $('score').textContent = score;
    $('level').textContent = `L${level+1} · ${LEVELS[level].name}`;
    $('lives').textContent = '❤️'.repeat(Math.max(0,lives)) + '🤍'.repeat(Math.max(0,3-lives));
    $('timefill').style.width = Math.max(0, levelT/LEVELS[level].time*100)+'%';
  }
  function showOnly(id){
    ['startScreen','endScreen','quiz','pauseScreen'].forEach(k => { $(k).hidden = k!==id; });
    const playing = !id;
    $('hud').style.display = playing ? 'block':'none';
    $('pause').style.display = playing ? 'grid':'none';
    wrap.classList.toggle('kg-playing', playing);
    wrap.classList.toggle('kg-end', id==='endScreen');
  }

  // ---------- Loop ----------
  function loop(ts){
    const dt = Math.min(0.05, (ts-last)/1000 || 0); last=ts;
    if (state==='play') update(dt);
    else if (state==='banner'){ bannerT-=dt; movePlayer(dt); tickFx(dt); if(bannerT<=0) state='play'; }
    else if (state==='over') tickFx(dt);
    draw(dt);
    requestAnimationFrame(loop);
  }
  function movePlayer(dt){
    const spd = W*1.5;
    if (keys.left) player.tx -= spd*dt;
    if (keys.right) player.tx += spd*dt;
    player.tx = Math.min(Math.max(player.tx, player.w/2), W-player.w/2);
    const prev = player.x;
    player.x += (player.tx - player.x) * Math.min(1, dt*14);
    player.tilt += (((player.x-prev)/Math.max(dt,0.001))*0.0006 - player.tilt) * Math.min(1,dt*10);
    player.tilt = Math.max(-0.25, Math.min(0.25, player.tilt));
  }
  function tickFx(dt){
    hitFlash = Math.max(0, hitFlash-dt*2.5); shake=Math.max(0,shake-dt);
    for (let i=floats.length-1;i>=0;i--){ const f=floats[i]; f.y -= 60*dt; f.life -= dt*0.9; if(f.life<=0) floats.splice(i,1); }
    for (let i=particles.length-1;i>=0;i--){ const p=particles[i]; p.x+=p.vx*dt; p.y+=p.vy*dt; p.vy+=(p.life>1?120:500)*dt; p.life-=dt*(p.life>1?.6:1.6); if(p.life<=0) particles.splice(i,1); }
  }

  function update(dt){
    levelT -= dt;
    boostT=Math.max(0,boostT-dt); magnetT=Math.max(0,magnetT-dt); slowT=Math.max(0,slowT-dt); viralT=Math.max(0,viralT-dt);
    if (levelT<=0){ levelT=0; updateHUD(); levelDone(); return; }
    movePlayer(dt); tickFx(dt);
    const ts = slowT>0 ? .5 : 1;

    spawnT -= dt*(slowT>0?.7:1);
    if (spawnT<=0){ spawn(); const L=LEVELS[level], lp=1-levelT/L.time; spawnT = viralT>0 ? .2 : (L.gap - lp*.12) * (0.75+Math.random()*0.5); }

    const trayY = player.y - 128, trayW = 104;
    for (let i=items.length-1;i>=0;i--){
      const it = items[i];
      it.y += it.vy*ts*dt; it.rot += it.vr*dt; it.wob += dt*3;
      if (it.data.homing) it.bx += Math.sign(player.x-it.bx)*Math.min(Math.abs(player.x-it.bx), 55*dt*ts);
      if (magnetT>0 && it.kind!=='bad' && it.y>0) it.bx += (player.x-it.bx)*Math.min(1,dt*3.4);
      if (it.zig){ it.zp += dt*2.4*ts; it.x = it.bx + Math.sin(it.zp)*it.zig*(magnetT>0&&it.kind!=='bad'?.2:1); } else it.x = it.bx;
      it.x = Math.min(Math.max(it.x, it.size/2+4), W-it.size/2-4);
      const bottom = it.y + it.size/2;
      if (bottom >= trayY && bottom <= trayY + 36 && Math.abs(it.x - player.x) < trayW/2 + it.size*0.3){
        items.splice(i,1); catchItem(it); if(state!=='play') return; continue;
      }
      if (it.y - it.size/2 > H){
        if (it.kind==='good'){ combo=0; goodMissed++; }
        items.splice(i,1);
      }
    }
    updateHUD();
  }

  // ---------- Level flow / quiz ----------
  function levelDone(){
    const bonus = 50*(level+1);
    score += bonus; items=[]; boostT=magnetT=slowT=viralT=0;
    if (level >= LEVELS.length-1){ endGame(true); return; }
    state='quiz'; sfx.level();
    const q = quizSet[level]; quizAsked++;
    $('qTag').textContent = `Level ${level+1} clear! +${bonus} · Bonus sawaal`;
    $('qText').textContent = q.q;
    $('qBtns').hidden = false; $('qRes').hidden = true; $('qNext').hidden = true;
    $('qNext').textContent = `Level ${level+2}: ${LEVELS[level+1].name} →`;
    showOnly('quiz');
  }
  function answer(val){
    if (state!=='quiz' || !$('qRes').hidden) return;
    const q = quizSet[level], ok = q.a===val, pts = 100*(level+1);
    if (ok){ quizRight++; score+=pts; sfx.right(); } else sfx.wrong();
    $('qRes').innerHTML = `<b class="${ok?'ok':'no'}">${ok?`✅ Bilkul sahi! +${pts}`:`❌ Galat jawab. Sahi jawab: ${q.a?'Sahi':'Galat'}`}</b>${q.why}`;
    $('qBtns').hidden = true; $('qRes').hidden = false; $('qNext').hidden = false;
  }
  $('qYes').addEventListener('click', () => answer(true));
  $('qNo').addEventListener('click', () => answer(false));
  $('qNext').addEventListener('click', () => { if(state!=='quiz') return; showOnly(null); last=performance.now(); beginLevel(level+1); });

  // ---------- Pause ----------
  let pausedFrom=null;
  function pause(){ if(state!=='play' && state!=='banner') return; pausedFrom=state; state='pause'; showOnly('pauseScreen'); }
  function resume(){ if(state!=='pause') return; showOnly(null); last=performance.now(); state=pausedFrom||'play'; }
  $('pause').addEventListener('click', e => { e.stopPropagation(); pause(); });
  $('resumeBtn').addEventListener('click', resume);
  $('quitBtn').addEventListener('click', () => { state='menu'; showOnly('startScreen'); });
  document.addEventListener('visibilitychange', () => { if(document.hidden) pause(); last = performance.now(); });

  // ---------- Drawing ----------
  function rr(x,y,w,h,r){ ctx.beginPath(); ctx.moveTo(x+r,y); ctx.arcTo(x+w,y,x+w,y+h,r); ctx.arcTo(x+w,y+h,x,y+h,r); ctx.arcTo(x,y+h,x,y,r); ctx.arcTo(x,y,x+w,y,r); ctx.closePath(); }

  function drawBG(dt){
    const L = LEVELS[state==='menu'?0:level];
    const g = ctx.createLinearGradient(0,0,0,H);
    g.addColorStop(0,L.sky[0]); g.addColorStop(0.55,L.sky[1]); g.addColorStop(1,L.sky[2]);
    ctx.fillStyle=g; ctx.fillRect(0,0,W,H);
    if (viralT>0){ ctx.fillStyle=`rgba(209,255,66,${.06+Math.sin(performance.now()/90)*.03})`; ctx.fillRect(0,0,W,H); }
    ctx.fillStyle='rgba(199,209,221,0.13)';
    const gap=26;
    for(let x=gap/2;x<W;x+=gap) for(let y=gap/2;y<H;y+=gap){ ctx.beginPath(); ctx.arc(x,y,1.1,0,Math.PI*2); ctx.fill(); }
    const sp = (viralT>0?14:3) * (slowT>0?.4:1);
    for(const d of dots){ d.y += d.s*dt*sp; if(d.y>1) d.y=0;
      ctx.fillStyle='rgba(209,255,66,0.35)'; ctx.beginPath(); ctx.arc(d.x*W,d.y*H,d.r,0,Math.PI*2); ctx.fill(); }
    // skyline
    const blocks=L.blocks, base=H, k=Math.min(1,H/760);
    ctx.fillStyle='rgba(1,30,70,0.88)';
    ctx.beginPath(); ctx.moveTo(0,base);
    let top=0, tx=0;
    for(let i=0;i<blocks.length-1;i++){ const [x1,h1]=blocks[i]; const [x2]=blocks[i+1]; ctx.lineTo(x1*W,base-h1*k); ctx.lineTo(x2*W,base-h1*k); if(h1>top){ top=h1; tx=(x1+x2)/2; } }
    ctx.lineTo(W,base); ctx.closePath(); ctx.fill();
    const hx=tx*W, hy=base-top*k+20;
    ctx.fillStyle='rgba(209,255,66,0.55)'; ctx.fillRect(hx-3,hy-9,6,18); ctx.fillRect(hx-9,hy-3,18,6);
    ctx.fillStyle='rgba(176,224,230,0.18)';
    for(let i=0;i<blocks.length-1;i++){ const [x1,h1]=blocks[i]; const [x2]=blocks[i+1];
      for(let wx=x1*W+8; wx<x2*W-8; wx+=14) for(let wy=base-h1*k+(i===Math.round(tx*10)?40:14); wy<base-20; wy+=18) ctx.fillRect(wx,wy,5,7); }
  }

  function drawItem(it){
    const s=it.size;
    ctx.save(); ctx.translate(it.x, it.y); ctx.rotate(it.rot*0.5 + Math.sin(it.wob)*0.05);
    ctx.fillStyle='rgba(1,20,50,0.3)'; rr(-s/2+3,-s/2+5,s,s,14); ctx.fill();
    ctx.textAlign='center'; ctx.textBaseline='middle';
    if (it.kind==='power'){
      const pulse=1+Math.sin(performance.now()/120)*0.06; ctx.scale(pulse,pulse);
      ctx.shadowColor=C.lime; ctx.shadowBlur=22;
      ctx.fillStyle = it.pid==='k' ? C.lime : C.navy; rr(-s/2,-s/2,s,s,14); ctx.fill(); ctx.shadowBlur=0;
      if (it.pid==='k'){
        ctx.fillStyle=C.navy; ctx.font=`700 ${s*0.55}px Figtree, sans-serif`; ctx.fillText('K',-2,-s*0.08);
        ctx.fillStyle=C.blue; ctx.save(); ctx.translate(s*0.2,-s*0.26); ctx.rotate(0.45); ctx.fillRect(-2.5,-6,5,12); ctx.restore();
        ctx.fillStyle=C.navy; ctx.font=`700 ${s*0.16}px Figtree, sans-serif`; ctx.fillText('BOOST',0,s*0.33);
        ctx.restore(); return;
      }
      ctx.strokeStyle=C.lime; ctx.lineWidth=3; ctx.stroke();
    }
    else if (it.kind==='good'){ ctx.fillStyle=C.white; rr(-s/2,-s/2,s,s,14); ctx.fill(); ctx.strokeStyle=C.lime; ctx.lineWidth=3; ctx.stroke(); }
    else { ctx.fillStyle=C.red; rr(-s/2,-s/2,s,s,14); ctx.fill(); ctx.strokeStyle='rgba(255,255,255,0.6)'; ctx.lineWidth=2; ctx.stroke(); }
    ctx.font=`${s*0.42}px "Apple Color Emoji","Segoe UI Emoji","Noto Color Emoji",sans-serif`;
    ctx.fillText(it.data.e,0,-s*0.1);
    ctx.fillStyle = it.kind==='good'? C.navy : it.kind==='power' ? C.lime : C.white;
    let fs = s*0.17; ctx.font=`700 ${fs}px Figtree, sans-serif`;
    while (ctx.measureText(it.data.t).width > s-8 && fs>7){ fs-=0.5; ctx.font=`700 ${fs}px Figtree, sans-serif`; }
    ctx.fillText(it.data.t,0,s*0.31);
    ctx.restore();
  }

  function drawPlayer(){
    const x=player.x, y=player.y, fem = avatar==='f', skin='#E9B98A';
    ctx.save(); ctx.translate(x,y); ctx.rotate(player.tilt*0.4);
    if (magnetT>0){
      const t=performance.now()/400;
      for(let i=0;i<3;i++){ const r=40+((t+i/3)%1)*90; ctx.strokeStyle=`rgba(209,255,66,${.5*(1-((t+i/3)%1))})`; ctx.lineWidth=2.5; ctx.beginPath(); ctx.arc(0,-134,r,Math.PI*1.1,Math.PI*1.9); ctx.stroke(); }
    }
    ctx.fillStyle='rgba(0,0,0,0.25)'; ctx.beginPath(); ctx.ellipse(0,2,38,6,0,0,Math.PI*2); ctx.fill();
    ctx.fillStyle=C.navy; ctx.fillRect(-14,-26,11,26); ctx.fillRect(3,-26,11,26);
    ctx.fillStyle='#1b1b1b'; rr(-17,-5,15,7,3); ctx.fill(); rr(2,-5,15,7,3); ctx.fill();
    if (fem){ ctx.fillStyle=C.navy; rr(-17,-104,34,44,12); ctx.fill(); }
    ctx.fillStyle=C.white; ctx.beginPath();
    ctx.moveTo(-24,-24); ctx.lineTo(-20,-74); ctx.quadraticCurveTo(0,-82,20,-74); ctx.lineTo(24,-24); ctx.closePath(); ctx.fill();
    ctx.fillStyle=fem?C.lime:C.lb; ctx.beginPath(); ctx.moveTo(-7,-78); ctx.lineTo(7,-78); ctx.lineTo(0,-56); ctx.closePath(); ctx.fill();
    if (!fem){ ctx.fillStyle=C.blue; ctx.beginPath(); ctx.moveTo(-3,-74); ctx.lineTo(3,-74); ctx.lineTo(4,-58); ctx.lineTo(0,-54); ctx.lineTo(-4,-58); ctx.closePath(); ctx.fill(); }
    ctx.strokeStyle=C.grey; ctx.lineWidth=1.5; ctx.beginPath(); ctx.moveTo(0,-54); ctx.lineTo(0,-26); ctx.stroke();
    ctx.strokeRect(8,-50,9,7);
    ctx.strokeStyle='#333'; ctx.lineWidth=2.5; ctx.beginPath(); ctx.moveTo(-9,-76); ctx.quadraticCurveTo(-16,-50,-4,-44); ctx.stroke();
    ctx.fillStyle='#888'; ctx.beginPath(); ctx.arc(-4,-43,3.5,0,Math.PI*2); ctx.fill();
    ctx.strokeStyle=C.white; ctx.lineWidth=9; ctx.lineCap='round';
    ctx.beginPath(); ctx.moveTo(-18,-70); ctx.lineTo(-34,-96); ctx.lineTo(-38,-118); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(18,-70); ctx.lineTo(34,-96); ctx.lineTo(38,-118); ctx.stroke();
    ctx.fillStyle=skin; ctx.beginPath(); ctx.arc(-38,-120,5,0,Math.PI*2); ctx.fill(); ctx.beginPath(); ctx.arc(38,-120,5,0,Math.PI*2); ctx.fill();
    ctx.fillStyle=skin; ctx.beginPath(); ctx.arc(0,-92,15,0,Math.PI*2); ctx.fill();
    ctx.fillStyle=C.navy; ctx.beginPath(); ctx.arc(0,-96,15.5,Math.PI*1.05,Math.PI*1.95); ctx.fill();
    if (fem){ ctx.beginPath(); ctx.arc(0,-112,7,0,Math.PI*2); ctx.fill(); ctx.fillRect(-16,-99,4,14); ctx.fillRect(12,-99,4,14);
      ctx.fillStyle=C.lime; ctx.beginPath(); ctx.arc(-15,-84,2,0,Math.PI*2); ctx.arc(15,-84,2,0,Math.PI*2); ctx.fill(); }
    else { ctx.fillRect(-15,-99,4,8); ctx.fillRect(11,-99,4,8); }
    ctx.fillStyle=C.navy; ctx.beginPath(); ctx.arc(-5,-91,1.8,0,Math.PI*2); ctx.arc(5,-91,1.8,0,Math.PI*2); ctx.fill();
    ctx.strokeStyle=C.navy; ctx.lineWidth=1.8; ctx.beginPath();
    if (hitFlash>0.2) ctx.arc(0,-81,4,Math.PI*1.15,Math.PI*1.85); else ctx.arc(0,-86,5,0.15*Math.PI,0.85*Math.PI);
    ctx.stroke();
    const tw=104, th=26, ty=-134, hot = boostT>0||viralT>0;
    ctx.fillStyle='rgba(0,0,0,0.25)'; rr(-tw/2+2,ty+3,tw,th,9); ctx.fill();
    ctx.fillStyle=C.navy; rr(-tw/2,ty,tw,th,9); ctx.fill();
    ctx.fillStyle=hot? C.lime : C.blue; rr(-tw/2+4,ty+4,tw-8,th-8,6); ctx.fill();
    ctx.fillStyle=hot? C.navy : C.white; ctx.font='700 11px Figtree, sans-serif'; ctx.textAlign='center'; ctx.textBaseline='middle';
    ctx.fillText(viralT>0?'🔥 VIRAL MODE':boostT>0?'⚡ DOUBLE POINTS':(fem?'Dr. Sahiba ka Phone':'Dr. Saheb ka Phone'), 0, ty+th/2+0.5);
    if (shield>0){
      ctx.strokeStyle='rgba(176,224,230,'+(0.5+Math.sin(performance.now()/150)*0.3)+')'; ctx.lineWidth=3;
      ctx.beginPath(); ctx.ellipse(0,-70,62,82,0,0,Math.PI*2); ctx.stroke();
    }
    ctx.restore();
  }

  function drawChips(){
    const chips=[];
    if (viralT>0) chips.push(['🔥 Viral',viralT,5]);
    if (boostT>0) chips.push(['⚡ 2x',boostT,6]);
    if (magnetT>0) chips.push(['🧲 Hook',magnetT,6]);
    if (slowT>0) chips.push(['🗓️ Slow',slowT,5]);
    if (shield>0) chips.push(['🛡️ Shield',1,1]);
    ctx.font='700 12px Figtree, sans-serif'; ctx.textBaseline='middle'; ctx.textAlign='center';
    const ws = chips.map(c=>ctx.measureText(c[0]).width+22), total = ws.reduce((a,b)=>a+b+6,-6);
    let x = W/2-total/2; const y=82;
    chips.forEach((c,i)=>{
      const w=ws[i];
      ctx.fillStyle='rgba(1,42,94,.85)'; rr(x,y-12,w,24,12); ctx.fill();
      ctx.fillStyle=C.lime; rr(x,y+9,w*Math.max(0,c[1]/c[2]),3,1.5); ctx.fill();
      ctx.fillStyle='#fff'; ctx.fillText(c[0],x+w/2,y); x+=w+6;
    });
    if (combo>=3){
      const m=mult(); ctx.font=`700 ${m>1?16:13}px Figtree, sans-serif`; ctx.fillStyle=m>1?C.lime:'#fff';
      ctx.lineWidth=4; ctx.strokeStyle=C.navy;
      const t = m>1 ? `x${m} · ${combo} combo` : `${combo} combo`;
      ctx.strokeText(t,W/2,chips.length?112:86); ctx.fillText(t,W/2,chips.length?112:86);
    }
  }

  function drawBanner(){
    const a = Math.min(1, bannerT/.3, (2.4-bannerT)/.3), L=LEVELS[level];
    ctx.save(); ctx.globalAlpha=Math.max(0,a);
    const bw=Math.min(W-36,360), bh=168, bx=W/2-bw/2, by=H*.32-bh/2;
    ctx.fillStyle='rgba(1,42,94,.92)'; rr(bx,by,bw,bh,22); ctx.fill();
    ctx.strokeStyle=C.lime; ctx.lineWidth=2; ctx.stroke();
    ctx.textAlign='center'; ctx.textBaseline='middle';
    ctx.fillStyle=C.lime; ctx.font='700 13px Figtree, sans-serif'; ctx.fillText(`LEVEL ${level+1} / ${LEVELS.length}`, W/2, by+34);
    ctx.fillStyle='#fff'; ctx.font='400 40px Waylimo, Georgia, serif'; ctx.fillText(L.name, W/2, by+78);
    ctx.fillStyle=C.lb; ctx.font='500 14px Figtree, sans-serif';
    const words=L.sub.split(' '); let line='', ly=by+118;
    for(const w of words){ if(ctx.measureText(line+w).width>bw-40){ ctx.fillText(line.trim(),W/2,ly); line=''; ly+=20; } line+=w+' '; }
    ctx.fillText(line.trim(),W/2,ly);
    ctx.restore();
  }

  function draw(dt){
    ctx.save();
    if (shake>0) ctx.translate((Math.random()-.5)*10*shake/0.35,(Math.random()-.5)*10*shake/0.35);
    drawBG(state==='pause'||state==='quiz'?0:(dt||0));
    if (state!=='menu'){
      for(const it of items) drawItem(it);
      if (player) drawPlayer();
      for(const p of particles){ ctx.globalAlpha=Math.max(0,Math.min(1,p.life)); ctx.fillStyle=p.color; ctx.beginPath(); ctx.arc(p.x,p.y,p.r,0,Math.PI*2); ctx.fill(); }
      ctx.globalAlpha=1;
      for(const f of floats){
        ctx.globalAlpha=Math.max(0,Math.min(1,f.life*1.5));
        ctx.font='700 15px Figtree, sans-serif'; ctx.textAlign='center'; ctx.textBaseline='middle';
        const hw=ctx.measureText(f.text).width/2+6, tx=Math.min(Math.max(f.x,hw),W-hw);
        ctx.lineWidth=4; ctx.strokeStyle=C.navy; ctx.strokeText(f.text,tx,f.y);
        ctx.fillStyle=f.color; ctx.fillText(f.text,tx,f.y);
      }
      ctx.globalAlpha=1;
      if (state==='play') drawChips();
      if (state==='banner') drawBanner();
    }
    if (hitFlash>0){ ctx.fillStyle=`rgba(224,71,91,${hitFlash*0.28})`; ctx.fillRect(0,0,W,H); }
    ctx.restore();
  }

  // ---------- Flow ----------
  function startGame(){
    initAudio(); resize(); reset(); showOnly(null);
    if (window.innerWidth < 861) wrap.scrollIntoView({behavior:'smooth', block:'center'});
    last=performance.now(); beginLevel(0);
  }
  function endGame(win){
    if (state==='over') return;
    state='over'; won=win;
    if (win){ sfx.win(); confetti(); } else sfx.end();
    setTimeout(showResult, win?1500:700);
  }

  function showResult(){
    if (state!=='over') return;
    if (score>best){ best=score; store.set('best',best); }
    const rank = won && score<RANKS[4][0] ? RANKS[4][1] : rankFor(score);
    const acc = goodCaught+goodMissed ? Math.round(goodCaught/(goodCaught+goodMissed)*100) : 0;
    const earned = new Set();
    if (caughtBad.size===0 && level>=1) earned.add('clean');
    if (maxCombo>=15) earned.add('combo');
    if (quizAsked===LEVELS.length-1 && quizRight===quizAsked) earned.add('quiz');
    if (kCaught>=2) earned.add('kteam');
    if (won) earned.add('india');
    const fresh = [...earned].filter(b=>!badges.has(b));
    earned.forEach(b=>badges.add(b)); store.set('badges',[...badges].join(','));

    $('endTag').textContent = won ? '🎉 Charon level clear!' : `Level ${level+1} · ${LEVELS[level].name} tak pahunche`;
    $('rankName').innerHTML = `<span>${rank}</span>`;
    $('fScore').textContent = score;
    $('fPatients').textContent = Math.floor(score*1.7);
    $('fBest').textContent = best;
    $('mini').innerHTML = `<span>🔥 Best combo <b>${maxCombo}</b></span><span>🎯 Accuracy <b>${acc}%</b></span><span>🎓 Quiz <b>${quizRight}/${quizAsked}</b></span>`;
    $('badges').innerHTML = BADGES.map(b=>`<span class="${badges.has(b.id)?'on':''}${fresh.includes(b.id)?' new':''}" title="${b.n}"><i>${b.e}</i>${b.n}</span>`).join('');
    const L = $('lessons');
    if (caughtBad.size===0){
      L.innerHTML = `<h4>👏 Ek bhi galti nahi!</h4>Aapki marketing sense ekdum sahi hai. Ab bas consistency chahiye: Reels, GMB aur reviews har hafte.`;
    } else {
      L.innerHTML = `<h4>💡 Asli zindagi ki seekh</h4><ul>${BAD.filter(b=>caughtBad.has(b.t)).slice(0,2).map(b=>`<li><b>${b.e} ${b.t}:</b> ${b.lesson}</li>`).join('')}</ul>`;
    }
    const msg = `Namaste Karunya Digital! Maine "Doctor Saheb Famous Kaise Bane?" game mein ${score} score kiya (${rank}, Level ${level+1}). Mujhe apni clinic/hospital ki marketing ke baare mein baat karni hai.`;
    $('waBtn').href = 'https://wa.me/916386492334?text=' + encodeURIComponent(msg);
    showOnly('endScreen'); $('endScreen').scrollTop = 0;
  }

  function toast(t){ const el=$('toast'); el.textContent=t; el.style.display='block'; clearTimeout(toast._t); toast._t=setTimeout(()=>el.style.display='none',2000); }

  $('playBtn').addEventListener('click', startGame);
  $('againBtn').addEventListener('click', startGame);
  $('copyBtn').addEventListener('click', async () => {
    const t = `Maine "Doctor Saheb Famous Kaise Bane?" game mein ${score} score kiya, rank: ${rankFor(score)}! 🩺 Aap try karo: karunyadigital.online/game.html`;
    try { await navigator.clipboard.writeText(t); toast('✅ Score copy ho gaya!'); }
    catch(e){ toast('Copy nahi ho paya, screenshot le lo 📸'); }
  });
  const picks = wrap.querySelectorAll('[data-avatar]');
  const setAvatar = a => { avatar=a; store.set('avatar',a); picks.forEach(b=>b.setAttribute('aria-pressed', b.dataset.avatar===a?'true':'false')); };
  picks.forEach(b=>b.addEventListener('click',()=>setAvatar(b.dataset.avatar)));
  setAvatar(avatar);
  const bestEl=$('menuBest'); if (bestEl && best>0) bestEl.textContent = `🏆 Aapka best: ${best}`;

  // ---------- Fullscreen ----------
  const fsBtn = $('fs');
  if (!(wrap.requestFullscreen || wrap.webkitRequestFullscreen)) fsBtn.style.display='none';
  fsBtn.addEventListener('click', e => {
    e.stopPropagation();
    try {
      if (document.fullscreenElement || document.webkitFullscreenElement) (document.exitFullscreen || document.webkitExitFullscreen).call(document);
      else (wrap.requestFullscreen || wrap.webkitRequestFullscreen).call(wrap);
    } catch(err){}
  });
  ['fullscreenchange','webkitfullscreenchange'].forEach(ev => document.addEventListener(ev, () => setTimeout(resize, 60)));

  // ---------- Input ----------
  function setTarget(clientX){ if(!player) return; const r=cv.getBoundingClientRect(); player.tx = clientX - r.left; }
  cv.addEventListener('pointerdown', e => { setTarget(e.clientX); });
  cv.addEventListener('pointermove', e => { if (e.pointerType==='mouse' || e.buttons || e.pressure>0) setTarget(e.clientX); });
  cv.addEventListener('touchmove', e => { e.preventDefault(); if(e.touches[0]) setTarget(e.touches[0].clientX); }, {passive:false});
  window.addEventListener('keydown', e => {
    if (e.key==='ArrowLeft'||e.key==='a'||e.key==='A') keys.left=true;
    if (e.key==='ArrowRight'||e.key==='d'||e.key==='D') keys.right=true;
    if ((state==='play'||state==='banner') && (e.key==='ArrowLeft'||e.key==='ArrowRight')) e.preventDefault();
    if (e.key==='p'||e.key==='P'||e.key==='Escape'){ if(state==='pause') resume(); else pause(); }
  });
  window.addEventListener('keyup', e => {
    if (e.key==='ArrowLeft'||e.key==='a'||e.key==='A') keys.left=false;
    if (e.key==='ArrowRight'||e.key==='d'||e.key==='D') keys.right=false;
  });

  window.addEventListener('resize', resize);
  try { new ResizeObserver(() => resize()).observe(wrap); } catch(e){}
  resize(); makeDots(); showOnly('startScreen');
  requestAnimationFrame(ts => { last=ts; loop(ts); });
})();

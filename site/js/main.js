/* Karunya Digital — interactions. No dependencies. */
(function () {
  "use strict";
  var doc = document.documentElement;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var WA = "916386492334";

  /* header */
  var header = document.querySelector(".site-header");
  function onScrollHeader() { if (header) header.classList.toggle("solid", window.scrollY > 40); }
  onScrollHeader();
  window.addEventListener("scroll", onScrollHeader, { passive: true });

  /* mobile menu */
  var btn = document.querySelector(".menu-btn");
  if (btn) btn.addEventListener("click", function () {
    var open = document.body.classList.toggle("menu-open");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
  });
  document.querySelectorAll(".nav a").forEach(function (a) {
    a.addEventListener("click", function () { document.body.classList.remove("menu-open"); });
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && document.body.classList.contains("menu-open")) {
      document.body.classList.remove("menu-open"); if (btn) { btn.setAttribute("aria-expanded", "false"); btn.focus(); }
    }
  });

  /* hero parallax (mouse + scroll), runs only while the hero is on screen */
  var scene = document.querySelector(".scene");
  if (scene && !reduce) {
    var layers = [["#far", 6, .10], ["#mid", 12, .05], ["#near", 22, 0], ["#moon", 4, .16], ["#pin", 12, .05]]
      .map(function (l) { return { el: scene.querySelector(l[0]), mx: l[1], sy: l[2] }; })
      .filter(function (l) { return l.el; });
    var tx = 0, cx = 0, heroOn = true, ticking = false;
    function frame() {
      ticking = false;
      if (!heroOn) return;
      cx += (tx - cx) * .08;
      var sy = Math.min(window.scrollY, 900);
      layers.forEach(function (l) { l.el.style.transform = "translate(" + (-cx * l.mx).toFixed(2) + "px," + (sy * l.sy).toFixed(2) + "px)"; });
      if (Math.abs(tx - cx) > .002) kick();
    }
    function kick() { if (!ticking) { ticking = true; requestAnimationFrame(frame); } }
    window.addEventListener("pointermove", function (e) { tx = (e.clientX / window.innerWidth - .5) * 2; kick(); }, { passive: true });
    window.addEventListener("scroll", kick, { passive: true });
    if ("IntersectionObserver" in window) new IntersectionObserver(function (en) { heroOn = en[0].isIntersecting; if (heroOn) kick(); }).observe(scene);
    kick();
  }

  /* reveal + sequences */
  var io = "IntersectionObserver" in window ? new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (!en.isIntersecting) return;
      var el = en.target;
      io.unobserve(el);
      if (el.classList.contains("talk-row")) {
        var parts = el.querySelectorAll(".pre");
        parts.forEach(function (p, i) { setTimeout(function () { p.classList.add("in"); p.classList.remove("pre"); }, reduce ? 0 : i * 260); });
      } else if (el.hasAttribute("data-count")) {
        countUp(el);
      } else {
        el.classList.add("in");
      }
    });
  }, { threshold: .25, rootMargin: "0px 0px -8% 0px" }) : null;

  document.querySelectorAll(".rv,.talk-row,.lotus,[data-count]").forEach(function (el) {
    if (io) io.observe(el); else el.classList.add("in");
  });

  function countUp(el) {
    var end = parseFloat(el.getAttribute("data-count"));
    var dec = (el.getAttribute("data-count").split(".")[1] || "").length;
    var suf = el.getAttribute("data-suffix") || "";
    if (reduce) { el.textContent = end.toFixed(dec) + suf; return; }
    var t0 = null, dur = 1600;
    function step(t) {
      if (!t0) t0 = t;
      var k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 3);
      el.textContent = (end * e).toFixed(dec) + suf;
      if (k < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  /* story: sticky phone follows the chapters */
  var phone = document.querySelector("[data-phone]");
  var chapters = document.querySelectorAll("[data-step]");
  if (phone && chapters.length && "IntersectionObserver" in window) {
    var typed = false;
    var stIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var s = en.target.getAttribute("data-step");
        phone.setAttribute("data-state", s);
        chapters.forEach(function (c) { c.classList.toggle("active", c === en.target); });
        if (s === "1" && !typed) { typed = true; typeQuery(); }
        var v = phone.querySelector("video");
        if (v) { if (s === "3") safePlay(v); else v.pause(); }
      });
    }, { rootMargin: "-45% 0px -45% 0px" });
    chapters.forEach(function (c) { stIO.observe(c); });
  }
  function typeQuery() {
    var box = document.querySelector("[data-type]");
    if (!box) return;
    var text = box.getAttribute("data-type");
    if (reduce) { box.textContent = text; return; }
    var i = 0; box.textContent = "";
    (function t() { box.textContent = text.slice(0, ++i); if (i < text.length) setTimeout(t, 70 + Math.random() * 60); })();
  }

  /* reels: play muted while visible; one sound at a time */
  function safePlay(v) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
  var reels = document.querySelectorAll("video[data-auto]");
  if ("IntersectionObserver" in window && !reduce) {
    var vIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var v = en.target;
        if (en.isIntersecting) { if (v.preload === "none") v.preload = "metadata"; safePlay(v); }
        else v.pause();
      });
    }, { threshold: .4 });
    reels.forEach(function (v) { vIO.observe(v); });
  }
  document.querySelectorAll("[data-sound]").forEach(function (b) {
    b.addEventListener("click", function () {
      var v = b.closest(".reel").querySelector("video");
      var willUnmute = v.muted;
      document.querySelectorAll(".reel video").forEach(function (o) { o.muted = true; });
      document.querySelectorAll("[data-sound]").forEach(function (o) { o.setAttribute("aria-pressed", "false"); o.querySelector("span").textContent = "Sound on"; });
      if (willUnmute) {
        v.muted = false; v.currentTime = v.currentTime; safePlay(v);
        b.setAttribute("aria-pressed", "true"); b.querySelector("span").textContent = "Sound off";
      }
    });
  });

  /* process road: rickshaw follows scroll */
  var proc = document.querySelector(".process");
  if (proc) {
    var onP = function () {
      var r = proc.getBoundingClientRect(), vh = window.innerHeight;
      var p = (vh * .78 - r.top) / (r.height + vh * .3);
      proc.style.setProperty("--p", Math.max(0, Math.min(1, p)).toFixed(3));
    };
    onP(); window.addEventListener("scroll", onP, { passive: true }); window.addEventListener("resize", onP);
  }

  /* floating WhatsApp label peek */
  var wf = document.querySelector(".wa-float");
  if (wf && !reduce) { setTimeout(function () { wf.classList.add("show"); }, 3500); setTimeout(function () { wf.classList.remove("show"); }, 8500); }

  /* contact form -> WhatsApp message */
  var form = document.querySelector("#wa-form");
  if (form) form.addEventListener("submit", function (e) {
    e.preventDefault();
    var f = new FormData(form);
    var name = (f.get("name") || "").toString().trim();
    var err = form.querySelector(".err");
    if (!name) { err.textContent = "Please add your name so we know who you are."; form.querySelector("#f-name").focus(); return; }
    err.textContent = "";
    var needs = f.getAll("need").join(", ");
    var lines = ["Hello Karunya Digital,", "I'm " + name + (f.get("spec") ? " (" + f.get("spec") + ")" : "") + (f.get("city") ? ", from " + f.get("city") : "") + "."];
    if (needs) lines.push("I need: " + needs + ".");
    if ((f.get("msg") || "").toString().trim()) lines.push(f.get("msg").toString().trim());
    lines.push("Please let me know a good time to call.");
    window.open("https://wa.me/" + WA + "?text=" + encodeURIComponent(lines.join("\n")), "_blank", "noopener");
  });

  /* specialties dropdown */
  document.querySelectorAll(".dd").forEach(function (dd) {
    var b = dd.querySelector(".dd-btn");
    b.addEventListener("click", function (e) { e.stopPropagation(); var o = dd.classList.toggle("open"); b.setAttribute("aria-expanded", o ? "true" : "false"); });
    document.addEventListener("click", function (e) { if (!dd.contains(e.target)) { dd.classList.remove("open"); b.setAttribute("aria-expanded", "false"); } });
  });

  /* reel tabs by specialty */
  document.querySelectorAll(".tabs").forEach(function (tabs) {
    var strip = tabs.closest("section").querySelector("[data-tabbed]");
    tabs.querySelectorAll("button").forEach(function (t) {
      t.addEventListener("click", function () {
        tabs.querySelectorAll("button").forEach(function (o) { o.setAttribute("aria-selected", o === t ? "true" : "false"); });
        var k = t.getAttribute("data-tab");
        strip.querySelectorAll(".rc").forEach(function (c) { c.classList.toggle("hide", k !== "all" && c.getAttribute("data-spec") !== k); });
        strip.scrollTo({ left: 0, behavior: reduce ? "auto" : "smooth" });
      });
    });
  });

  /* Karunya Originals: episode player (loads video only on demand) */
  document.querySelectorAll(".originals").forEach(function (sec) {
    var v = sec.querySelector("[data-og-video]"), screen = sec.querySelector(".og-screen");
    var playBtn = sec.querySelector("[data-og-play]"), now = sec.querySelector(".og-now");
    function play() { v.controls = true; screen.classList.add("playing"); v.muted = false; safePlay(v); }
    playBtn.addEventListener("click", play);
    v.addEventListener("pause", function () { if (v.currentTime < 0.2) screen.classList.remove("playing"); });
    sec.querySelectorAll(".og-thumb").forEach(function (t) {
      t.addEventListener("click", function () {
        sec.querySelectorAll(".og-thumb").forEach(function (o) { o.classList.toggle("on", o === t); o.setAttribute("aria-pressed", o === t ? "true" : "false"); });
        now.classList.add("swap");
        setTimeout(function () {
          sec.querySelector("[data-og-ep]").textContent = t.dataset.ep;
          sec.querySelector("[data-og-title]").textContent = t.dataset.title;
          sec.querySelector("[data-og-desc]").textContent = t.dataset.desc;
          now.classList.remove("swap");
        }, 220);
        v.pause(); v.poster = t.dataset.poster; v.src = t.dataset.video; play();
      });
    });
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (en) { en.forEach(function (e) { if (!e.isIntersecting && !v.paused) v.pause(); }); }, { threshold: 0.1 }).observe(sec);
    }
  });

  /* cursor: native pointer + a small dot with one smooth trail (fine pointers only) */
  if (!reduce && window.matchMedia("(pointer:fine)").matches) {
    var dot = document.createElement("div"); dot.className = "cur-dot"; dot.setAttribute("aria-hidden", "true");
    var cv = document.createElement("canvas"); cv.className = "trail"; cv.setAttribute("aria-hidden", "true");
    document.body.appendChild(cv); document.body.appendChild(dot);
    var ctx = cv.getContext("2d"), dpr = Math.min(window.devicePixelRatio || 1, 2);
    var DARK = ".hero,.dark,.cta-band,.page-hero,.site-footer,.a-hero,.spec-hero,.ghat-cap,.founder,.bridge-sec,.pricing";
    var mx = -100, my = -100, hx = -100, hy = -100, pts = [], light = false, raf = 0, lastT = null;
    function size() { cv.width = innerWidth * dpr; cv.height = innerHeight * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); }
    size(); window.addEventListener("resize", size);
    window.addEventListener("pointermove", function (e) {
      mx = e.clientX; my = e.clientY;
      if (hx < 0) { hx = mx; hy = my; }
      if (e.target !== lastT) { lastT = e.target; light = !!(e.target.closest && e.target.closest(DARK)); dot.classList.toggle("lt", light); }
      document.documentElement.classList.add("cur-on");
      if (!raf) raf = requestAnimationFrame(loop);
    }, { passive: true });
    document.addEventListener("pointerleave", function () { document.documentElement.classList.remove("cur-on"); });
    function loop() {
      hx += (mx - hx) * 0.35; hy += (my - hy) * 0.35;
      dot.style.transform = "translate(" + hx.toFixed(1) + "px," + hy.toFixed(1) + "px)";
      pts.unshift({ x: hx, y: hy }); if (pts.length > 22) pts.pop();
      ctx.clearRect(0, 0, innerWidth, innerHeight);
      if (pts.length > 2) {
        var c = light ? "209,255,66" : "2,81,176";
        for (var i = 1; i < pts.length - 1; i++) {
          var t = 1 - i / pts.length, p0 = pts[i - 1], p1 = pts[i], p2 = pts[i + 1];
          ctx.strokeStyle = "rgba(" + c + "," + (t * 0.55).toFixed(3) + ")";
          ctx.lineWidth = 0.5 + t * 3.2; ctx.lineCap = "round";
          ctx.beginPath();
          ctx.moveTo((p0.x + p1.x) / 2, (p0.y + p1.y) / 2);
          ctx.quadraticCurveTo(p1.x, p1.y, (p1.x + p2.x) / 2, (p1.y + p2.y) / 2);
          ctx.stroke();
        }
      }
      var moving = Math.abs(mx - hx) + Math.abs(my - hy) > 0.2 || Math.abs(pts[0].x - pts[pts.length - 1].x) + Math.abs(pts[0].y - pts[pts.length - 1].y) > 0.5;
      raf = moving ? requestAnimationFrame(loop) : 0;
      if (!moving) ctx.clearRect(0, 0, innerWidth, innerHeight);
    }
  }

  /* sale bar: live countdown + dismiss-for-session */
  var saleBar = document.getElementById("sale-bar");
  if (saleBar) {
    var saleClosed = false;
    try { saleClosed = sessionStorage.getItem("kd-sale") === "1"; } catch (e) {}
    if (saleClosed) document.body.classList.add("sale-closed");
    var saleCd = document.getElementById("sale-cd");
    if (saleCd) {
      var target = new Date(saleCd.getAttribute("data-countdown")).getTime();
      var dEl = saleCd.querySelector("[data-cd-d]"), hEl = saleCd.querySelector("[data-cd-h]"),
          mEl = saleCd.querySelector("[data-cd-m]"), sEl = saleCd.querySelector("[data-cd-s]");
      function pad(n) { return n < 10 ? "0" + n : "" + n; }
      function tickCd() {
        var diff = target - Date.now();
        if (diff <= 0) { saleBar.hidden = true; return; }
        var s = Math.floor(diff / 1000);
        var d = Math.floor(s / 86400); s -= d * 86400;
        var h = Math.floor(s / 3600); s -= h * 3600;
        var m = Math.floor(s / 60); s -= m * 60;
        if (dEl) dEl.textContent = pad(d); if (hEl) hEl.textContent = pad(h);
        if (mEl) mEl.textContent = pad(m); if (sEl) sEl.textContent = pad(s);
      }
      tickCd();
      setInterval(tickCd, 1000);
    }
    var saleX = saleBar.querySelector("[data-sale-close]");
    if (saleX) saleX.addEventListener("click", function () {
      document.body.classList.add("sale-closed");
      try { sessionStorage.setItem("kd-sale", "1"); } catch (e) {}
    });
  }

  /* free check popup: after 10 seconds on the site, once per session */
  var pop = document.getElementById("fc-pop");
  if (pop && !/audit\.html/.test(location.pathname)) {
    var seen = false;
    try { seen = sessionStorage.getItem("kd-pop") === "1"; } catch (e) {}
    function closePop() { pop.hidden = true; pop.classList.remove("show"); try { sessionStorage.setItem("kd-pop", "1"); } catch (e) {} }
    if (!seen) setTimeout(function () { if (document.body.classList.contains("menu-open")) return; pop.hidden = false; pop.classList.add("show"); try { sessionStorage.setItem("kd-pop", "1"); } catch (e) {} }, 10000);
    pop.querySelectorAll("[data-pop-close]").forEach(function (x) { x.addEventListener("click", closePop); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && !pop.hidden) closePop(); });
  }

  /* footer: live Varanasi time + office status, back to top */
  var clock = document.querySelector("[data-clock]");
  if (clock) {
    var live = clock.closest(".f-live"), st = document.querySelector("[data-status]");
    var tick = function () {
      var now = new Date(), ist = new Date(now.getTime() + (now.getTimezoneOffset() + 330) * 60000);
      var h = ist.getHours(), m = ist.getMinutes(), day = ist.getDay();
      clock.textContent = (h % 12 || 12) + ":" + String(m).padStart(2, "0") + (h < 12 ? " am" : " pm");
      st.textContent = "WhatsApp us anytime";
    };
    tick(); setInterval(tick, 30000);
  }
  document.querySelectorAll("[data-top]").forEach(function (b) { b.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" }); }); });

  /* Free Google + Instagram check: lead first, then questions, then score */
  var af = document.getElementById("audit");
  if (af) {
    var lead = {};
    function sendLead(extra) {
      var body = new URLSearchParams();
      body.append("form-name", "free-check");
      Object.keys(lead).forEach(function (k) { body.append(k, lead[k]); });
      Object.keys(extra).forEach(function (k) { body.append(k, extra[k]); });
      return fetch("/", { method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" }, body: body.toString() }).catch(function () {});
    }
    var sf = document.getElementById("start");
    sf.addEventListener("submit", function (e) {
      e.preventDefault();
      var fd = new FormData(sf), se = sf.querySelector(".s-err");
      var name = (fd.get("name") || "").trim(), phone = (fd.get("phone") || "").replace(/\D/g, "").slice(-10);
      if (!name) { se.textContent = "Please add your name."; sf.querySelector("#s-name").focus(); return; }
      if (phone.length < 10) { se.textContent = "Please add a valid 10-digit WhatsApp number."; sf.querySelector("#s-phone").focus(); return; }
      se.textContent = "";
      lead = { name: name, phone: phone, speciality: (fd.get("speciality") || "").toString(), city: (fd.get("city") || "").toString().trim() };
      sendLead({ stage: "started" });
      var q = document.getElementById("questions"); q.hidden = false;
      q.scrollIntoView({ behavior: reduce ? "auto" : "smooth" });
      setTimeout(function () { var f = q.querySelector("input"); if (f) f.focus({ preventScroll: true }); }, 500);
    });
    var qs = af.querySelectorAll(".aq");
    var arc = document.querySelector(".g-arc"), scoreEl = document.querySelector("[data-score]");
    var levelEl = document.querySelector("[data-level]"), ansEl = document.querySelector("[data-answered]");
    var shown = 0;
    function calc() {
      var g = 0, i = 0, n = 0, items = [];
      qs.forEach(function (f) {
        var c = f.querySelector("input:checked"), nm = f.querySelector("input").name;
        if (c) { n++; var v = +c.value; if (nm[0] === "g") g += v; else i += v; items.push({ q: f.querySelector("legend").textContent, a: c.dataset.label, v: v, tip: f.dataset.tip }); }
        f.classList.toggle("done", !!c);
      });
      return { g: g, i: i, total: g + i, n: n, items: items };
    }
    function level(t) { return t >= 90 ? "Excellent. You're ahead of most clinics." : t >= 70 ? "Strong. A few fixes away from the top." : t >= 40 ? "A good start, with clear gaps." : "Your clinic is hard to find online."; }
    function animateTo(t) {
      var from = shown, t0 = null;
      function st(ts) { if (!t0) t0 = ts; var k = Math.min(1, (ts - t0) / (reduce ? 1 : 700)); var v = Math.round(from + (t - from) * (1 - Math.pow(1 - k, 3))); scoreEl.textContent = v; arc.style.strokeDashoffset = 100 - v; if (k < 1) requestAnimationFrame(st); else shown = t; }
      requestAnimationFrame(st);
    }
    function update() {
      var r = calc();
      ansEl.textContent = r.n;
      document.querySelector('[data-bar="g"]').style.width = (r.g * 2) + "%";
      document.querySelector('[data-bar="i"]').style.width = (r.i * 2) + "%";
      document.querySelector('[data-sub="g"]').textContent = r.g + "/50";
      document.querySelector('[data-sub="i"]').textContent = r.i + "/50";
      animateTo(r.total);
      levelEl.textContent = r.n < 10 ? "Keep going: " + (10 - r.n) + " questions left" : level(r.total);
      if (r.n === 10) af.querySelector(".a-err").textContent = "";
      return r;
    }
    af.addEventListener("change", update);
    af.addEventListener("submit", function (e) {
      e.preventDefault();
      var r = update(), err = af.querySelector(".a-err");
      if (r.n < 10) {
        err.textContent = "Please answer all 10 questions to see your full score.";
        var miss = Array.prototype.find.call(qs, function (f) { return !f.querySelector("input:checked"); });
        if (miss) { miss.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "center" }); miss.querySelector("input").focus({ preventScroll: true }); }
        return;
      }
      var fixes = r.items.slice().sort(function (a, b) { return a.v - b.v; }).filter(function (x) { return x.v < 10; }).slice(0, 3);
      var ol = document.querySelector("[data-fixes]"); ol.innerHTML = "";
      if (!fixes.length) { var li0 = document.createElement("li"); li0.innerHTML = "<b>You're doing everything right.</b><span>Next step: content that turns attention into appointments. Talk to us.</span>"; ol.appendChild(li0); }
      fixes.forEach(function (x) { var li = document.createElement("li"), b = document.createElement("b"), a = document.createElement("em"), sp = document.createElement("span"); b.textContent = x.q; a.textContent = "Your answer: " + x.a; sp.textContent = x.tip; li.appendChild(b); li.appendChild(a); li.appendChild(sp); ol.appendChild(li); });
      document.querySelector("[data-greet]").textContent = lead.name || "Doctor";
      var msg = "Hello Karunya Digital, I'm " + (lead.name || "a doctor") + (lead.speciality ? " (" + lead.speciality + (lead.city ? ", " + lead.city : "") + ")" : "") + ". My free check score is " + r.total + "/100 (Google " + r.g + "/50, Instagram " + r.i + "/50). Please share my detailed plan.";
      document.querySelector("[data-wa-now]").href = "https://wa.me/" + WA + "?text=" + encodeURIComponent(msg);
      sendLead({ stage: "completed", score: r.total, google_score: r.g, instagram_score: r.i, answers: r.items.map(function (x) { return x.q + " " + x.a + " (" + x.v + "/10)"; }).join("\n") });
      var res = document.getElementById("result"); res.hidden = false;
      res.scrollIntoView({ behavior: reduce ? "auto" : "smooth" });
    });
  }

  /* year */
  document.querySelectorAll("[data-year]").forEach(function (y) { y.textContent = new Date().getFullYear(); });
})();

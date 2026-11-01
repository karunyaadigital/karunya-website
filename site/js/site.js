/* Karunya Digital v3 — interactions. No dependencies, no custom cursor. */
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var WA = "916386492334";
  var hasIO = "IntersectionObserver" in window;

  /* header: glass after scroll, hide on scroll down, show on scroll up */
  var hd = document.querySelector(".hd"), lastY = 0;
  function onScroll() {
    var y = window.scrollY;
    if (hd) {
      hd.classList.toggle("solid", y > 24);
      hd.classList.toggle("hide", y > 400 && y > lastY && !document.body.classList.contains("menu-open"));
    }
    lastY = y;
  }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* mobile menu */
  var mb = document.querySelector(".menu");
  if (mb) mb.addEventListener("click", function () {
    var open = document.body.classList.toggle("menu-open");
    mb.setAttribute("aria-expanded", open ? "true" : "false");
    mb.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  });
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    if (document.body.classList.contains("menu-open")) { document.body.classList.remove("menu-open"); if (mb) { mb.setAttribute("aria-expanded", "false"); mb.focus(); } }
    var vm = document.getElementById("vm"); if (vm && !vm.hidden) closeVm();
  });

  /* specialties dropdown */
  document.querySelectorAll(".dd").forEach(function (dd) {
    var b = dd.querySelector(".dd-btn");
    b.addEventListener("click", function (e) { e.stopPropagation(); var o = dd.classList.toggle("open"); b.setAttribute("aria-expanded", o ? "true" : "false"); });
    document.addEventListener("click", function (e) { if (!dd.contains(e.target)) { dd.classList.remove("open"); b.setAttribute("aria-expanded", "false"); } });
  });

  /* reveal on scroll + big number count-up */
  function countUp(el) {
    var raw = el.textContent.trim(), end = parseFloat(raw.replace(/,/g, "")), dec = (raw.split(".")[1] || "").length, comma = raw.indexOf(",") > -1;
    if (isNaN(end) || reduce) return;
    var t0 = null, dur = 1800;
    function fmt(v) { var s = v.toFixed(dec); return comma ? Number(s).toLocaleString("en-IN") : s; }
    el.textContent = fmt(0);
    (function step(t) {
      if (!t0) t0 = t;
      var k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 4);
      el.textContent = fmt(end * e);
      if (k < 1) requestAnimationFrame(step); else el.textContent = raw;
    })(performance.now());
  }
  var rio = hasIO ? new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (!en.isIntersecting) return;
      rio.unobserve(en.target);
      en.target.classList.add("in");
      var n = en.target.querySelector(".bn-n span");
      if (n) countUp(n);
    });
  }, { threshold: 0.2, rootMargin: "0px 0px -6% 0px" }) : null;
  document.querySelectorAll("[data-r]").forEach(function (el, i) {
    if (rio) { el.style.setProperty("--i", i % 4); rio.observe(el); } else el.classList.add("in");
  });

  /* Manisha's call counter ticks up when it comes into view */
  document.querySelectorAll("[data-tick]").forEach(function (el) {
    if (!hasIO || reduce) return;
    var end = +el.dataset.tick;
    el.textContent = "0";
    new IntersectionObserver(function (en, o) {
      if (!en[0].isIntersecting) return; o.disconnect();
      var t0 = null;
      requestAnimationFrame(function st(t) {
        if (!t0) t0 = t;
        var k = Math.min(1, (t - t0) / 2200), v = Math.round(end * (1 - Math.pow(1 - k, 3)));
        el.textContent = v.toLocaleString("en-IN");
        if (k < 1) requestAnimationFrame(st);
      });
    }, { threshold: 0.5 }).observe(el);
  });

  /* pause the hero's looping motion when it is off screen */
  var canvas = document.querySelector(".canvas");
  if (canvas && hasIO) new IntersectionObserver(function (en) { canvas.classList.toggle("off", !en[0].isIntersecting); }).observe(canvas);

  /* horizontal rows: drag to scroll + arrow buttons */
  document.querySelectorAll("[data-drag]").forEach(function (row) {
    var down = false, sx = 0, sl = 0, moved = false;
    row.addEventListener("pointerdown", function (e) { if (e.pointerType !== "mouse") return; down = true; moved = false; sx = e.clientX; sl = row.scrollLeft; });
    window.addEventListener("pointermove", function (e) { if (!down) return; var d = e.clientX - sx; if (Math.abs(d) > 5) { moved = true; row.classList.add("dragging"); } row.scrollLeft = sl - d; });
    window.addEventListener("pointerup", function () { down = false; setTimeout(function () { row.classList.remove("dragging"); }, 0); });
    row.addEventListener("click", function (e) { if (moved) { e.preventDefault(); e.stopPropagation(); moved = false; } }, true);
  });
  document.querySelectorAll("[data-scroll]").forEach(function (b) {
    b.addEventListener("click", function () {
      var row = b.closest("section").querySelector("[data-scroller]");
      if (row) row.scrollBy({ left: (+b.dataset.scroll) * row.clientWidth * 0.8, behavior: reduce ? "auto" : "smooth" });
    });
  });

  /* reels: autoplay muted while visible; one sound at a time */
  function safePlay(v) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
  if (hasIO && !reduce) {
    var vio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var v = en.target;
        if (en.isIntersecting) { if (v.preload === "none") v.preload = "metadata"; safePlay(v); } else v.pause();
      });
    }, { threshold: 0.5 });
    document.querySelectorAll("video[data-auto]").forEach(function (v) { vio.observe(v); });
  }
  document.querySelectorAll("[data-sound]").forEach(function (b) {
    b.addEventListener("click", function () {
      var v = b.closest(".rc").querySelector("video"), unmute = v.muted;
      document.querySelectorAll(".rc video").forEach(function (o) { o.muted = true; });
      document.querySelectorAll("[data-sound]").forEach(function (o) { o.setAttribute("aria-pressed", "false"); o.querySelector("span").textContent = "Sound on"; });
      if (unmute) { v.muted = false; safePlay(v); b.setAttribute("aria-pressed", "true"); b.querySelector("span").textContent = "Sound off"; }
    });
  });

  /* Karunya Originals: modal player */
  var vm = document.getElementById("vm"), lastFocus = null;
  function closeVm() { var v = vm.querySelector("video"); v.pause(); v.removeAttribute("src"); v.load(); vm.hidden = true; document.body.classList.remove("vm-open"); if (lastFocus) lastFocus.focus(); }
  if (vm) {
    document.querySelectorAll("[data-play]").forEach(function (b) {
      b.addEventListener("click", function () {
        lastFocus = b;
        var v = vm.querySelector("video");
        v.poster = b.dataset.poster; v.src = b.dataset.play; v.setAttribute("aria-label", b.dataset.title);
        vm.hidden = false; document.body.classList.add("vm-open");
        vm.querySelector("[data-close]").focus({ preventScroll: true });
        safePlay(v);
      });
    });
    vm.addEventListener("click", function (e) { if (e.target === vm || e.target.closest("[data-close]")) closeVm(); });
  }

  /* contact form -> prepared WhatsApp message */
  var form = document.getElementById("wa-form");
  if (form) form.addEventListener("submit", function (e) {
    e.preventDefault();
    var f = new FormData(form), name = (f.get("name") || "").toString().trim(), err = form.querySelector(".err");
    if (!name) { err.textContent = "Please add your name."; form.querySelector("#f-name").focus(); return; }
    err.textContent = "";
    var needs = f.getAll("need").join(", "), spec = (f.get("spec") || "").toString().trim(), city = (f.get("city") || "").toString().trim();
    var lines = ["Hello Karunya Digital,", "I'm " + name + (spec ? " (" + spec + ")" : "") + (city ? " from " + city : "") + "."];
    if (needs) lines.push("I'm interested in: " + needs + ".");
    var m = (f.get("msg") || "").toString().trim(); if (m) lines.push(m);
    lines.push("When can we talk?");
    window.open("https://wa.me/" + WA + "?text=" + encodeURIComponent(lines.join("\n")), "_blank", "noopener");
  });

  /* free Google + Instagram check: lead first, then questions, then score */
  var af = document.getElementById("audit");
  if (af) {
    var lead = {};
    var sendLead = function (extra) {
      var body = new URLSearchParams();
      body.append("form-name", "free-check");
      Object.keys(lead).forEach(function (k) { body.append(k, lead[k]); });
      Object.keys(extra).forEach(function (k) { body.append(k, extra[k]); });
      return fetch("/", { method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" }, body: body.toString() }).catch(function () {});
    };
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
      setTimeout(function () { var i = q.querySelector("input"); if (i) i.focus({ preventScroll: true }); }, 500);
    });
    var qs = af.querySelectorAll(".aq"), arc = document.querySelector(".g-arc"), scoreEl = document.querySelector("[data-score]");
    var levelEl = document.querySelector("[data-level]"), ansEl = document.querySelector("[data-answered]"), shown = 0;
    var calc = function () {
      var g = 0, i = 0, n = 0, items = [];
      qs.forEach(function (f) {
        var c = f.querySelector("input:checked"), nm = f.querySelector("input").name;
        if (c) { n++; var v = +c.value; if (nm[0] === "g") g += v; else i += v; items.push({ q: f.querySelector("legend").textContent, a: c.dataset.label, v: v, tip: f.dataset.tip }); }
        f.classList.toggle("done", !!c);
      });
      return { g: g, i: i, total: g + i, n: n, items: items };
    };
    var level = function (t) { return t >= 90 ? "Excellent. You're ahead of most clinics." : t >= 70 ? "Strong. A few fixes away from the top." : t >= 40 ? "A good start, with clear gaps." : "Your clinic is hard to find online."; };
    var animateTo = function (t) {
      var from = shown, t0 = null;
      requestAnimationFrame(function st(ts) {
        if (!t0) t0 = ts;
        var k = Math.min(1, (ts - t0) / (reduce ? 1 : 700)), v = Math.round(from + (t - from) * (1 - Math.pow(1 - k, 3)));
        scoreEl.textContent = v; arc.style.strokeDashoffset = 100 - v;
        if (k < 1) requestAnimationFrame(st); else shown = t;
      });
    };
    var update = function () {
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
    };
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
      fixes.forEach(function (x) {
        var li = document.createElement("li"), b = document.createElement("b"), a = document.createElement("em"), sp = document.createElement("span");
        b.textContent = x.q; a.textContent = "Your answer: " + x.a; sp.textContent = x.tip;
        li.appendChild(b); li.appendChild(a); li.appendChild(sp); ol.appendChild(li);
      });
      document.querySelector("[data-greet]").textContent = lead.name || "Doctor";
      var msg = "Hello Karunya Digital, I'm " + (lead.name || "a doctor") + (lead.speciality ? " (" + lead.speciality + (lead.city ? ", " + lead.city : "") + ")" : "") + ". My free check score is " + r.total + "/100 (Google " + r.g + "/50, Instagram " + r.i + "/50). Please share my detailed plan.";
      document.querySelector("[data-wa-now]").href = "https://wa.me/" + WA + "?text=" + encodeURIComponent(msg);
      sendLead({ stage: "completed", score: r.total, google_score: r.g, instagram_score: r.i, answers: r.items.map(function (x) { return x.q + " " + x.a + " (" + x.v + "/10)"; }).join("\n") });
      var res = document.getElementById("result"); res.hidden = false;
      res.scrollIntoView({ behavior: reduce ? "auto" : "smooth" });
    });
  }

  /* brand motion band: words land when it scrolls in */
  document.querySelectorAll(".bm").forEach(function (el) {
    if (!hasIO) { el.classList.add("in"); return; }
    new IntersectionObserver(function (en, o) { if (en[0].isIntersecting) { el.classList.add("in"); o.disconnect(); } }, { threshold: 0.35 }).observe(el);
  });

  /* trail cursor: style changes per page and per section (fine pointers only, native cursor stays) */
  if (!reduce && window.matchMedia("(pointer:fine)").matches) {
    var cv = document.createElement("canvas"); cv.className = "trail"; cv.setAttribute("aria-hidden", "true");
    document.body.appendChild(cv);
    var ctx = cv.getContext("2d"), dpr = Math.min(window.devicePixelRatio || 1, 2), pts = [], running = false;
    var PAGE = { home: "ribbon", services: "dots", work: "spark", about: "comet", blog: "dots", contact: "ribbon", audit: "spark", "404": "spark" };
    var bodyKey = (document.body.className.match(/p-([\w-]+)/) || [])[1] || "home";
    var pageMode = PAGE[bodyKey] || (bodyKey.indexOf("blog-") === 0 ? "dots" : "comet");
    var DARK = ".canvas,.bm,.cta,.duo-c.blue,.pl.pop,.ct-wa,.a-card,.v-trust,.ph-stat";
    var mode = pageMode, col = "2,81,176";
    function size() { cv.width = innerWidth * dpr; cv.height = innerHeight * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); }
    size(); window.addEventListener("resize", size);
    var lastT = null;
    window.addEventListener("pointermove", function (e) {
      if (e.target !== lastT) {
        lastT = e.target;
        var sec = e.target.closest ? e.target.closest("[data-trail]") : null;
        mode = sec ? sec.dataset.trail : pageMode;
        col = (e.target.closest && e.target.closest(DARK)) ? "209,255,66" : "2,81,176";
      }
      pts.push({ x: e.clientX, y: e.clientY, life: 1, vx: (Math.random() - .5) * 1.4, vy: (Math.random() - .5) * 1.4 - .4, m: mode, c: col });
      if (pts.length > 40) pts.shift();
      if (!running) { running = true; requestAnimationFrame(draw); }
    }, { passive: true });
    function star(x, y, r) {
      ctx.beginPath();
      for (var i = 0; i < 8; i++) { var a = i * Math.PI / 4, rr = i % 2 ? r * .38 : r; ctx.lineTo(x + Math.cos(a) * rr, y + Math.sin(a) * rr); }
      ctx.closePath(); ctx.fill();
    }
    function draw() {
      ctx.clearRect(0, 0, innerWidth, innerHeight);
      for (var i = 0; i < pts.length; i++) {
        var p = pts[i], t = (i + 1) / pts.length, a = Math.max(0, p.life);
        ctx.fillStyle = ctx.strokeStyle = "rgba(" + p.c + "," + (a * .75).toFixed(3) + ")";
        if (p.m === "ribbon" && i > 0 && pts[i - 1].m === "ribbon") {
          var q = pts[i - 1]; ctx.lineWidth = 1 + t * 5 * a; ctx.lineCap = "round";
          ctx.beginPath(); ctx.moveTo(q.x, q.y); ctx.lineTo(p.x, p.y); ctx.stroke();
        } else if (p.m === "dots") {
          p.x += p.vx * .6; p.y += p.vy * .6;
          ctx.beginPath(); ctx.arc(p.x, p.y, 1.5 + 3 * a, 0, 6.283); ctx.fill();
        } else if (p.m === "spark") {
          p.x += p.vx; p.y += p.vy;
          star(p.x, p.y, 2 + 6 * a * t);
        } else if (p.m === "comet") {
          ctx.beginPath(); ctx.arc(p.x, p.y, (1 + 7 * t) * a, 0, 6.283); ctx.fill();
        }
        p.life -= p.m === "ribbon" ? .07 : .045;
      }
      pts = pts.filter(function (p) { return p.life > 0; });
      if (pts.length) requestAnimationFrame(draw); else { running = false; ctx.clearRect(0, 0, innerWidth, innerHeight); }
    }
  }

  /* footer: live Varanasi time, year, back to top */
  var clock = document.querySelector("[data-clock]");
  if (clock) {
    var tick = function () {
      var now = new Date(), ist = new Date(now.getTime() + (now.getTimezoneOffset() + 330) * 60000), h = ist.getHours(), m = ist.getMinutes();
      clock.textContent = (h % 12 || 12) + ":" + String(m).padStart(2, "0") + (h < 12 ? " am" : " pm");
    };
    tick(); setInterval(tick, 30000);
  }
  document.querySelectorAll("[data-year]").forEach(function (y) { y.textContent = new Date().getFullYear(); });
  document.querySelectorAll("[data-top]").forEach(function (b) { b.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" }); }); });
})();

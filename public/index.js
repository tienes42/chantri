const dialog = document.getElementById('dialog');
const dialogTitle = document.getElementById('dialogTitle');
const dialogText = document.getElementById('dialogText');
const confirmDialog = document.getElementById('confirmDialog');
const skyLayer = document.getElementById('skyLayer');
const homeScene = document.getElementById('homeScene');
const islandsLayer = document.getElementById('islandsLayer');
const parallaxFar = document.getElementById('parallaxFar');
let nextAction = null;

function showDialog(title, message, label = 'Đã hiểu', action = null) {
  dialogTitle.textContent = title;
  dialogText.textContent = message;
  confirmDialog.textContent = label;
  nextAction = action;
  dialog.classList.add('open');
  dialog.setAttribute('aria-hidden', 'false');
}

function hideDialog() {
  dialog.classList.remove('open');
  dialog.setAttribute('aria-hidden', 'true');
  nextAction = null;
}

document.getElementById('closeDialog').addEventListener('click', hideDialog);
dialog.addEventListener('click', e => { if (e.target === dialog) hideDialog(); });
confirmDialog.addEventListener('click', () => {
  const action = nextAction;
  hideDialog();
  if (action) action();
});
document.addEventListener('keydown', e => { if (e.key === 'Escape') hideDialog(); });

// Điều hướng khi bấm vào các đảo môn học
document.querySelectorAll('.hit[data-page]').forEach(b => {
  b.addEventListener('click', () => {
    window.location.href = b.dataset.page;
  });
});

// Các nút thông tin & Popup
document.getElementById('centerHit').addEventListener('click', () =>
  showDialog('Chân Tri', 'Khám phá kiến thức qua tình huống thực tế và mini game để vận dụng điều đã học vào giải quyết vấn đề.')
);

document.getElementById('rankingButton').addEventListener('click', () => {
  if (window.HDLG && HDLG.configured) HDLG.showLeaderboard();
  else showDialog('Bảng xếp hạng', 'Cần cấu hình Firebase (file firebase-config.js) để xem bảng xếp hạng.');
});

// ===== Tài khoản Firebase + Sao (auth.js) =====
(function accountHud() {
  const $ = id => document.getElementById(id);
  const card = $('playerCard');
  card.style.cursor = 'pointer';
  card.addEventListener('click', () => { if (window.HDLG) HDLG.showAccount(); });

  function renderPlayer(d) {
    $('playerName').textContent = d.name || 'Tên người chơi';
    $('playerLevel').textContent = 'Lv.' + d.level;
    $('playerXpBar').style.width = d.inLevel + '%';
    $('playerXpText').textContent = d.inLevel + '/100';
    const av = $('playerAvatar');
    if (d.photo) {
      av.innerHTML = '';
      const img = document.createElement('img');
      img.src = d.photo; img.referrerPolicy = 'no-referrer'; img.alt = '';
      img.style.cssText = 'width:100%;height:100%;border-radius:50%;object-fit:cover';
      av.appendChild(img);
    } else if (d.name) {
      av.textContent = d.name.charAt(0).toUpperCase();
    }
  }

  let rankTimer = null;
  function renderRanking() {
    const panel = $('rankingPanel');
    if (!window.HDLG || !HDLG.configured || !HDLG.user) return;
    HDLG.getLeaderboard(5).then(list => {
      panel.querySelectorAll('.rank-row').forEach(r => r.remove());
      list.forEach((r, i) => {
        const row = document.createElement('div');
        row.className = 'rank-row' + (r.uid === HDLG.user.uid ? ' current' : '');
        const a = document.createElement('span'); a.textContent = i === 0 ? '👑' : String(i + 1);
        const b = document.createElement('b'); b.textContent = r.name;
        const c = document.createElement('strong'); c.textContent = r.xp;
        row.append(a, b, c); panel.appendChild(row);
      });
    });
  }

  window.addEventListener('hdlg:update', e => {
    renderPlayer(e.detail);
    clearTimeout(rankTimer); rankTimer = setTimeout(renderRanking, 800);
  });
  if (window.HDLG) HDLG.ready.then(() => { if (HDLG.user) renderRanking(); });
})();

document.querySelectorAll('.hit[data-popup]').forEach(b => {
  b.addEventListener('click', () => {
    const name = b.dataset.popup;
    const Q = window.HDLGQ;
    if (Q) {
      if (name === 'Cài đặt') return Q.openSettings();
      if (name === 'Phần thưởng') return Q.openRewards();
      if (name === 'Nhiệm vụ') return Q.openMissions();
      if (name === 'Thoát') return Q.openExit();
    }
    if (name === 'Thoát') {
      showDialog('Thoát', 'Bạn có muốn rời khỏi trang chủ không?', 'Rời trang', () => {
        window.location.href = 'about:blank';
      });
    } else {
      showDialog(name, `Khu vực ${name.toLowerCase()} sẽ được kết nối với dữ liệu người chơi ở bước phát triển tiếp theo.`);
    }
  });
});

/* ================= 1. GÁN TRỰC TIẾP SPRITE WEBP ĐÃ TÁCH NỀN SẴN (LOAD TỨC THÌ 0MS) ================= */
const birdFrames = {
  up: 'assets/sprites/props2_14.webp',
  down: 'assets/sprites/props2_15.webp'
};

function applyInstantSprites() {
  document.querySelectorAll('.island-center-art').forEach(el => {
    el.style.backgroundImage = 'url("assets/sprites/island-center.webp")';
  });
  document.querySelectorAll('.island-art').forEach(el => {
    el.style.backgroundImage = 'url("assets/sprites/island-subject.webp")';
  });

  const props1Map = [
    { idx: 0, selector: '.flask-left' },
    { idx: 1, selector: '.flask-right' },
    { idx: 2, selector: '.chem-boom, .spark, .lava' },
    { idx: 3, selector: '.chem-smoke' },
    { idx: 4, selector: '.ruler' },
    { idx: 5, selector: '.compass' },
    { idx: 6, selector: '.magnet' },
    { idx: 7, selector: '.apple' },
    { idx: 8, selector: '.book' },
    { idx: 9, selector: '.quill, .brush' },
    { idx: 10, selector: '.shoe' },
    { idx: 11, selector: '.ball' },
    { idx: 12, selector: '.palette' },
    { idx: 13, selector: '.globe' },
    { idx: 14, selector: '.volcano' },
    { idx: 15, selector: '.laptop' }
  ];

  const props2Map = [
    { idx: 0, selector: '.sprout, .bush-l, .bush-r' },
    { idx: 1, selector: '.flower, .rainbow' },
    { idx: 2, selector: '.butterfly, .bird-paper' },
    { idx: 3, selector: '.bug' },
    { idx: 4, selector: '.hammer' },
    { idx: 5, selector: '.chat-a' },
    { idx: 6, selector: '.chat-b' },
    { idx: 7, selector: '.music-fx' },
    { idx: 8, selector: '.sword-l, .sword-r' },
    { idx: 9, selector: '.crown' },
    { idx: 10, selector: '.crystal' },
    { idx: 11, selector: '.goal' },
    { idx: 12, selector: '.cloud-white' },
    { idx: 13, selector: '.cloud-gold' }
  ];

  props1Map.forEach(({ idx, selector }) => {
    const url = `assets/sprites/props1_${idx}.webp`;
    document.querySelectorAll(selector).forEach(el => {
      el.style.backgroundImage = `url("${url}")`;
    });
  });

  props2Map.forEach(({ idx, selector }) => {
    const url = `assets/sprites/props2_${idx}.webp`;
    document.querySelectorAll(selector).forEach(el => {
      el.style.backgroundImage = `url("${url}")`;
    });
  });
}

applyInstantSprites();

/* ================= 2. HIỆU ỨNG CAMERA PARALLAX KHI DI CHUỘT ================= */
homeScene.addEventListener('mousemove', e => {
  const x = (e.clientX / window.innerWidth - 0.5);
  const y = (e.clientY / window.innerHeight - 0.5);
  islandsLayer.style.transform = `translate(${x * -20}px, ${y * -14}px)`;
  if (parallaxFar) {
    parallaxFar.style.transform = `translate(${x * 24}px, ${y * 14}px) scale(1.04)`;
  }
});

/* ================= 3. HỆ THỐNG CANVAS 60FPS (SAO BĂNG & ĐOM ĐÓM BOKEH) ================= */
const canvas = document.getElementById('cinematicCanvas');
const ctx = canvas ? canvas.getContext('2d') : null;
let cw = 0, ch = 0;

function resizeCanvas() {
  if (!canvas) return;
  cw = canvas.width = window.innerWidth;
  ch = canvas.height = window.innerHeight;
}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();

const orbs = Array.from({ length: 28 }, () => ({
  x: Math.random() * window.innerWidth,
  y: Math.random() * window.innerHeight,
  r: Math.random() * 4 + 1.5,
  vy: -(Math.random() * 0.55 + 0.2),
  vx: (Math.random() - 0.5) * 0.35,
  hue: Math.random() > 0.45 ? '#fde047' : '#38bdf8',
  alpha: Math.random() * 0.65 + 0.25
}));

let shootingStar = null;
setInterval(() => {
  if (!document.hidden && Math.random() < 0.75) {
    shootingStar = {
      x: Math.random() * cw * 0.65 + cw * 0.2,
      y: Math.random() * ch * 0.25 + 20,
      vx: -9,
      vy: 4.5,
      len: 110,
      life: 1
    };
  }
}, 4500);

function renderCinematicCanvas() {
  if (!ctx) return;
  ctx.clearRect(0, 0, cw, ch);

  if (shootingStar) {
    const st = shootingStar;
    const grad = ctx.createLinearGradient(st.x, st.y, st.x - st.vx * 10, st.y - st.vy * 10);
    grad.addColorStop(0, `rgba(255, 250, 210, ${st.life})`);
    grad.addColorStop(1, 'rgba(56, 189, 248, 0)');
    ctx.strokeStyle = grad;
    ctx.lineWidth = 2.4;
    ctx.beginPath();
    ctx.moveTo(st.x, st.y);
    ctx.lineTo(st.x + st.len, st.y - st.len * 0.5);
    ctx.stroke();

    st.x += st.vx;
    st.y += st.vy;
    st.life -= 0.022;
    if (st.life <= 0) shootingStar = null;
  }

  orbs.forEach(o => {
    o.x += o.vx;
    o.y += o.vy;
    if (o.y < -20) {
      o.y = ch + 15;
      o.x = Math.random() * cw;
    }
    ctx.save();
    ctx.globalAlpha = o.alpha;
    ctx.shadowColor = o.hue;
    // shadowBlur removed for 60fps GPU speed
    ctx.fillStyle = o.hue;
    ctx.beginPath();
    ctx.arc(o.x, o.y, o.r, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  });

  requestAnimationFrame(renderCinematicCanvas);
}
renderCinematicCanvas();

/* ================= 4. ĐÀN CHIM VỖ CÁNH 2 FRAME ================= */
function spawnFlyingBirds() {
  if (!skyLayer || !birdFrames.up) return;

  const group = document.createElement('div');
  group.className = 'flying-bird-group';

  const isFlock = Math.random() < 0.65;
  group.innerHTML = isFlock
    ? `<div class="bird-sprite"></div><div class="bird-sprite small-mate"></div>`
    : `<div class="bird-sprite"></div>`;

  const sprites = group.querySelectorAll('.bird-sprite');
  let flap = false;
  sprites.forEach(s => { s.style.backgroundImage = `url("${birdFrames.up}")`; });

  const flapTimer = setInterval(() => {
    flap = !flap;
    const frame = flap ? birdFrames.down : birdFrames.up;
    sprites.forEach(s => { s.style.backgroundImage = `url("${frame}")`; });
  }, 220);

  const randomTop = Math.floor(Math.random() * 58) + 6;
  const duration = (Math.random() * 7 + 12).toFixed(1);

  group.style.top = `${randomTop}%`;
  group.style.animationDuration = `${duration}s`;

  skyLayer.appendChild(group);

  setTimeout(() => {
    clearInterval(flapTimer);
    group.remove();
  }, parseFloat(duration) * 1000 + 500);
}

setTimeout(spawnFlyingBirds, 1200);
setInterval(() => {
  if (!document.hidden) {
    spawnFlyingBirds();
  }
}, 5200);


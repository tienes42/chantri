/* Máy tính fx-880BTG Plus (ClassWiz CW) — bản mô phỏng cho HDLJ. Không phải phần mềm chính hãng Casio. */
(function () {
"use strict";
/* =====================================================================
   LÕI TÍNH TOÁN — số hữu tỉ chính xác (BigInt), căn thức, bội của π,
   bộ phân tích biểu thức hiển thị tự nhiên, định dạng kết quả kiểu Casio
   ===================================================================== */
class CalcErr extends Error { constructor(kind, msg) { super(msg || kind); this.kind = kind; } }
const ERR = (k, m) => { throw new CalcErr(k, m); };

/* ---------- 1. Số hữu tỉ ---------- */
const babs = x => (x < 0n ? -x : x);
function bgcd(a, b) { a = babs(a); b = babs(b); while (b) { const t = a % b; a = b; b = t; } return a; }
const blen = x => babs(x).toString().length;
class Q {
  constructor(n, d = 1n) {
    if (d === 0n) ERR("Math");
    if (d < 0n) { n = -n; d = -d; }
    const g = bgcd(n, d) || 1n; this.n = n / g; this.d = d / g;
  }
  static int(k) { return new Q(BigInt(k)); }
  static dec(str) { // "12.5E-3" → hữu tỉ chính xác
    const m = /^(\d*)(?:\.(\d*))?(?:E([+-]?\d+))?$/.exec(str); if (!m) ERR("Syntax");
    const ip = m[1] || "0", fp = m[2] || "", ex = parseInt(m[3] || "0", 10);
    if (Math.abs(ex) > 99) ERR("Math");
    let n = BigInt(ip + fp), d = 10n ** BigInt(fp.length);
    if (ex > 0) n *= 10n ** BigInt(ex); else if (ex < 0) d *= 10n ** BigInt(-ex);
    return new Q(n, d);
  }
  add(o) { return new Q(this.n * o.d + o.n * this.d, this.d * o.d); }
  sub(o) { return new Q(this.n * o.d - o.n * this.d, this.d * o.d); }
  mul(o) { return new Q(this.n * o.n, this.d * o.d); }
  div(o) { if (o.n === 0n) ERR("Math"); return new Q(this.n * o.d, this.d * o.n); }
  neg() { return new Q(-this.n, this.d); }
  get zero() { return this.n === 0n; }
  get isInt() { return this.d === 1n; }
  get sign() { return this.n > 0n ? 1 : this.n < 0n ? -1 : 0; }
  cmp(o) { const x = this.n * o.d - o.n * this.d; return x > 0n ? 1 : x < 0n ? -1 : 0; }
  num() {
    const a = blen(this.n), b = blen(this.d);
    if (a < 300 && b < 300) return Number(this.n) / Number(this.d);
    const sh = BigInt(Math.max(0, Math.max(a, b) - 280));
    return Number(this.n / 10n ** sh) / Number(this.d / 10n ** sh);
  }
  big() { return blen(this.n) > 60 || blen(this.d) > 60; }
}
const Q0 = Q.int(0), Q1 = Q.int(1);
function qFromFloat(x, maxDen = 1000, tol = 1e-12) { // nhận dạng phân số nhỏ
  if (!isFinite(x)) return null;
  let h1 = 1, h0 = 0, k1 = 0, k0 = 1, b = x;
  for (let i = 0; i < 30; i++) {
    const a = Math.floor(b), h = a * h1 + h0, k = a * k1 + k0;
    if (k > maxDen) break;
    h0 = h1; h1 = h; k0 = k1; k1 = k;
    if (Math.abs(x - h1 / k1) <= tol * Math.max(1, Math.abs(x))) return new Q(BigInt(h1), BigInt(k1));
    if (b - a < 1e-15) break; b = 1 / (b - a);
  }
  return null;
}

/* ---------- 2. Giá trị: q (hữu tỉ) · s (a+b√n) · p (q·π) · f (thực) · c (phức) ---------- */
const V = {
  q: q => (q.big() ? { k: "f", v: q.num() } : { k: "q", q }),
  f: v => { if (typeof v !== "number" || isNaN(v) || !isFinite(v)) ERR("Math"); return { k: "f", v }; },
  s: (a, b, n) => (b.zero ? V.q(a) : n === 1n ? V.q(a.add(b)) : a.big() || b.big() ? V.f(a.num() + b.num() * Math.sqrt(Number(n))) : { k: "s", a, b, n }),
  p: q => (q.zero ? V.q(Q0) : q.big() ? V.f(q.num() * Math.PI) : { k: "p", q }),
  c: (re, im) => { if (!isFinite(re) || !isFinite(im)) ERR("Math"); return Math.abs(im) < 1e-14 * Math.max(1, Math.abs(re)) ? { k: "f", v: re } : { k: "c", re, im }; },
  int: k => V.q(Q.int(k))
};
const isExact = x => x.k === "q" || x.k === "s" || x.k === "p";
function toNum(x) {
  switch (x.k) {
    case "q": return x.q.num();
    case "s": return x.a.num() + x.b.num() * Math.sqrt(Number(x.n));
    case "p": return x.q.num() * Math.PI;
    case "f": return x.v;
    case "c": if (Math.abs(x.im) < 1e-12) return x.re; ERR("Math");
    default: ERR("Math");
  }
}
const toC = x => (x.k === "c" ? [x.re, x.im] : [toNum(x), 0]);
const isZero = x => (x.k === "q" ? x.q.zero : x.k === "c" ? x.re === 0 && x.im === 0 : toNum(x) === 0);
const asQ = x => (x.k === "q" ? x.q : null);
function asInt(x, what) {
  const q = asQ(x); if (q && q.isInt) return q.n;
  if (x.k === "f" && Number.isInteger(x.v) && Math.abs(x.v) < 9e15) return BigInt(x.v);
  ERR("Math", what || "Cần số nguyên");
}

/* căn bậc hai của số nguyên: N = k²·m */
function splitSquare(N) {
  if (N < 0n) ERR("Math");
  if (N === 0n) return [0n, 1n];
  if (N > 10000000000n) { const r = bsqrt(N); return r * r === N ? [r, 1n] : null; }
  let n = Number(N), k = 1, m = 1;
  for (let p = 2; p * p <= n; p += p === 2 ? 1 : 2) {
    let e = 0; while (n % p === 0) { n /= p; e++; }
    k *= p ** Math.floor(e / 2); if (e % 2) m *= p;
  }
  m *= n; return [BigInt(k), BigInt(m)];
}
function bsqrt(N) { if (N < 2n) return N; let x = BigInt(Math.floor(Math.sqrt(Number(N)))); while (x * x > N) x--; while ((x + 1n) * (x + 1n) <= N) x++; return x; }
function bnroot(N, k) { // căn bậc k nguyên (nếu đúng), ngược lại null
  if (N < 0n) return null; if (N < 2n) return N;
  let x = BigInt(Math.round(Math.pow(Number(N), 1 / k)));
  for (const c of [x - 1n, x, x + 1n]) if (c >= 0n && c ** BigInt(k) === N) return c;
  return null;
}
function sqrtV(x, cplx) {
  if (x.k === "q") {
    if (x.q.sign < 0) { if (cplx) return V.c(0, Math.sqrt(-x.q.num())); ERR("Math"); }
    const sp = splitSquare(x.q.n * x.q.d);
    if (!sp) return V.f(Math.sqrt(x.q.num()));
    const [k, m] = sp; return V.s(Q0, new Q(k, x.q.d), m);
  }
  if (x.k === "c") { const [a, b] = toC(x), r = Math.hypot(a, b); return V.c(Math.sqrt((r + a) / 2), Math.sign(b || 1) * Math.sqrt((r - a) / 2)); }
  const v = toNum(x); if (v < 0) { if (cplx) return V.c(0, Math.sqrt(-v)); ERR("Math"); }
  return V.f(Math.sqrt(v));
}

/* ---------- 3. Phép toán ---------- */
function add(x, y) {
  if (x.k === "c" || y.k === "c") { const [a, b] = toC(x), [c, d] = toC(y); return V.c(a + c, b + d); }
  if (isExact(x) && isZero(x)) return y; if (isExact(y) && isZero(y)) return x;
  if (x.k === "q" && y.k === "q") return V.q(x.q.add(y.q));
  if (x.k === "q" && y.k === "s") return V.s(y.a.add(x.q), y.b, y.n);
  if (x.k === "s" && y.k === "q") return V.s(x.a.add(y.q), x.b, x.n);
  if (x.k === "s" && y.k === "s" && x.n === y.n) return V.s(x.a.add(y.a), x.b.add(y.b), x.n);
  if (x.k === "p" && y.k === "p") return V.p(x.q.add(y.q));
  return V.f(toNum(x) + toNum(y));
}
function neg(x) {
  switch (x.k) { case "q": return V.q(x.q.neg()); case "s": return V.s(x.a.neg(), x.b.neg(), x.n); case "p": return V.p(x.q.neg()); case "c": return V.c(-x.re, -x.im); default: return V.f(-x.v); }
}
const sub = (x, y) => add(x, neg(y));
function mul(x, y) {
  if (x.k === "c" || y.k === "c") { const [a, b] = toC(x), [c, d] = toC(y); return V.c(a * c - b * d, a * d + b * c); }
  if ((isExact(x) && isZero(x)) || (isExact(y) && isZero(y))) return V.int(0);
  if (y.k === "q") [x, y] = [y, x];
  if (x.k === "q") {
    if (y.k === "q") return V.q(x.q.mul(y.q));
    if (y.k === "s") return V.s(y.a.mul(x.q), y.b.mul(x.q), y.n);
    if (y.k === "p") return V.p(y.q.mul(x.q));
  }
  if (x.k === "s" && y.k === "s") {
    if (x.n === y.n) return V.s(x.a.mul(y.a).add(x.b.mul(y.b).mul(new Q(x.n))), x.a.mul(y.b).add(x.b.mul(y.a)), x.n);
    if (x.a.zero && y.a.zero) { const r = sqrtV(V.q(new Q(x.n * y.n))); return mul(V.q(x.b.mul(y.b)), r); }
  }
  return V.f(toNum(x) * toNum(y));
}
function inv(x) {
  if (isZero(x)) ERR("Math");
  switch (x.k) {
    case "q": return V.q(Q1.div(x.q));
    case "s": { const den = x.a.mul(x.a).sub(x.b.mul(x.b).mul(new Q(x.n))); if (den.zero) ERR("Math"); return V.s(x.a.div(den), x.b.neg().div(den), x.n); }
    case "c": { const m = x.re * x.re + x.im * x.im; return V.c(x.re / m, -x.im / m); }
    default: return V.f(1 / toNum(x));
  }
}
function div(x, y) {
  if (isZero(y)) ERR("Math");
  if (x.k === "p" && y.k === "p") return V.q(x.q.div(y.q));
  if (x.k === "p" && y.k === "q") return V.p(x.q.div(y.q));
  if (x.k === "q" && y.k === "p") return V.f(toNum(x) / toNum(y));
  if (x.k === "s" && y.k === "s" && x.n !== y.n && x.a.zero && y.a.zero) { // b1√n1 / (b2√n2)
    const r = sqrtV(V.q(new Q(x.n * y.n))); return mul(V.q(x.b.div(y.b.mul(new Q(y.n)))), r);
  }
  if (y.k === "q" || y.k === "s" || y.k === "c") return mul(x, inv(y));
  return V.f(toNum(x) / toNum(y));
}
function qpow(q, k) { // k: BigInt
  if (k === 0n) { if (q.zero) ERR("Math"); return Q1; }
  if (babs(k) > 4000n || (blen(q.n) + blen(q.d)) * Number(babs(k)) > 4000) return null;
  const e = babs(k), r = new Q(q.n ** e, q.d ** e); return k < 0n ? Q1.div(r) : r;
}
function pow(x, y, cplx) {
  if (x.k === "c" || y.k === "c") {
    const [a, b] = toC(x), [c, d] = toC(y);
    if (a === 0 && b === 0) return V.int(0);
    if (d === 0 && Number.isInteger(c) && Math.abs(c) <= 64) { let r = V.c(1, 0), base = V.c(a, b); for (let i = 0; i < Math.abs(c); i++) r = mul(r, base); return c < 0 ? inv(r) : r; }
    const lr = Math.log(Math.hypot(a, b)), th = Math.atan2(b, a), er = Math.exp(c * lr - d * th), et = d * lr + c * th;
    return V.c(er * Math.cos(et), er * Math.sin(et));
  }
  const yq = asQ(y);
  if (yq && yq.isInt) {
    const k = yq.n;
    if (x.k === "q") { const r = qpow(x.q, k); if (r) return V.q(r); }
    if (x.k === "s" && babs(k) <= 64n) { let r = V.int(1), b = x, e = babs(k); while (e) { if (e & 1n) r = mul(r, b); b = mul(b, b); e >>= 1n; } return k < 0n ? inv(r) : r; }
    if (x.k === "p" && babs(k) <= 3n && k !== 0n) return V.f(Math.pow(toNum(x), Number(k)));
  }
  if (yq && x.k === "q") { // x^(p/q)
    const den = Number(yq.d), nu = yq.n;
    if (den === 2 && x.q.sign >= 0) return pow(sqrtV(x), V.q(new Q(nu)));
    if (den <= 12) {
      const sgn = x.q.sign < 0 ? -1n : 1n;
      if (sgn < 0n && den % 2 === 0) { if (cplx) return pow(V.c(x.q.num(), 0), V.c(yq.num(), 0)); ERR("Math"); }
      const rn = bnroot(babs(x.q.n), den), rd = bnroot(x.q.d, den);
      if (rn !== null && rd !== null) { const base = new Q(sgn * rn, rd), r = qpow(base, nu); if (r) return V.q(r); }
      if (sgn < 0n) { const v = -Math.pow(-x.q.num(), yq.num()); return V.f(Number(nu) % 2 === 0 ? -v : v); }
    }
  }
  const a = toNum(x), b = toNum(y), r = Math.pow(a, b);
  if (isNaN(r)) { if (cplx && a < 0) return pow(V.c(a, 0), V.c(b, 0), true); ERR("Math"); }
  return V.f(r);
}
function cmpV(x, y) { const d = toNum(x) - toNum(y); return Math.abs(d) < 1e-13 * Math.max(1, Math.abs(toNum(x))) ? 0 : d > 0 ? 1 : -1; }

/* ---------- 4. Hàm số ---------- */
const SIN12 = [[0n, 1n, 1n], [1n, 2n, 1n], [1n, 2n, 3n], [1n, 1n, 1n], [1n, 2n, 3n], [1n, 2n, 1n], [0n, 1n, 1n], [-1n, 2n, 1n], [-1n, 2n, 3n], [-1n, 1n, 1n], [-1n, 2n, 3n], [-1n, 2n, 1n]]; // (b/d)√n
const SIN8 = [[0n, 1n, 1n], [1n, 2n, 2n], [1n, 1n, 1n], [1n, 2n, 2n], [0n, 1n, 1n], [-1n, 2n, 2n], [-1n, 1n, 1n], [-1n, 2n, 2n]];
function turnsOf(x, ang) { // góc → số vòng (hữu tỉ) nếu chính xác
  if (ang === "D" && x.k === "q") return x.q.div(Q.int(360));
  if (ang === "G" && x.k === "q") return x.q.div(Q.int(400));
  if (ang === "R" && x.k === "p") return x.q.div(Q.int(2));
  if (x.k === "q" && x.q.zero) return Q0;
  return null;
}
function exactSin(t) { // t: số vòng
  let f = t.sub(new Q(t.n >= 0n ? t.n / t.d : t.n / t.d - 1n)); // phần lẻ ∈ [0,1)
  if (f.sign < 0) f = f.add(Q1);
  for (const [N, T] of [[12n, SIN12], [8n, SIN8]]) {
    const k = f.mul(new Q(N)); if (k.isInt) { const [b, d, n] = T[Number(k.n)]; return V.s(Q0, new Q(b, d), n); }
  }
  return null;
}
const toRad = (v, ang) => (ang === "D" ? v * Math.PI / 180 : ang === "G" ? v * Math.PI / 200 : v);
const fromRad = (v, ang) => (ang === "D" ? v * 180 / Math.PI : ang === "G" ? v * 200 / Math.PI : v);
function trig(fn, x, ang) {
  if (x.k === "c") { const [a, b] = toC(x); if (fn === "sin") return V.c(Math.sin(a) * Math.cosh(b), Math.cos(a) * Math.sinh(b)); if (fn === "cos") return V.c(Math.cos(a) * Math.cosh(b), -Math.sin(a) * Math.sinh(b)); return div(trig("sin", x, ang), trig("cos", x, ang)); }
  const t = turnsOf(x, ang);
  if (t) {
    const s = exactSin(fn === "cos" ? t.add(new Q(1n, 4n)) : t);
    if (fn !== "tan" && s) return s;
    if (fn === "tan") { const a = exactSin(t), c = exactSin(t.add(new Q(1n, 4n))); if (a && c) { if (isZero(c)) ERR("Math"); return div(a, c); } }
  }
  const r = toRad(toNum(x), ang);
  if (Math.abs(r) > 1e10) ERR("Math");
  if (fn === "sin") return V.f(clean(Math.sin(r)));
  if (fn === "cos") return V.f(clean(Math.cos(r)));
  if (Math.abs(Math.cos(r)) < 1e-15) ERR("Math");
  return V.f(clean(Math.tan(r)));
}
const clean = v => (Math.abs(v) < 1e-15 ? 0 : v);
function atrig(fn, x, ang) {
  const v = toNum(x);
  if ((fn === "asin" || fn === "acos") && Math.abs(v) > 1 + 1e-15) ERR("Math");
  const r = fn === "asin" ? Math.asin(Math.max(-1, Math.min(1, v))) : fn === "acos" ? Math.acos(Math.max(-1, Math.min(1, v))) : Math.atan(v);
  if (isExact(x)) { // nhận dạng bội của π/12, π/8
    const t = r / Math.PI;
    for (const N of [12, 8]) { const k = Math.round(t * N); if (Math.abs(t * N - k) < 1e-11) { const q = new Q(BigInt(k), BigInt(N)); return ang === "R" ? V.p(q) : V.q(q.mul(Q.int(ang === "D" ? 180 : 200))); } }
  }
  return V.f(fromRad(r, ang));
}
function logV(base, x) { // log_base(x)
  const a = toNum(x), b = toNum(base);
  if (a <= 0 || b <= 0 || b === 1) ERR("Math");
  const r = Math.log(a) / Math.log(b);
  if (x.k === "q" && base.k === "q") {
    const g = qFromFloat(r, 12, 1e-10);
    if (g) { // kiểm tra chính xác: base^(g.n) == x^(g.d)
      const L = qpow(base.q, g.n), R = qpow(x.q, g.d);
      if (L && R && L.cmp(R) === 0) return V.q(g);
    }
  }
  return V.f(clean(r));
}
function factorial(x) {
  const n = asInt(x); if (n < 0n || n > 69n) ERR("Math"); let r = 1n; for (let i = 2n; i <= n; i++) r *= i; return V.q(new Q(r));
}
function nPr(n, r) { n = asInt(n); r = asInt(r); if (n < 0n || r < 0n || r > n || n >= 10000000000n) ERR("Math"); if (r > 100000n) ERR("Math"); let v = 1n; for (let i = 0n; i < r; i++) v *= n - i; return V.q(new Q(v)); }
function nCr(n, r) { n = asInt(n); r = asInt(r); if (n < 0n || r < 0n || r > n || n >= 10000000000n) ERR("Math"); if (r > n - r) r = n - r; if (r > 100000n) ERR("Math"); let v = 1n; for (let i = 1n; i <= r; i++) v = v * (n - r + i) / i; return V.q(new Q(v)); }
function absV(x) { if (x.k === "c") return V.f(Math.hypot(x.re, x.im)); return toNum(x) < 0 ? neg(x) : x; }
function roundTo(x, S) { // Rnd theo cài đặt hiển thị
  if (isExact(x) && x.k === "q" && x.q.isInt) return x;
  const v = toNum(x);
  if (S.fmt === "fix") return V.f(Number(v.toFixed(S.fmtN)));
  if (S.fmt === "sci") return V.f(Number(v.toPrecision(Math.max(1, S.fmtN))));
  return V.f(Number(v.toPrecision(10)));
}

/* ---------- 5. Bộ phân tích (items → cây biểu thức) ---------- */
/* item: {t:"c", v:"7"} ký tự · {t:"f", v:"sin"} hàm có ngoặc mở · {t:"frac"|"sqrt"|..., s:[[...],...]} khuôn */
const ATOM_FUN = { det: 1, Trn: 1, Identity: 1, dot: 2, angle: 2, UnitV: 1, sin: 1, cos: 1, tan: 1, asin: 1, acos: 1, atan: 1, sinh: 1, cosh: 1, tanh: 1, asinh: 1, acosh: 1, atanh: 1, ln: 1, log: 1, Abs: 1, GCD: 2, LCM: 2, Int: 1, Intg: 1, Rnd: 1, RanInt: 2, Pol: 2, Rec: 2, f: 1, g: 1, Conjg: 1, ReP: 1, ImP: 1, Arg: 1, Q: 1, P: 1, R: 1, t: 1, ceil: 1 };
function lex(items) {
  const out = [];
  for (let i = 0; i < items.length; i++) {
    const it = items[i];
    if (it.t !== "c") { out.push(it.t === "f" ? { k: "fn", v: it.v } : { k: "tpl", it }); continue; }
    const c = it.v;
    if (/^[0-9.]$/.test(c)) {
      let s = "";
      while (i < items.length && items[i].t === "c" && /^[0-9.]$/.test(items[i].v)) s += items[i++].v;
      if (i < items.length && items[i].t === "c" && items[i].v === "E") { // ×10ˣ
        s += "E"; i++;
        if (i < items.length && items[i].t === "c" && (items[i].v === "−" || items[i].v === "neg" || items[i].v === "+")) { s += items[i].v === "+" ? "" : "-"; i++; }
        let e = ""; while (i < items.length && items[i].t === "c" && /^[0-9]$/.test(items[i].v)) e += items[i++].v;
        if (!e) ERR("Syntax"); s += e;
      }
      i--;
      if ((s.match(/\./g) || []).length > 1 || s === ".") ERR("Syntax");
      out.push({ k: "num", v: s });
    } else if (c === "E") { // ×10ˣ đứng đầu = 1×10ˣ
      let s = "1E"; i++;
      if (i < items.length && items[i].t === "c" && (items[i].v === "−" || items[i].v === "neg")) { s += "-"; i++; }
      let e = ""; while (i < items.length && items[i].t === "c" && /^[0-9]$/.test(items[i].v)) e += items[i++].v;
      i--; if (!e) ERR("Syntax"); out.push({ k: "num", v: s + e });
    } else out.push({ k: "op", v: c });
  }
  return out;
}
const VARS = ["A", "B", "C", "D", "E", "F", "x", "y", "z", "M"];
const CONSTS = { "π": 1, "e": 1, "i": 1, "Ans": 1, "PreAns": 1, "Ran#": 1 };
["A", "B", "C", "D", "Ans"].forEach(k => { CONSTS["Mat" + k] = 1; CONSTS["Vct" + k] = 1; });
/* hằng số khoa học (CODATA 2018) */
const SCI = {
  c0: ["c<sub>0</sub>", "299792458", "Tốc độ ánh sáng (m/s)"], h: ["h", "6.62607015E-34", "Hằng số Planck (J·s)"],
  hbar: ["ħ", "1.054571817E-34", "Hằng số Planck rút gọn (J·s)"], G: ["G", "6.6743E-11", "Hằng số hấp dẫn (N·m²/kg²)"],
  g0: ["g<sub>n</sub>", "9.80665", "Gia tốc trọng trường chuẩn (m/s²)"], NA: ["N<sub>A</sub>", "6.02214076E23", "Số Avogadro (1/mol)"],
  kB: ["k", "1.380649E-23", "Hằng số Boltzmann (J/K)"], R0: ["R", "8.314462618", "Hằng số khí (J/(mol·K))"],
  qe: ["e", "1.602176634E-19", "Điện tích nguyên tố (C)"], me: ["m<sub>e</sub>", "9.1093837015E-31", "Khối lượng electron (kg)"],
  mp: ["m<sub>p</sub>", "1.67262192369E-27", "Khối lượng proton (kg)"], mn: ["m<sub>n</sub>", "1.67492749804E-27", "Khối lượng neutron (kg)"],
  u: ["u", "1.6605390666E-27", "Đơn vị khối lượng nguyên tử (kg)"], eps0: ["ε<sub>0</sub>", "8.8541878128E-12", "Hằng số điện môi chân không (F/m)"],
  mu0: ["μ<sub>0</sub>", "1.25663706212E-6", "Độ từ thẩm chân không (N/A²)"], Far: ["F", "96485.33212", "Hằng số Faraday (C/mol)"],
  atm: ["atm", "101325", "Áp suất khí quyển chuẩn (Pa)"], Vm: ["V<sub>m</sub>", "22.71095464", "Thể tích mol khí lý tưởng ở 0 °C, 1 bar (L/mol)"],
  sigma: ["σ", "5.670374419E-8", "Hằng số Stefan–Boltzmann (W/(m²·K⁴))"], a0: ["a<sub>0</sub>", "5.29177210903E-11", "Bán kính Bohr (m)"]
};
Object.keys(SCI).forEach(k => { CONSTS["k:" + k] = 1; });
/* đổi đơn vị (hậu tố) */
const CONV = {
  "in▸cm": ["in▸cm", v => v * 2.54], "cm▸in": ["cm▸in", v => v / 2.54], "ft▸m": ["ft▸m", v => v * 0.3048], "m▸ft": ["m▸ft", v => v / 0.3048],
  "mile▸km": ["mile▸km", v => v * 1.609344], "km▸mile": ["km▸mile", v => v / 1.609344], "n mile▸m": ["n mile▸m", v => v * 1852], "m▸n mile": ["m▸n mile", v => v / 1852],
  "lb▸kg": ["lb▸kg", v => v * 0.45359237], "kg▸lb": ["kg▸lb", v => v / 0.45359237], "oz▸g": ["oz▸g", v => v * 28.349523125], "g▸oz": ["g▸oz", v => v / 28.349523125],
  "°F▸°C": ["°F▸°C", v => (v - 32) * 5 / 9], "°C▸°F": ["°C▸°F", v => v * 9 / 5 + 32], "°C▸K": ["°C▸K", v => v + 273.15], "K▸°C": ["K▸°C", v => v - 273.15],
  "km/h▸m/s": ["km/h▸m/s", v => v / 3.6], "m/s▸km/h": ["m/s▸km/h", v => v * 3.6], "atm▸Pa": ["atm▸Pa", v => v * 101325], "Pa▸atm": ["Pa▸atm", v => v / 101325],
  "mmHg▸Pa": ["mmHg▸Pa", v => v * 133.322387415], "Pa▸mmHg": ["Pa▸mmHg", v => v / 133.322387415], "J▸cal": ["J▸cal", v => v / 4.184], "cal▸J": ["cal▸J", v => v * 4.184],
  "kWh▸J": ["kWh▸J", v => v * 3.6e6], "J▸kWh": ["J▸kWh", v => v / 3.6e6], "hp▸kW": ["hp▸kW", v => v * 0.745699872], "kW▸hp": ["kW▸hp", v => v / 0.745699872],
  "L▸m³": ["L▸m³", v => v / 1000], "m³▸L": ["m³▸L", v => v * 1000], "ha▸m²": ["ha▸m²", v => v * 10000], "m²▸ha": ["m²▸ha", v => v / 10000]
};
class Parser {
  constructor(tokens) { this.t = tokens; this.i = 0; }
  peek() { return this.t[this.i]; }
  isOp(v) { const p = this.peek(); return p && p.k === "op" && p.v === v; }
  eat(v) { if (this.isOp(v)) { this.i++; return true; } return false; }
  end() { return this.i >= this.t.length; }
  top() {
    const a = this.expr();
    if (this.isOp("=")) { this.i++; const b = this.expr(); if (!this.end()) ERR("Syntax"); return { t: "eq", a, b }; }
    if (this.isOp("÷R")) { this.i++; const b = this.expr(); if (!this.end()) ERR("Syntax"); return { t: "divr", a, b }; }
    if (!this.end()) ERR("Syntax");
    return a;
  }
  expr() {
    let a = this.term();
    for (;;) {
      if (this.eat("+")) a = { t: "bin", op: "+", a, b: this.term() };
      else if (this.eat("−")) a = { t: "bin", op: "-", a, b: this.term() };
      else return a;
    }
  }
  term() {
    let a = this.comb();
    for (;;) {
      if (this.eat("×")) a = { t: "bin", op: "*", a, b: this.comb() };
      else if (this.eat("÷")) a = { t: "bin", op: "/", a, b: this.comb() };
      else return a;
    }
  }
  comb() {
    let a = this.unary();
    for (;;) {
      if (this.eat("nPr")) a = { t: "fn", n: "nPr", args: [a, this.unary()] };
      else if (this.eat("nCr")) a = { t: "fn", n: "nCr", args: [a, this.unary()] };
      else if (this.eat("∠")) a = { t: "polar", a, b: this.unary() };
      else return a;
    }
  }
  unary() {
    if (this.eat("−") || this.eat("neg")) return { t: "neg", a: this.unary() };
    if (this.eat("+")) return this.unary();
    return this.implicit();
  }
  startsAtom() {
    const p = this.peek(); if (!p) return false;
    if (p.k === "num" || p.k === "fn") return true;
    if (p.k === "tpl") return p.it.t !== "pow";
    return p.v === "(" || VARS.includes(p.v) || p.v in CONSTS;
  }
  implicit() {
    let a = this.postfix();
    while (this.startsAtom()) a = { t: "bin", op: "*", a, b: this.postfix(), imp: true };
    return a;
  }
  postfix() {
    let a = this.atom();
    for (;;) {
      const p = this.peek(); if (!p) return a;
      if (p.k === "tpl" && p.it.t === "pow") { this.i++; a = { t: "pow", a, b: sub1(p.it.s[0]) }; }
      else if (this.eat("!")) a = { t: "fn", n: "fact", args: [a] };
      else if (this.eat("inv")) a = { t: "inv", a };
      else if (this.eat("%")) a = { t: "pct", a };
      else if (p.k === "op" && CONV[p.v]) { this.i++; a = { t: "conv", c: p.v, a }; }
      else if (this.isOp("°")) { // độ-phút-giây
        const parts = [a]; this.i++;
        while (this.peek() && this.peek().k === "num" && parts.length < 3) { parts.push(this.atom()); if (!this.eat("°")) break; }
        a = { t: "dms", parts };
      } else return a;
    }
  }
  args() {
    const out = [];
    if (this.eat(")")) return out;
    out.push(this.expr());
    while (this.eat(",")) out.push(this.expr());
    if (!this.eat(")") && !this.end()) ERR("Syntax");
    return out;
  }
  atom() {
    const p = this.peek(); if (!p) ERR("Syntax");
    this.i++;
    if (p.k === "num") return { t: "num", v: V.q(Q.dec(p.v)), s: p.v };
    if (p.k === "fn") {
      const args = this.args(), need = ATOM_FUN[p.v] || 1;
      if (args.length !== need) ERR("Syntax");
      return { t: "fn", n: p.v, args };
    }
    if (p.k === "tpl") return tplNode(p.it);
    if (p.v === "(") { const e = this.expr(); if (!this.eat(")") && !this.end()) ERR("Syntax"); return e; }
    if (VARS.includes(p.v)) return { t: "var", n: p.v };
    if (p.v in CONSTS) return { t: "const", n: p.v };
    if (p.v === "°" || p.v === "r" || p.v === "g") ERR("Syntax");
    ERR("Syntax");
  }
}
function sub1(items) { if (!items.length) ERR("Syntax"); const P = new Parser(lex(items)); const e = P.expr(); if (!P.end()) ERR("Syntax"); return e; }
function tplNode(it) {
  const s = it.s;
  switch (it.t) {
    case "frac": return { t: "bin", op: "/", a: sub1(s[0]), b: sub1(s[1]), frac: true };
    case "mixed": return { t: "mixed", w: sub1(s[0]), a: sub1(s[1]), b: sub1(s[2]) };
    case "sqrt": return { t: "fn", n: "sqrt", args: [sub1(s[0])] };
    case "cbrt": return { t: "root", n: { t: "num", v: V.int(3) }, a: sub1(s[0]) };
    case "root": return { t: "root", n: sub1(s[0]), a: sub1(s[1]) };
    case "log": return { t: "logb", b: sub1(s[0]), a: sub1(s[1]) };
    case "abs": return { t: "fn", n: "Abs", args: [sub1(s[0])] };
    case "deriv": return { t: "deriv", f: sub1(s[0]), at: sub1(s[1]) };
    case "integ": return { t: "integ", a: sub1(s[0]), b: sub1(s[1]), f: sub1(s[2]) };
    case "sum": return { t: "sum", a: sub1(s[0]), b: sub1(s[1]), f: sub1(s[2]) };
    case "prod": return { t: "prod", a: sub1(s[0]), b: sub1(s[1]), f: sub1(s[2]) };
    case "exp10": return { t: "pow", a: { t: "num", v: V.int(10) }, b: sub1(s[0]) };
    case "expe": return { t: "pow", a: { t: "const", n: "e" }, b: sub1(s[0]) };
    default: ERR("Syntax");
  }
}
function parseItems(items) { if (!items.length) ERR("Syntax"); return new Parser(lex(items)).top(); }

/* ---------- 6. Tính giá trị ---------- */
function evalNode(n, env) {
  const S = env.S, A = env.ang || S.ang, cx = !!env.complex;
  switch (n.t) {
    case "num": return n.v;
    case "var": { if (n.n in (env.bind || {})) return env.bind[n.n]; const v = env.vars[n.n]; return v || V.int(0); }
    case "const":
      if (n.n === "π") return V.p(Q1);
      if (n.n === "e") return V.f(Math.E);
      if (n.n === "i") { if (!cx) ERR("Math", "Chỉ dùng i trong ứng dụng Số phức"); return V.c(0, 1); }
      if (n.n === "Ans") return env.ans || V.int(0);
      if (n.n === "PreAns") return env.preAns || V.int(0);
      if (n.n === "Ran#") return V.q(new Q(BigInt(Math.floor(Math.random() * 1000)), 1000n));
      if (n.n.startsWith("k:")) return V.q(Q.dec(SCI[n.n.slice(2)][1]));
      if (n.n.startsWith("Mat") || n.n.startsWith("Vct")) {
        const st = n.n.startsWith("Mat") ? env.mats : env.vcts, v = st && st[n.n.slice(3)];
        if (!v) ERR("Math", (n.n.startsWith("Mat") ? "Ma trận " : "Vectơ ") + n.n.slice(3) + " chưa được định nghĩa");
        return v;
      }
      break;
    case "neg": { const a = evalNode(n.a, env); return isMV(a) ? mvBin("*", V.int(-1), a) : neg(a); }
    case "conv": return V.f(CONV[n.c][1](toNum(evalNode(n.a, env))));
    case "bin": {
      const a = evalNode(n.a, env), b = evalNode(n.b, env);
      if (isMV(a) || isMV(b)) return mvBin(n.op, a, b);
      if (n.op === "+") return add(a, b); if (n.op === "-") return sub(a, b);
      if (n.op === "*") return mul(a, b); return div(a, b);
    }
    case "mixed": { const w = evalNode(n.w, env), f = div(evalNode(n.a, env), evalNode(n.b, env)); return toNum(w) < 0 ? sub(w, f) : add(w, f); }
    case "pow": { const a = evalNode(n.a, env), b = evalNode(n.b, env); return isMV(a) ? mvPow(a, b) : pow(a, b, cx); }
    case "inv": { const a = evalNode(n.a, env); return a.k === "mat" ? matInv(a) : inv(a); }
    case "pct": return div(evalNode(n.a, env), V.int(100));
    case "dms": { let r = V.int(0); n.parts.forEach((p, i) => { r = add(r, div(evalNode(p, env), V.int([1, 60, 3600][i]))); }); return r; }
    case "root": {
      const k = evalNode(n.n, env), x = evalNode(n.a, env);
      if (isZero(k)) ERR("Math");
      return pow(x, inv(k), cx);
    }
    case "logb": return logV(evalNode(n.b, env), evalNode(n.a, env));
    case "polar": { const r = toNum(evalNode(n.a, env)), th = toRad(toNum(evalNode(n.b, env)), A); return V.c(r * Math.cos(th), r * Math.sin(th)); }
    case "eq": ERR("Syntax");
    case "divr": ERR("Syntax");
    case "deriv": {
      const a = toNum(evalNode(n.at, env)), f = t => toNum(evalNode(n.f, { ...env, bind: { ...(env.bind || {}), x: V.f(t) } }));
      const h = 1e-3 * Math.max(1, Math.abs(a));
      const D = h => (f(a - 2 * h) - 8 * f(a - h) + 8 * f(a + h) - f(a + 2 * h)) / (12 * h);
      const d1 = D(h), d2 = D(h / 2), r = d2 + (d2 - d1) / 15;
      if (!isFinite(r)) ERR("Math");
      return niceFloat(r, 1e-9);
    }
    case "integ": {
      const a = toNum(evalNode(n.a, env)), b = toNum(evalNode(n.b, env));
      const f = t => { const v = toNum(evalNode(n.f, { ...env, bind: { ...(env.bind || {}), x: V.f(t) } })); if (!isFinite(v)) ERR("Math"); return v; };
      return niceFloat(integrate(f, a, b), 1e-10);
    }
    case "sum": case "prod": {
      const a = asInt(evalNode(n.a, env)), b = asInt(evalNode(n.b, env));
      if (b - a > 100000n) ERR("Math", "Quá nhiều số hạng");
      let r = V.int(n.t === "sum" ? 0 : 1);
      for (let k = a; k <= b; k++) { const v = evalNode(n.f, { ...env, bind: { ...(env.bind || {}), x: V.q(new Q(k)) } }); r = n.t === "sum" ? add(r, v) : mul(r, v); }
      return r;
    }
    case "fn": return callFn(n.n, n.args.map(a => (n.n === "f" || n.n === "g" ? a : evalNode(a, env))), env);
  }
  ERR("Syntax");
}
function niceFloat(v, tol) {
  const r = Math.round(v); if (Math.abs(v - r) < tol * Math.max(1, Math.abs(v))) return V.int(r);
  const q = qFromFloat(v, 1000, tol); if (q) return V.q(q);
  return V.f(v);
}
function integrate(f, a, b) { // Gauss–Kronrod 7-15 thích nghi
  const XK = [0.991455371120813, 0.949107912342759, 0.864864423359769, 0.741531185599394, 0.586087235467691, 0.405845151377397, 0.207784955007898, 0];
  const WK = [0.022935322010529, 0.063092092629979, 0.104790010322250, 0.140653259715525, 0.169004726639267, 0.190350578064785, 0.204432940075298, 0.209482141084728];
  const WG = [0.129484966168870, 0.279705391489277, 0.381830050505119, 0.417959183673469];
  let calls = 0;
  function gk(a, b) {
    const c = (a + b) / 2, h = (b - a) / 2; let k = WK[7] * f(c), g = WG[3] * f(c);
    for (let j = 0; j < 7; j++) { const dx = h * XK[j], s = f(c - dx) + f(c + dx); k += WK[j] * s; if (j % 2 === 1) g += WG[(j - 1) / 2] * s; }
    calls++; return [k * h, Math.abs((k - g) * h)];
  }
  function rec(a, b, tol, depth) {
    const [v, e] = gk(a, b);
    if (e <= tol || depth > 40 || calls > 4000) return v;
    const m = (a + b) / 2; return rec(a, m, tol / 2, depth + 1) + rec(m, b, tol / 2, depth + 1);
  }
  if (a === b) return 0;
  return rec(a, b, 1e-11, 0);
}
/* ---------- ma trận / vectơ ---------- */
const isMV = x => x && (x.k === "mat" || x.k === "vec");
function M(r, c, f) { const a = []; for (let i = 0; i < r; i++) { a.push([]); for (let j = 0; j < c; j++) a[i].push(f(i, j)); } return { k: "mat", r, c, a }; }
function mvBin(op, a, b) {
  const sc = x => !isMV(x);
  if (op === "+" || op === "-") {
    const f = op === "+" ? add : sub;
    if (a.k === "mat" && b.k === "mat") { if (a.r !== b.r || a.c !== b.c) ERR("Math", "Kích thước không khớp"); return M(a.r, a.c, (i, j) => f(a.a[i][j], b.a[i][j])); }
    if (a.k === "vec" && b.k === "vec") { if (a.a.length !== b.a.length) ERR("Math", "Kích thước không khớp"); return { k: "vec", a: a.a.map((v, i) => f(v, b.a[i])) }; }
    ERR("Math", "Không thể cộng/trừ số với ma trận/vectơ");
  }
  if (op === "*") {
    if (sc(a)) return b.k === "mat" ? M(b.r, b.c, (i, j) => mul(a, b.a[i][j])) : { k: "vec", a: b.a.map(v => mul(a, v)) };
    if (sc(b)) return mvBin("*", b, a);
    if (a.k === "mat" && b.k === "mat") {
      if (a.c !== b.r) ERR("Math", "Số cột của ma trận trước phải bằng số hàng của ma trận sau");
      return M(a.r, b.c, (i, j) => { let s = V.int(0); for (let k = 0; k < a.c; k++) s = add(s, mul(a.a[i][k], b.a[k][j])); return s; });
    }
    if (a.k === "vec" && b.k === "vec") { // tích có hướng
      if (a.a.length !== 3 || b.a.length !== 3) ERR("Math", "Tích có hướng cần vectơ 3 chiều");
      const [x1, y1, z1] = a.a, [x2, y2, z2] = b.a;
      return { k: "vec", a: [sub(mul(y1, z2), mul(z1, y2)), sub(mul(z1, x2), mul(x1, z2)), sub(mul(x1, y2), mul(y1, x2))] };
    }
    if (a.k === "mat" && b.k === "vec") { if (a.c !== b.a.length) ERR("Math"); return { k: "vec", a: a.a.map(row => row.reduce((s, v, k) => add(s, mul(v, b.a[k])), V.int(0))) }; }
    ERR("Math");
  }
  if (op === "/") { if (isMV(b)) ERR("Math"); return mvBin("*", inv(b), a); }
  ERR("Math");
}
function mvPow(a, b) {
  if (a.k !== "mat" || a.r !== a.c) ERR("Math");
  let k = Number(asInt(b)); if (Math.abs(k) > 100) ERR("Math");
  let base = k < 0 ? matInv(a) : a, r = M(a.r, a.r, (i, j) => V.int(i === j ? 1 : 0)); k = Math.abs(k);
  while (k) { if (k & 1) r = mvBin("*", r, base); base = mvBin("*", base, base); k >>= 1; }
  return r;
}
function matDet(x) {
  if (x.k !== "mat" || x.r !== x.c) ERR("Math", "Định thức cần ma trận vuông");
  const n = x.r, a = x.a.map(r => r.slice()); let d = V.int(1);
  for (let c = 0; c < n; c++) {
    let p = -1; for (let r = c; r < n; r++) if (!isZero(a[r][c]) && Math.abs(toNum(a[r][c])) > 1e-14) { p = r; break; }
    if (p < 0) return V.int(0);
    if (p !== c) { [a[p], a[c]] = [a[c], a[p]]; d = neg(d); }
    d = mul(d, a[c][c]);
    for (let r = c + 1; r < n; r++) { const f = div(a[r][c], a[c][c]); for (let k = c; k < n; k++) a[r][k] = sub(a[r][k], mul(f, a[c][k])); }
  }
  return d;
}
function matInv(x) {
  if (x.k !== "mat" || x.r !== x.c) ERR("Math", "Nghịch đảo cần ma trận vuông");
  const n = x.r, a = x.a.map((r, i) => r.concat(Array.from({ length: n }, (_, j) => V.int(i === j ? 1 : 0))));
  for (let c = 0; c < n; c++) {
    let p = -1; for (let r = c; r < n; r++) if (!isZero(a[r][c]) && Math.abs(toNum(a[r][c])) > 1e-14) { p = r; break; }
    if (p < 0) ERR("Math", "Ma trận suy biến (định thức = 0)");
    [a[p], a[c]] = [a[c], a[p]];
    const pv = a[c][c]; for (let k = 0; k < 2 * n; k++) a[c][k] = div(a[c][k], pv);
    for (let r = 0; r < n; r++) if (r !== c && !isZero(a[r][c])) { const f = a[r][c]; for (let k = 0; k < 2 * n; k++) a[r][k] = sub(a[r][k], mul(f, a[c][k])); }
  }
  return M(n, n, (i, j) => a[i][n + j]);
}
function vecDot(a, b) { if (a.k !== "vec" || b.k !== "vec" || a.a.length !== b.a.length) ERR("Math"); return a.a.reduce((s, v, i) => add(s, mul(v, b.a[i])), V.int(0)); }
function vecNorm(a) { return sqrtV(vecDot(a, a)); }
function callFn(name, args, env) {
  const A = env.ang || env.S.ang, x = args[0], cx = !!env.complex;
  switch (name) {
    case "sin": case "cos": case "tan": return trig(name, x, A);
    case "asin": case "acos": case "atan": return atrig(name, x, A);
    case "sinh": return V.f(Math.sinh(toNum(x))); case "cosh": return V.f(Math.cosh(toNum(x))); case "tanh": return V.f(Math.tanh(toNum(x)));
    case "asinh": return V.f(Math.asinh(toNum(x))); case "acosh": { const v = toNum(x); if (v < 1) ERR("Math"); return V.f(Math.acosh(v)); }
    case "atanh": { const v = toNum(x); if (Math.abs(v) >= 1) ERR("Math"); return V.f(Math.atanh(v)); }
    case "ln": { if (x.k === "c") { const [a, b] = toC(x); return V.c(Math.log(Math.hypot(a, b)), Math.atan2(b, a)); } const v = toNum(x); if (v <= 0) { if (cx && v < 0) return V.c(Math.log(-v), Math.PI); ERR("Math"); } if (x.k === "q" && x.q.cmp(Q1) === 0) return V.int(0); return V.f(clean(Math.log(v))); }
    case "log": return logV(V.int(10), x);
    case "sqrt": return sqrtV(x, cx);
    case "Abs": return x.k === "vec" ? vecNorm(x) : x.k === "mat" ? matDet(x, true) : absV(x);
    case "det": return matDet(x);
    case "Trn": if (x.k !== "mat") ERR("Math"); return M(x.c, x.r, (i, j) => x.a[j][i]);
    case "Identity": { const k = Number(asInt(x)); if (k < 1 || k > 4) ERR("Math"); return M(k, k, (i, j) => V.int(i === j ? 1 : 0)); }
    case "dot": return vecDot(args[0], args[1]);
    case "angle": { const d = toNum(vecDot(args[0], args[1])), l = toNum(vecNorm(args[0])) * toNum(vecNorm(args[1])); if (!l) ERR("Math"); return atrig("acos", niceFloat(Math.max(-1, Math.min(1, d / l)), 1e-12), A); }
    case "UnitV": { if (x.k !== "vec") ERR("Math"); const l = vecNorm(x); if (isZero(l)) ERR("Math"); return { k: "vec", a: x.a.map(v => div(v, l)) }; }
    case "fact": return factorial(x);
    case "nPr": return nPr(args[0], args[1]);
    case "nCr": return nCr(args[0], args[1]);
    case "GCD": case "LCM": {
      const a = babs(asInt(args[0])), b = babs(asInt(args[1])), g = bgcd(a, b);
      return V.q(new Q(name === "GCD" ? g : g === 0n ? 0n : a / g * b));
    }
    case "Int": { const v = toNum(x); if (x.k === "q") return V.q(new Q(x.q.n / x.q.d)); return V.int(Math.trunc(v)); }
    case "Intg": { if (x.k === "q") { let k = x.q.n / x.q.d; if (x.q.sign < 0 && !x.q.isInt) k -= 1n; return V.q(new Q(k)); } return V.int(Math.floor(toNum(x))); }
    case "ceil": return V.int(Math.ceil(toNum(x)));
    case "Rnd": return roundTo(x, env.S);
    case "RanInt": { const a = asInt(args[0]), b = asInt(args[1]); if (b < a) ERR("Math"); return V.q(new Q(a + BigInt(Math.floor(Math.random() * (Number(b - a) + 1))))); }
    case "Pol": { const X = toNum(args[0]), Y = toNum(args[1]); return { k: "list", items: [["r", sqrtV(add(mul(args[0], args[0]), mul(args[1], args[1])))], ["θ", fromRadNice(Math.atan2(Y, X), A)]] }; }
    case "Rec": { return { k: "list", items: [["x", mul(args[0], trig("cos", args[1], A))], ["y", mul(args[0], trig("sin", args[1], A))]] }; }
    case "f": case "g": {
      const fx = env.funcs && env.funcs[name]; if (!fx || !fx.length) ERR("Syntax", "Chưa định nghĩa " + name + "(x) — bấm FUNCTION");
      if ((env.depth || 0) > 3) ERR("Math");
      const arg = evalNode(x, env);
      return evalNode(parseItems(fx), { ...env, depth: (env.depth || 0) + 1, bind: { ...(env.bind || {}), x: arg } });
    }
    case "Conjg": { const [a, b] = toC(x); return V.c(a, -b); }
    case "ReP": return V.f(toC(x)[0]);
    case "ImP": return V.f(toC(x)[1]);
    case "Arg": { const [a, b] = toC(x); return V.f(fromRad(Math.atan2(b, a), A)); }
  }
  ERR("Syntax");
}
function fromRadNice(r, A) {
  const t = r / Math.PI;
  for (const N of [12, 8]) { const k = Math.round(t * N); if (Math.abs(t * N - k) < 1e-11) { const q = new Q(BigInt(k), BigInt(N)); return A === "R" ? V.p(q) : V.q(q.mul(Q.int(A === "D" ? 180 : 200))); } }
  return V.f(fromRad(r, A));
}
function evaluate(items, env) {
  const ast = parseItems(items);
  if (ast.t === "divr") {
    const a = asInt(evalNode(ast.a, env)), b = asInt(evalNode(ast.b, env)); if (b === 0n) ERR("Math");
    let q = a / b, r = a % b; if (r < 0n) { r += babs(b); q = (a - r) / b; }
    return { k: "qr", q: V.q(new Q(q)), r: V.q(new Q(r)) };
  }
  if (ast.t === "eq") ERR("Syntax");
  return evalNode(ast, env);
}

/* ---------- 7. Định dạng kết quả ---------- */
const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const fr = (a, b) => `<span class="fr"><span class="nu">${a}</span><span class="de">${b}</span></span>`;
const sqH = (a, idx) => `<span class="sq">${idx ? `<sup class="ri">${idx}</sup>` : ""}<span class="rs">√</span><span class="ar">${a}</span></span>`;
function minus(s) { return s.replace(/^-/, "−"); }
function sciParts(v, digits) { // mantissa, exponent
  if (v === 0) return ["0", 0];
  let e = Math.floor(Math.log10(Math.abs(v))), m = v / Math.pow(10, e);
  let ms = m.toFixed(Math.max(0, digits - 1));
  if (Math.abs(parseFloat(ms)) >= 10) { e++; m = v / Math.pow(10, e); ms = m.toFixed(Math.max(0, digits - 1)); }
  return [ms, e];
}
const trimZ = s => (s.indexOf(".") >= 0 ? s.replace(/0+$/, "").replace(/\.$/, "") : s);
function sciHTML(m, e) { return `${minus(m)}<span class="x10">×10<sup>${minus(String(e))}</sup></span>`; }
function sep(s, S) { // dấu phân cách hàng nghìn
  if (!S.sep) return s;
  const m = /^(-?)(\d+)(.*)$/.exec(s); if (!m) return s;
  return m[1] + m[2].replace(/\B(?=(\d{3})+(?!\d))/g, "&#8201;") + m[3];
}
function decHTML(v, S, eng) {
  if (!isFinite(v)) ERR("Math");
  if (Math.abs(v) >= 1e100) ERR("Math");
  if (Math.abs(v) < 1e-99) v = 0;
  if (eng) {
    if (v === 0) return "0";
    let e = Math.floor(Math.log10(Math.abs(v)) / 3) * 3, m = v / Math.pow(10, e);
    let ms = trimZ(Number(m.toPrecision(10)).toString());
    if (Math.abs(Number(ms)) >= 1000) { e += 3; ms = trimZ(Number((v / Math.pow(10, e)).toPrecision(10)).toString()); }
    return sciHTML(ms, e);
  }
  if (S.fmt === "fix") {
    if (Math.abs(v) >= 1e10) { const [m, e] = sciParts(v, 10); return sciHTML(trimZ(m), e); }
    return sep(minus(v.toFixed(S.fmtN)), S);
  }
  if (S.fmt === "sci") { const [m, e] = sciParts(v, S.fmtN || 10); return sciHTML(m, e); }
  const lo = S.fmt === "norm2" ? 1e-9 : 1e-2, a = Math.abs(v);
  v = Number(v.toPrecision(10));
  if (v !== 0 && (a < lo || a >= 1e10)) { const [m, e] = sciParts(v, 10); return sciHTML(trimZ(m), e); }
  let s = v.toPrecision(10);
  if (/e/.test(s)) s = v.toFixed(12);
  return sep(minus(trimZ(s)), S);
}
const digits = q => blen(q.n) + blen(q.d);
function qHTML(q, S, mode) {
  if (q.isInt) return blen(q.n) <= 10 ? sep(minus(q.n.toString()), S) : decHTML(q.num(), S);
  if (mode === "dec" || digits(q) > 10) return decHTML(q.num(), S);
  const sg = q.sign < 0 ? "−" : "", n = babs(q.n);
  if (mode === "mixed" || (mode !== "improper" && S.frac === "mixed")) {
    const w = n / q.d, r = n % q.d;
    if (w > 0n) return `${sg}${w}<span class="mx">${fr(r, q.d)}</span>`;
  }
  return sg + fr(n, q.d);
}
function sHTML(x, S) { // (P ± Q√n)/D
  const D = x.a.d * x.b.d / bgcd(x.a.d, x.b.d), P = x.a.n * (D / x.a.d), Qc = x.b.n * (D / x.b.d);
  if (blen(P) + blen(Qc) + blen(D) + blen(x.n) > 12) return null;
  const rad = (k, first) => { const a = babs(k); return (k < 0n ? "−" : first ? "" : "+") + (a === 1n ? "" : a) + sqH(x.n); };
  let top;
  if (P === 0n) top = rad(Qc, true); else top = minus(P.toString()) + rad(Qc, false);
  if (D === 1n) return top;
  if (P === 0n && Qc < 0n) return "−" + fr(rad(-Qc, true), D);
  return fr(top, D);
}
function pHTML(q) {
  if (digits(q) > 10) return null;
  const k = babs(q.n), sg = q.sign < 0 ? "−" : "", top = (k === 1n ? "" : k) + "π";
  return q.isInt ? sg + top : sg + fr(top, q.d);
}
function recurring(q) {
  if (q.isInt) return null;
  const sg = q.sign < 0 ? "−" : "", n = babs(q.n), ip = n / q.d; let r = n % q.d;
  const seen = new Map(), ds = [];
  while (r !== 0n && !seen.has(r) && ds.length < 60) { seen.set(r, ds.length); r *= 10n; ds.push((r / q.d).toString()); r %= q.d; }
  if (r === 0n) return null;
  if (!seen.has(r)) return null;
  const st = seen.get(r), pre = ds.slice(0, st).join(""), rep = ds.slice(st).join("");
  if (pre.length + rep.length + ip.toString().length > 18) return null;
  return `${sg}${ip}.${pre}<span class="ovl">${rep}</span>`;
}
function primeHTML(x) {
  const q = asQ(x); if (!q || !q.isInt || q.n < 2n || q.n > 9999999999n) return null;
  let n = Number(q.n); const fs = [];
  for (let p = 2; p * p <= n; p += p === 2 ? 1 : 2) { let e = 0; while (n % p === 0) { n /= p; e++; } if (e) fs.push([p, e]); }
  if (n > 1) fs.push([n, 1]);
  return fs.map(([p, e]) => p + (e > 1 ? `<sup>${e}</sup>` : "")).join("×");
}
function dmsHTML(v) {
  const sg = v < 0 ? "−" : ""; v = Math.abs(v);
  let d = Math.floor(v), m = Math.floor((v - d) * 60), s = ((v - d) * 60 - m) * 60;
  s = Math.round(s * 100) / 100; if (s >= 60) { s -= 60; m++; } if (m >= 60) { m -= 60; d++; }
  return `${sg}${d}°${m}′${trimZ(s.toFixed(2))}″`;
}
function cHTML(x, S, mode) {
  const part = v => { const q = mode === "dec" ? null : qFromFloat(v, 1000, 1e-11); return q ? qHTML(q, S) : decHTML(v, S); };
  if (S.cform === "polar") {
    const r = Math.hypot(x.re, x.im), th = fromRad(Math.atan2(x.im, x.re), S.ang);
    return part(r) + "∠" + part(th);
  }
  const re = Math.abs(x.re) < 1e-13 ? 0 : x.re, im = x.im;
  const ims = (Math.abs(Math.abs(im) - 1) < 1e-13 ? "" : part(Math.abs(im))) + "<i>i</i>";
  if (re === 0) return (im < 0 ? "−" : "") + ims;
  return part(re) + (im < 0 ? "−" : "+") + ims;
}
/* mode: std | dec | improper | mixed | prime | dms | eng | rec */
function formatValue(x, S, mode = "std") {
  if (x.k === "mat") return `<span class="mat"><table>${x.a.map(r => "<tr>" + r.map(v => "<td>" + formatValue(v, S, mode) + "</td>").join("") + "</tr>").join("")}</table></span>`;
  if (x.k === "vec") return `<span class="mat vec"><table><tr>${x.a.map(v => "<td>" + formatValue(v, S, mode) + "</td>").join("")}</tr></table></span>`;
  if (x.k === "cx") { const im = x.im, ng = toNum(im) < 0, ia = ng ? neg(im) : im, ih = (isExact(ia) && ia.k === "q" && ia.q.cmp(Q1) === 0 ? "" : formatValue(ia, S, mode)) + "<i>i</i>"; return isZero(x.re) ? (ng ? "−" : "") + ih : formatValue(x.re, S, mode) + (ng ? "−" : "+") + ih; }
  if (x.k === "list") return x.items.map(([n, v]) => `<div class="li"><i>${n}=</i>${formatValue(v, S, mode)}</div>`).join("");
  if (x.k === "qr") return `${formatValue(x.q, S)}<span class="qr">, R=</span>${formatValue(x.r, S)}`;
  if (x.k === "c") return cHTML(x, S, mode);
  const mathO = S.io !== "decO" && mode !== "dec";
  if (mode === "prime") { const h = primeHTML(x); if (h) return h; }
  if (mode === "dms") return dmsHTML(toNum(x));
  if (mode === "eng") return decHTML(toNum(x), S, true);
  if (mode === "rec" && x.k === "q") { const h = recurring(x.q); if (h) return h; }
  if (x.k === "q") return mathO || mode === "improper" || mode === "mixed" ? qHTML(x.q, S, mode) : decHTML(x.q.num(), S);
  if (x.k === "s" && mathO) { const h = sHTML(x, S); if (h) return h; }
  if (x.k === "p" && mathO) { const h = pHTML(x.q); if (h) return h; }
  return decHTML(toNum(x), S);
}
function valueText(x) { // dạng chữ thuần (cho lịch sử, sao chép)
  if (typeof document === "undefined") return "";
  const tmp = document.createElement("div"); tmp.innerHTML = formatValue(x, { ang: "D", fmt: "norm1", io: "mathO", frac: "improper" });
  tmp.querySelectorAll(".fr").forEach(f => { f.replaceWith("(" + f.children[0].textContent + ")/(" + f.children[1].textContent + ")"); });
  tmp.querySelectorAll("sup").forEach(s => s.replaceWith("^" + s.textContent));
  return tmp.textContent.replace(/\(([^()]+)\)\/\(([^()]+)\)/g, (m, a, b) => (/^[\d]+$/.test(a) && /^\d+$/.test(b) ? a + "/" + b : m));
}
/* lưu/đọc giá trị (localStorage) */
function serV(x) {
  if (!x) return null;
  switch (x.k) {
    case "q": return ["q", x.q.n.toString(), x.q.d.toString()];
    case "s": return ["s", x.a.n.toString(), x.a.d.toString(), x.b.n.toString(), x.b.d.toString(), x.n.toString()];
    case "p": return ["p", x.q.n.toString(), x.q.d.toString()];
    case "c": return ["c", x.re, x.im];
    case "f": return ["f", x.v];
    case "mat": return ["m", x.r, x.c, x.a.map(r => r.map(serV))];
    case "vec": return ["v", x.a.map(serV)];
    default: return null;
  }
}
function desV(a) {
  try {
    if (!a) return null;
    if (a[0] === "q") return V.q(new Q(BigInt(a[1]), BigInt(a[2])));
    if (a[0] === "s") return V.s(new Q(BigInt(a[1]), BigInt(a[2])), new Q(BigInt(a[3]), BigInt(a[4])), BigInt(a[5]));
    if (a[0] === "p") return V.p(new Q(BigInt(a[1]), BigInt(a[2])));
    if (a[0] === "c") return V.c(a[1], a[2]);
    if (a[0] === "f") return V.f(a[1]);
    if (a[0] === "m") return { k: "mat", r: a[1], c: a[2], a: a[3].map(r => r.map(v => desV(v) || V.int(0))) };
    if (a[0] === "v") return { k: "vec", a: a[1].map(v => desV(v) || V.int(0)) };
  } catch (e) {}
  return null;
}
/* chuỗi → items (cho bàn phím máy tính và ô nhập nhanh) */
function strItems(s) {
  const out = []; s = String(s);
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    if (c === " ") continue;
    const map = { "*": "×", "/": "÷", "-": "−" };
    out.push({ t: "c", v: map[c] || c });
  }
  return out;
}

const CalcCore = { CalcErr, ERR, Q, Q0, Q1, V, qFromFloat, isExact, toNum, toC, isZero, asQ, asInt, sqrtV, add, sub, mul, div, neg, inv, pow, cmpV, trig, atrig, logV, factorial, nCr, nPr, absV, niceFloat, integrate, lex, parseItems, evalNode, evaluate, formatValue, valueText, serV, desV, strItems, decHTML, qHTML, M, mvBin, matDet, matInv, vecDot, vecNorm, isMV, SCI, CONV, CONSTS, VARS, fromRad, toRad, bgcd, babs };
if (typeof globalThis !== "undefined") globalThis.CalcCore = CalcCore;
/* =====================================================================
   TRÌNH SOẠN BIỂU THỨC HIỂN THỊ TỰ NHIÊN (Natural Textbook Display)
   ===================================================================== */
const TPL = { // số ô, thứ tự di chuyển ◀▶, ô bắt đầu
  frac: [2, [0, 1], 0], mixed: [3, [0, 1, 2], 0], sqrt: [1, [0], 0], cbrt: [1, [0], 0], root: [2, [0, 1], 0], log: [2, [0, 1], 0],
  abs: [1, [0], 0], deriv: [2, [0, 1], 0], integ: [3, [0, 1, 2], 0], sum: [3, [0, 1, 2], 0], prod: [3, [0, 1, 2], 0],
  exp10: [1, [0], 0], expe: [1, [0], 0], pow: [1, [0], 0]
};
const VERT = { // ▲▼ giữa các ô
  frac: { 0: { down: 1 }, 1: { up: 0 } }, mixed: { 1: { down: 2 }, 2: { up: 1 } },
  integ: { 0: { up: 1 }, 1: { down: 0 }, 2: { up: 1, down: 0 } }, sum: { 0: { up: 1 }, 1: { down: 0 }, 2: { up: 1, down: 0 } },
  prod: { 0: { up: 1 }, 1: { down: 0 }, 2: { up: 1, down: 0 } }
};
const isTpl = it => it && it.t !== "c" && it.t !== "f";
const clone = x => JSON.parse(JSON.stringify(x));
const CH = c => ({ t: "c", v: c });
const FN = v => ({ t: "f", v });
class Editor {
  constructor(items) { this.root = items ? clone(items) : []; this.path = []; this.pos = this.root.length; this.hist = []; this.max = 199; }
  arr(path = this.path) { let a = this.root; for (const [i, s] of path) a = a[i].s[s]; return a; }
  snap() { this.hist.push(JSON.stringify([this.root, this.path, this.pos])); if (this.hist.length > 60) this.hist.shift(); }
  undo() { const h = this.hist.pop(); if (!h) return false; [this.root, this.path, this.pos] = JSON.parse(h); return true; }
  set(items, atStart) { this.root = clone(items || []); this.path = []; this.pos = atStart ? 0 : this.root.length; }
  clear() { this.snap(); this.set([]); }
  get empty() { return !this.root.length; }
  count(a = this.root) { return a.reduce((n, it) => n + 1 + (isTpl(it) ? it.s.reduce((m, s) => m + this.count(s), 0) : 0), 0); }
  insert(item) {
    if (this.count() >= this.max) return false;
    this.snap(); const a = this.arr(); a.splice(this.pos, 0, item); this.pos++; return true;
  }
  insertChars(str) { for (const c of str) this.insert(CH(c)); }
  insertTpl(t, prefill) {
    if (this.count() >= this.max) return false;
    this.snap();
    const [n, , start] = TPL[t], it = { t, s: Array.from({ length: n }, () => []) }, a = this.arr();
    let at = this.pos, slot = start;
    if (prefill) prefill.forEach((p, i) => { if (p) it.s[i] = clone(p); });
    if (t === "frac" || t === "mixed") { // nuốt số đứng ngay trước làm tử số / phần nguyên
      let j = this.pos; while (j > 0 && a[j - 1].t === "c" && /^[0-9.]$/.test(a[j - 1].v)) j--;
      if (j < this.pos) { it.s[0] = a.splice(j, this.pos - j); at = j; slot = 1; }
    }
    a.splice(at, 0, it);
    if (t === "pow" && prefill && prefill[0]) { this.pos = at + 1; return true; } // x², x³: đứng sau
    this.path.push([at, slot]); this.pos = it.s[slot].length; return true;
  }
  parentInfo() {
    if (!this.path.length) return null;
    const [ti, si] = this.path[this.path.length - 1], parent = this.arr(this.path.slice(0, -1));
    return { ti, si, parent, tpl: parent[ti], nav: TPL[parent[ti].t][1] };
  }
  right() {
    const a = this.arr();
    if (this.pos < a.length) {
      const it = a[this.pos];
      if (isTpl(it)) { this.path.push([this.pos, TPL[it.t][1][0]]); this.pos = 0; } else this.pos++;
      return;
    }
    const P = this.parentInfo(); if (!P) { this.pos = 0; return; }
    const k = P.nav.indexOf(P.si);
    if (k < P.nav.length - 1) { this.path[this.path.length - 1] = [P.ti, P.nav[k + 1]]; this.pos = 0; }
    else { this.path.pop(); this.pos = P.ti + 1; }
  }
  left() {
    const a = this.arr();
    if (this.pos > 0) {
      const it = a[this.pos - 1];
      if (isTpl(it)) { const nav = TPL[it.t][1], s = nav[nav.length - 1]; this.path.push([this.pos - 1, s]); this.pos = it.s[s].length; } else this.pos--;
      return;
    }
    const P = this.parentInfo(); if (!P) { this.pos = this.root.length; return; }
    const k = P.nav.indexOf(P.si);
    if (k > 0) { const s = P.nav[k - 1]; this.path[this.path.length - 1] = [P.ti, s]; this.pos = P.tpl.s[s].length; }
    else { this.path.pop(); this.pos = P.ti; }
  }
  vert(dir) {
    for (let L = this.path.length - 1; L >= 0; L--) {
      const [ti, si] = this.path[L], tpl = this.arr(this.path.slice(0, L))[ti], v = VERT[tpl.t];
      const tg = v && v[si] && v[si][dir];
      if (tg !== undefined) {
        const keep = L === this.path.length - 1 ? this.pos : 0;
        this.path = this.path.slice(0, L).concat([[ti, tg]]); this.pos = Math.min(keep, tpl.s[tg].length); return true;
      }
    }
    return false;
  }
  home() { this.path = []; this.pos = 0; }
  end() { this.path = []; this.pos = this.root.length; }
  del() {
    const a = this.arr();
    if (this.pos > 0) {
      const it = a[this.pos - 1];
      this.snap();
      if (isTpl(it) && it.s.some(s => s.length)) { // đi vào khuôn thay vì xóa cả khuôn
        if (it.t === "pow" && it.s[0].length <= 1) { a.splice(this.pos - 1, 1); this.pos--; return true; }
        this.hist.pop(); this.left(); return true;
      }
      a.splice(this.pos - 1, 1); this.pos--; return true;
    }
    const P = this.parentInfo(); if (!P) return false;
    const k = P.nav.indexOf(P.si);
    if (k > 0 && P.tpl.s.some((s, i) => i !== P.si && s.length) && P.tpl.s[P.nav[k - 1]].length) { this.left(); return true; }
    this.snap(); // gỡ khuôn, giữ nội dung
    const content = P.nav.flatMap(i => P.tpl.s[i]); let before = 0;
    for (let j = 0; j < k; j++) before += P.tpl.s[P.nav[j]].length;
    P.parent.splice(P.ti, 1, ...content); this.path.pop(); this.pos = P.ti + before; return true;
  }
  /* ---- hiển thị ---- */
  html(showCursor = true) {
    const cur = showCursor ? this.arr() : null, pos = this.pos;
    const R = a => {
      let h = "";
      a.forEach((it, i) => { if (a === cur && i === pos) h += CURSOR; h += itemHTML(it, slot); });
      if (a === cur && pos === a.length) h += CURSOR;
      return h;
    };
    const slot = a => (a.length ? `<span class="sl">${R(a)}</span>` : `<span class="sl ph">${a === cur ? CURSOR : ""}</span>`);
    return R(this.root) || (showCursor ? "" : "");
  }
}
const CURSOR = '<span class="cur"></span>';
const FN_LABEL = { asin: "sin<sup>−1</sup>", acos: "cos<sup>−1</sup>", atan: "tan<sup>−1</sup>", asinh: "sinh<sup>−1</sup>", acosh: "cosh<sup>−1</sup>", atanh: "tanh<sup>−1</sup>", Abs: "Abs", f: "<i>f</i>", g: "<i>g</i>" };
const CH_LABEL = { "neg": '<span class="ng">−</span>', "inv": "<sup>−1</sup>", "E": '<span class="e10">ᴇ</span>', "nPr": "<b class='pc'>P</b>", "nCr": "<b class='pc'>C</b>", "e": "<i class='ee'>e</i>", "i": "<i>i</i>", "Ran#": "Ran#", "÷R": "÷R", "Ans": "Ans", "PreAns": "PreAns", ",": ",", "=": "=", "°": "°", "∠": "∠", "%": "%" };
function chLabel(v) {
  if (CH_LABEL[v]) return CH_LABEL[v];
  if (/^[A-Fxyz M]$/.test(v)) return `<i class="var">${v}</i>`;
  if (v.startsWith("k:")) return `<span class="kc">${SCI[v.slice(2)][0]}</span>`;
  if (CONV[v]) return `<span class="cv">${esc(v)}</span>`;
  if (/^(Mat|Vct)/.test(v)) return `<span class="mn">${v}</span>`;
  if (/^(and|or|xor|xnor)$/.test(v)) return ` <span class="kw">${v}</span> `;
  return esc(v);
}
function itemHTML(it, slot) {
  if (it.t === "c") return `<span class="ch">${chLabel(it.v)}</span>`;
  if (it.t === "f") return `<span class="fn">${FN_LABEL[it.v] || it.v}(</span>`;
  const s = it.s;
  const big = (op, lo, up, body, lead) => `<span class="bo"><span class="bo-u">${slot(up)}</span><span class="bo-op">${op}</span><span class="bo-l">${lead || ""}${slot(lo)}</span></span><span class="pa">(</span>${slot(body)}<span class="pa">)</span>`;
  switch (it.t) {
    case "frac": return `<span class="fr"><span class="nu">${slot(s[0])}</span><span class="de">${slot(s[1])}</span></span>`;
    case "mixed": return `${slot(s[0])}<span class="fr"><span class="nu">${slot(s[1])}</span><span class="de">${slot(s[2])}</span></span>`;
    case "sqrt": return `<span class="sq"><span class="rs">√</span><span class="ar">${slot(s[0])}</span></span>`;
    case "cbrt": return `<span class="sq"><sup class="ri">3</sup><span class="rs">√</span><span class="ar">${slot(s[0])}</span></span>`;
    case "root": return `<span class="sq"><sup class="ri">${slot(s[0])}</sup><span class="rs">√</span><span class="ar">${slot(s[1])}</span></span>`;
    case "log": return `<span class="fn">log</span><sub class="lgb">${slot(s[0])}</sub><span class="pa">(</span>${slot(s[1])}<span class="pa">)</span>`;
    case "abs": return `<span class="ab">${slot(s[0])}</span>`;
    case "deriv": return `<span class="fr dd"><span class="nu">d</span><span class="de">d<i>x</i></span></span><span class="pa">(</span>${slot(s[0])}<span class="pa">)</span><span class="at">|<sub><i>x</i>=${slot(s[1])}</sub></span>`;
    case "integ": return `<span class="bo"><span class="bo-u">${slot(s[1])}</span><span class="bo-op it">∫</span><span class="bo-l">${slot(s[0])}</span></span>${slot(s[2])}<span class="dx">d<i>x</i></span>`;
    case "sum": return big("Σ", s[0], s[1], s[2], "<i>x</i>=");
    case "prod": return big("Π", s[0], s[1], s[2], "<i>x</i>=");
    case "exp10": return `10<sup class="ex">${slot(s[0])}</sup>`;
    case "expe": return `<i class="ee">e</i><sup class="ex">${slot(s[0])}</sup>`;
    case "pow": return `<sup class="ex">${slot(s[0])}</sup>`;
  }
  return "?";
}
function itemsHTML(items) { const e = new Editor(items); return e.html(false); }
/* dạng chữ một dòng (lịch sử, sao chép) */
function itemsText(items) {
  const T = a => a.map(itemText).join("");
  const P = a => (a.length > 1 && !a.every(it => it.t === "c" && /^[0-9.A-Za-zπ]$/.test(it.v)) ? "(" + T(a) + ")" : T(a));
  function itemText(it) {
    if (it.t === "c") {
      const v = it.v, m = { neg: "−", inv: "⁻¹", E: "ᴇ", nPr: "P", nCr: "C" };
      if (m[v]) return m[v]; if (v.startsWith("k:")) return SCI[v.slice(2)][0].replace(/<[^>]+>/g, ""); return v;
    }
    if (it.t === "f") return (FN_LABEL[it.v] || it.v).replace("<sup>−1</sup>", "⁻¹").replace(/<[^>]+>/g, "") + "(";
    const s = it.s;
    switch (it.t) {
      case "frac": return P(s[0]) + "/" + P(s[1]);
      case "mixed": return T(s[0]) + "⌟" + T(s[1]) + "/" + T(s[2]);
      case "sqrt": return "√" + P(s[0]); case "cbrt": return "∛" + P(s[0]); case "root": return P(s[0]) + "√" + P(s[1]);
      case "log": return "log" + P(s[0]) + "(" + T(s[1]) + ")"; case "abs": return "|" + T(s[0]) + "|";
      case "deriv": return "d/dx(" + T(s[0]) + ")|x=" + T(s[1]);
      case "integ": return "∫[" + T(s[0]) + "→" + T(s[1]) + "](" + T(s[2]) + ")dx";
      case "sum": return "Σ[x=" + T(s[0]) + "→" + T(s[1]) + "](" + T(s[2]) + ")";
      case "prod": return "Π[x=" + T(s[0]) + "→" + T(s[1]) + "](" + T(s[2]) + ")";
      case "exp10": return "10^" + P(s[0]); case "expe": return "e^" + P(s[0]); case "pow": return "^" + P(s[0]);
    }
    return "";
  }
  return T(items);
}
/* giá trị → items (đưa kết quả vào ô nhập: ví dụ khi sửa ô của bảng) */
function valueItems(x) {
  const num = q => { const s = []; if (q.sign < 0) s.push(CH("neg")); const a = babs(q.n); if (q.isInt) return s.concat([...a.toString()].map(CH)); s.push({ t: "frac", s: [[...a.toString()].map(CH), [...q.d.toString()].map(CH)] }); return s; };
  if (x.k === "q") return num(x.q);
  if (x.k === "p") { const q = x.q, a = babs(q.n), s = q.sign < 0 ? [CH("neg")] : []; const top = (a === 1n ? [] : [...a.toString()].map(CH)).concat([CH("π")]); return s.concat(q.isInt ? top : [{ t: "frac", s: [top, [...q.d.toString()].map(CH)] }]); }
  if (x.k === "s") {
    const out = []; if (!x.a.zero) out.push(...num(x.a), CH(x.b.sign < 0 ? "−" : "+")); else if (x.b.sign < 0) out.push(CH("neg"));
    const b = new Q(babs(x.b.n), x.b.d), rt = { t: "sqrt", s: [[...x.n.toString()].map(CH)] };
    if (b.isInt) { if (b.n !== 1n) out.push(...[...b.n.toString()].map(CH)); out.push(rt); }
    else out.push({ t: "frac", s: [(b.n === 1n ? [] : [...b.n.toString()].map(CH)).concat([rt]), [...b.d.toString()].map(CH)] });
    return out;
  }
  const v = toNum(x); let s = Number(v.toPrecision(12)).toString().replace("e+", "E").replace("e", "E");
  const out = []; for (const c of s) out.push(CH(c === "-" ? (out.length && out[out.length - 1].v === "E" ? "−" : "neg") : c)); return out;
}
/* =====================================================================
   THUẬT TOÁN ỨNG DỤNG: đa thức, hệ phương trình, thống kê, phân phối,
   Solver, bất phương trình, Base-N
   ===================================================================== */
/* ---- đa thức ---- */
function cplxRoots(c) { // c: hệ số số thực bậc cao → thấp; Durand–Kerner
  const n = c.length - 1, a = c.map(v => v / c[0]);
  let z = Array.from({ length: n }, (_, k) => [Math.cos(2 * Math.PI * k / n + 0.4) * (1 + Math.max(...a.map(Math.abs))), Math.sin(2 * Math.PI * k / n + 0.4) * (1 + Math.max(...a.map(Math.abs)))]);
  const cm = (x, y) => [x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]];
  const cd = (x, y) => { const m = y[0] * y[0] + y[1] * y[1]; return [(x[0] * y[0] + x[1] * y[1]) / m, (x[1] * y[0] - x[0] * y[1]) / m]; };
  const ev = x => a.reduce((s, k) => { const t = cm(s, x); return [t[0] + k, t[1]]; }, [0, 0]);
  for (let it = 0; it < 800; it++) {
    let mx = 0;
    z = z.map((zi, i) => { let d = [1, 0]; z.forEach((zj, j) => { if (j !== i) d = cm(d, [zi[0] - zj[0], zi[1] - zj[1]]); }); if (!d[0] && !d[1]) d = [1e-12, 0]; const st = cd(ev(zi), d); mx = Math.max(mx, Math.hypot(st[0], st[1])); return [zi[0] - st[0], zi[1] - st[1]]; });
    if (mx < 1e-15) break;
  }
  // Newton đánh bóng
  const da = a.slice(0, -1).map((k, i) => k * (n - i));
  const evd = x => da.reduce((s, k) => { const t = cm(s, x); return [t[0] + k, t[1]]; }, [0, 0]);
  return z.map(r => { for (let i = 0; i < 6; i++) { const f = ev(r), d = evd(r); if (!d[0] && !d[1]) break; const st = cd(f, d); r = [r[0] - st[0], r[1] - st[1]]; } return r; });
}
function qPolyEval(cq, x) { return cq.reduce((s, k) => s.mul(x).add(k), Q0); }
function qDeflate(cq, r) { const out = [cq[0]]; for (let i = 1; i < cq.length - 1; i++) out.push(out[i - 1].mul(r).add(cq[i])); return out; }
function quadRootsExact(a, b, c) { // Q → [V,V] (thực hoặc phức "cx")
  const D = b.mul(b).sub(Q.int(4).mul(a).mul(c)), a2 = a.mul(Q.int(2));
  if (D.sign >= 0) {
    const sd = sqrtV(V.q(D)), mb = V.q(b.neg());
    const r1 = div(sub(mb, sd), V.q(a2)), r2 = div(add(mb, sd), V.q(a2));
    return [r1, r2].sort((x, y) => toNum(x) - toNum(y));
  }
  const re = V.q(b.neg().div(a2)), im = div(sqrtV(V.q(D.neg())), V.q(a2.sign < 0 ? a2.neg() : a2));
  return [{ k: "cx", re, im }, { k: "cx", re, im: neg(im) }];
}
/* coefs: mảng V (bậc cao → thấp) → nghiệm [V] */
function polyRoots(coefs) {
  if (isZero(coefs[0])) ERR("Math", "Hệ số bậc cao nhất phải khác 0");
  const allQ = coefs.every(v => v.k === "q");
  let found = [];
  if (allQ) {
    let cq = coefs.map(v => v.q);
    while (cq.length > 3) {
      const num = cplxRoots(cq.map(q => q.num()));
      let hit = null;
      for (const r of num) {
        if (Math.abs(r[1]) > 1e-6) continue;
        const g = qFromFloat(r[0], 100000, 1e-9) || (Math.abs(r[0]) < 1e-12 ? Q0 : null);
        if (g && qPolyEval(cq, g).zero) { hit = g; break; }
      }
      if (!hit) break;
      found.push(V.q(hit)); cq = qDeflate(cq, hit);
    }
    if (cq.length === 3) found = found.concat(quadRootsExact(cq[0], cq[1], cq[2]));
    else if (cq.length === 2) found.push(V.q(cq[1].neg().div(cq[0])));
    else found = found.concat(numRoots(cq.map(q => q.num())));
  } else found = numRoots(coefs.map(toNum));
  const reals = found.filter(r => r.k !== "cx" && r.k !== "c").sort((x, y) => toNum(x) - toNum(y));
  const cs = found.filter(r => r.k === "cx" || r.k === "c");
  return reals.concat(cs);
}
function numRoots(c) {
  return cplxRoots(c).map(([re, im]) => (Math.abs(im) < 1e-9 * Math.max(1, Math.abs(re)) ? niceFloat(re, 1e-10) : { k: "cx", re: niceFloat(re, 1e-10), im: niceFloat(im, 1e-10) }));
}
function polyEvalV(coefs, x) { return coefs.reduce((s, k) => add(mul(s, x), k), V.int(0)); }
/* ---- hệ phương trình tuyến tính: rows n×(n+1) V ---- */
function linSolve(rows) {
  const n = rows.length, a = rows.map(r => r.slice());
  let rank = 0; const piv = [];
  for (let c = 0; c < n && rank < n; c++) {
    let p = -1; for (let r = rank; r < n; r++) if (!isZero(a[r][c]) && Math.abs(toNum(a[r][c])) > 1e-13) { p = r; break; }
    if (p < 0) continue;
    [a[p], a[rank]] = [a[rank], a[p]];
    const pv = a[rank][c]; for (let k = c; k <= n; k++) a[rank][k] = div(a[rank][k], pv);
    for (let r = 0; r < n; r++) if (r !== rank && !isZero(a[r][c])) { const f = a[r][c]; for (let k = c; k <= n; k++) a[r][k] = sub(a[r][k], mul(f, a[rank][k])); }
    piv.push(c); rank++;
  }
  if (rank < n) {
    for (let r = rank; r < n; r++) if (!isZero(a[r][n]) && Math.abs(toNum(a[r][n])) > 1e-11) return { none: true };
    return { inf: true };
  }
  return { x: a.map(r => r[n]) };
}
/* ---- Solver: f(x)=0 ---- */
function solveEq(f, x0) {
  let x = x0, fx = f(x);
  if (!isFinite(fx)) fx = NaN;
  const tryNewton = start => {
    let x = start;
    for (let i = 0; i < 200; i++) {
      const fx = f(x); if (!isFinite(fx)) return null;
      if (Math.abs(fx) < 1e-15) return x;
      const h = 1e-7 * Math.max(1, Math.abs(x)), d = (f(x + h) - f(x - h)) / (2 * h);
      if (!isFinite(d) || d === 0) return null;
      let st = fx / d, nx = x - st, k = 0;
      while (Math.abs(f(nx)) > Math.abs(fx) && k++ < 30) { st /= 2; nx = x - st; }
      if (Math.abs(nx - x) < 1e-14 * Math.max(1, Math.abs(x))) return nx;
      x = nx;
    }
    return Math.abs(f(x)) < 1e-9 ? x : null;
  };
  let r = tryNewton(x);
  if (r === null) for (const s of [0, 1, -1, 10, -10, 100, -100, 0.5, -0.5, 1000]) { r = tryNewton(x0 + s); if (r !== null) break; }
  if (r === null) ERR("Math", "Không tìm được nghiệm — thử giá trị đầu khác");
  return r;
}
/* ---- bất phương trình đa thức ---- */
function polyIneq(coefs, rel) { // rel: ">", "<", "≥", "≤"
  const roots = polyRoots(coefs).filter(r => r.k !== "cx" && r.k !== "c");
  const uniq = []; roots.forEach(r => { if (!uniq.length || Math.abs(toNum(r) - toNum(uniq[uniq.length - 1])) > 1e-9) uniq.push(r); });
  const cf = coefs.map(toNum), P = x => cf.reduce((s, k) => s * x + k, 0);
  const ok = v => (rel === ">" ? v > 0 : rel === "<" ? v < 0 : rel === "≥" ? v >= 0 : v <= 0);
  const pts = uniq.map(toNum), segs = []; // [{lo, hi, loIn, hiIn}]
  const sample = i => (pts.length === 0 ? 0 : i === 0 ? pts[0] - 1 : i === pts.length ? pts[pts.length - 1] + 1 : (pts[i - 1] + pts[i]) / 2);
  const pieces = [];
  for (let i = 0; i <= pts.length; i++) {
    pieces.push({ type: "int", i, ok: ok(P(sample(i))) });
    if (i < pts.length) pieces.push({ type: "pt", i, ok: rel === "≥" || rel === "≤" });
  }
  let cur = null;
  const flush = () => { if (cur) segs.push(cur); cur = null; };
  pieces.forEach(p => {
    if (!p.ok) { flush(); return; }
    if (p.type === "int") {
      if (!cur) cur = { lo: p.i === 0 ? null : uniq[p.i - 1], loIn: false, hi: null, hiIn: false };
      cur.hi = p.i === pts.length ? null : uniq[p.i]; cur.hiIn = false;
    } else {
      if (!cur) cur = { lo: uniq[p.i], loIn: true, hi: uniq[p.i], hiIn: true, pt: true };
      else { cur.hi = uniq[p.i]; cur.hiIn = true; }
    }
  });
  flush();
  return segs;
}
/* ---- thống kê ---- */
function statCalc(xs, ys, fs, type) {
  const n0 = fs.reduce((s, f) => add(s, f), V.int(0)), nn = toNum(n0);
  if (!(nn > 0)) ERR("Math", "Chưa có dữ liệu");
  fs.forEach(f => { if (toNum(f) < 0) ERR("Math", "Tần số phải ≥ 0"); });
  const S = (vals, g) => vals.reduce((s, v, i) => add(s, mul(fs[i], g ? g(v, i) : v)), V.int(0));
  const out = [];
  const sx = S(xs), sx2 = S(xs, v => mul(v, v)), mx = div(sx, n0);
  const varx = sub(div(sx2, n0), mul(mx, mx)), sdx = sqrtV(toNum(varx) < 0 ? V.int(0) : varx);
  const ssx = nn > 1 ? sqrtV(div(mul(toNum(varx) < 0 ? V.int(0) : varx, n0), sub(n0, V.int(1)))) : null;
  if (!ys) {
    out.push(["x̄", mx], ["Σx", sx], ["Σx²", sx2], ["σ²x", varx], ["σx", sdx]); if (ssx) out.push(["s²x", mul(ssx, ssx)], ["sx", ssx]); out.push(["n", n0]);
    const pairs = xs.map((v, i) => [toNum(v), toNum(fs[i]), v]).filter(p => p[1] > 0).sort((a, b) => a[0] - b[0]);
    const tot = pairs.reduce((s, p) => s + p[1], 0);
    const at = k => { let c = 0; for (const p of pairs) { c += p[1]; if (c >= k) return p; } return pairs[pairs.length - 1]; };
    const medOf = (lo, hi) => { // trung vị của các phần tử thứ lo..hi (1-based, theo tần số)
      const len = hi - lo + 1; if (len <= 0) return null;
      if (len % 2) return at(lo + (len - 1) / 2)[2];
      return div(add(at(lo + len / 2 - 1)[2], at(lo + len / 2)[2]), V.int(2));
    };
    const allInt = pairs.every(p => Number.isInteger(p[1]));
    out.push(["min(x)", pairs[0][2]]);
    if (allInt) {
      const half = Math.floor(tot / 2);
      const q1 = tot > 1 ? medOf(1, half) : pairs[0][2], q3 = tot > 1 ? medOf(tot % 2 ? half + 2 : half + 1, tot) : pairs[0][2];
      out.push(["Q₁", q1], ["Med", medOf(1, tot)], ["Q₃", q3]);
    }
    out.push(["max(x)", pairs[pairs.length - 1][2]]);
    const mf = Math.max(...pairs.map(p => p[1])), modes = pairs.filter(p => p[1] === mf);
    if (modes.length < pairs.length || pairs.length === 1) out.push(["Mốt", modes.length === 1 ? modes[0][2] : { k: "txt", h: modes.map(p => formatValue(p[2], App.S)).join("; ") }]);
    return { list: out };
  }
  const sy = S(ys), sy2 = S(ys, v => mul(v, v)), sxy = S(xs, (v, i) => mul(v, ys[i])), my = div(sy, n0);
  const vary = sub(div(sy2, n0), mul(my, my));
  out.push(["x̄", mx], ["ȳ", my], ["Σx", sx], ["Σy", sy], ["Σx²", sx2], ["Σy²", sy2], ["Σxy", sxy], ["σx", sdx], ["σy", sqrtV(toNum(vary) < 0 ? V.int(0) : vary)]);
  if (nn > 1) out.push(["sx", ssx], ["sy", sqrtV(div(mul(toNum(vary) < 0 ? V.int(0) : vary, n0), sub(n0, V.int(1))))]);
  out.push(["n", n0]);
  const reg = regression(xs.map(toNum), ys.map(toNum), fs.map(toNum), type, { xs, ys, fs });
  return { list: out, reg };
}
function regression(x, y, f, type, ex) {
  const tf = { lin: [v => v, v => v], ln: [Math.log, v => v], exp: [v => v, Math.log], abx: [v => v, Math.log], pow: [Math.log, Math.log], inv: [v => 1 / v, v => v] }[type];
  if (type === "quad") {
    let S = Array(5).fill(0), T = Array(3).fill(0), n = 0;
    x.forEach((v, i) => { for (let k = 0; k < 5; k++) S[k] += f[i] * v ** k; for (let k = 0; k < 3; k++) T[k] += f[i] * y[i] * v ** k; n += f[i]; });
    const M3 = [[S[0], S[1], S[2], T[0]], [S[1], S[2], S[3], T[1]], [S[2], S[3], S[4], T[2]]].map(r => r.map(v => niceFloat(v, 1e-13)));
    const r = linSolve(M3); if (!r.x) ERR("Math", "Không đủ dữ liệu cho hồi quy bậc hai");
    const [a, b, c] = r.x.map(v => niceFloat(toNum(v), 1e-10));
    const my = T[0] / n; let sse = 0, sst = 0; x.forEach((v, i) => { const p = toNum(a) + toNum(b) * v + toNum(c) * v * v; sse += f[i] * (y[i] - p) ** 2; sst += f[i] * (y[i] - my) ** 2; });
    return { eq: "y=a+bx+cx²", coef: [["a", a], ["b", b], ["c", c], ["R²", niceFloat(sst ? 1 - sse / sst : 1, 1e-10)]], pred: v => toNum(a) + toNum(b) * v + toNum(c) * v * v };
  }
  const X = x.map(tf[0]), Y = y.map(tf[1]);
  if ([...X, ...Y].some(v => !isFinite(v))) ERR("Math", "Dữ liệu không hợp lệ cho mô hình này (cần x>0 hoặc y>0)");
  let n = 0, sx = 0, sy = 0, sxx = 0, syy = 0, sxy = 0;
  X.forEach((v, i) => { n += f[i]; sx += f[i] * v; sy += f[i] * Y[i]; sxx += f[i] * v * v; syy += f[i] * Y[i] * Y[i]; sxy += f[i] * v * Y[i]; });
  const Sxx = sxx - sx * sx / n, Syy = syy - sy * sy / n, Sxy = sxy - sx * sy / n;
  if (Math.abs(Sxx) < 1e-300) ERR("Math", "Cần ít nhất 2 giá trị x khác nhau");
  let b = Sxy / Sxx, a = (sy - b * sx) / n; const r = Syy > 0 ? Sxy / Math.sqrt(Sxx * Syy) : 1;
  let A = a, B = b;
  if (type === "lin" && ex) { // chính xác bằng hữu tỉ
    const nV = ex.fs.reduce((s, v) => add(s, v), V.int(0)), sum = g => ex.xs.reduce((s, v, i) => add(s, mul(ex.fs[i], g(v, i))), V.int(0));
    const SX = sum(v => v), SY = sum((v, i) => ex.ys[i]), SXX = sum(v => mul(v, v)), SXY = sum((v, i) => mul(v, ex.ys[i]));
    const Dx = sub(SXX, div(mul(SX, SX), nV)), Dxy = sub(SXY, div(mul(SX, SY), nV));
    if (!isZero(Dx)) { const bb = div(Dxy, Dx), aa = div(sub(SY, mul(bb, SX)), nV); B = bb; A = aa; }
  }
  if (type === "exp") A = Math.exp(a);
  if (type === "abx") { A = Math.exp(a); B = Math.exp(b); }
  if (type === "pow") A = Math.exp(a);
  const vA = typeof A === "number" ? niceFloat(A, 1e-11) : A, vB = typeof B === "number" ? niceFloat(B, 1e-11) : B;
  const eq = { lin: "y=a+bx", ln: "y=a+b·ln(x)", exp: "y=a·e^(bx)", abx: "y=a·b^x", pow: "y=a·x^b", inv: "y=a+b/x" }[type];
  const an = toNum(vA), bn = toNum(vB);
  const pred = { lin: v => an + bn * v, ln: v => an + bn * Math.log(v), exp: v => an * Math.exp(bn * v), abx: v => an * Math.pow(bn, v), pow: v => an * Math.pow(v, bn), inv: v => an + bn / v }[type];
  const predX = { lin: v => (v - an) / bn, ln: v => Math.exp((v - an) / bn), exp: v => Math.log(v / an) / bn, abx: v => Math.log(v / an) / Math.log(bn), pow: v => Math.pow(v / an, 1 / bn), inv: v => bn / (v - an) }[type];
  return { eq, coef: [["a", vA], ["b", vB], ["r", niceFloat(r, 1e-12)]], pred, predX };
}
/* dữ liệu ghép nhóm: lớp [u_i; u_{i+1}) với tần số n_i */
function groupedStats(los, his, fs) {
  const k = los.length; if (!k) ERR("Math", "Chưa có dữ liệu");
  const L = los.map(toNum), H = his.map(toNum), F = fs.map(toNum);
  for (let i = 0; i < k; i++) { if (!(H[i] > L[i])) ERR("Math", "Đầu mút phải lớn hơn đầu trái (nhóm " + (i + 1) + ")"); if (F[i] < 0) ERR("Math", "Tần số phải ≥ 0"); if (i && Math.abs(L[i] - H[i - 1]) > 1e-12) ERR("Math", "Các nhóm phải liền nhau: đầu trái nhóm " + (i + 1) + " = đầu phải nhóm " + i); }
  const n = fs.reduce((s, v) => add(s, v), V.int(0)), nn = toNum(n); if (!(nn > 0)) ERR("Math", "Tổng tần số phải > 0");
  const mids = los.map((l, i) => div(add(l, his[i]), V.int(2)));
  const sum = g => mids.reduce((s, c, i) => add(s, mul(fs[i], g(c))), V.int(0));
  const mean = div(sum(c => c), n), m2 = div(sum(c => mul(c, c)), n), varr = sub(m2, mul(mean, mean));
  const vp = toNum(varr) < 0 ? V.int(0) : varr, out = [["x̄", mean], ["σ²", vp], ["σ", sqrtV(vp)]];
  if (nn > 1) { const s2 = div(mul(vp, n), sub(n, V.int(1))); out.push(["s²", s2], ["s", sqrtV(s2)]); }
  out.push(["n", n]);
  const quant = p => { // vị trí p·n
    const target = mul(V.q(p), n); let cum = V.int(0);
    for (let i = 0; i < k; i++) {
      const nc = add(cum, fs[i]);
      if (toNum(nc) >= toNum(target) - 1e-12 && F[i] > 0) { const h = sub(his[i], los[i]); return add(los[i], mul(div(sub(target, cum), fs[i]), h)); }
      cum = nc;
    }
    return his[k - 1];
  };
  out.push(["Q₁", quant(new Q(1n, 4n))], ["Mₑ", quant(new Q(1n, 2n))], ["Q₃", quant(new Q(3n, 4n))]);
  const mf = Math.max(...F), mi = F.indexOf(mf);
  const d1 = sub(fs[mi], mi > 0 ? fs[mi - 1] : V.int(0)), d2 = sub(fs[mi], mi < k - 1 ? fs[mi + 1] : V.int(0)), dd = add(d1, d2);
  out.push(["M₀", isZero(dd) ? los[mi] : add(los[mi], mul(div(d1, dd), sub(his[mi], los[mi])))]);
  out.push(["Nhóm mốt", { k: "txt", h: `[${formatValue(los[mi], App.S)}; ${formatValue(his[mi], App.S)})` }]);
  return out;
}
/* ---- phân phối xác suất ---- */
function erfc(x) { // Numerical Recipes erfcc (độ chính xác ~1.2e-7) → tinh chỉnh bằng chuỗi
  const z = Math.abs(x);
  let r;
  if (z < 3) { // chuỗi Taylor cho erf
    let s = 0, t = z, k = 0; const z2 = z * z;
    do { s += t / (2 * k + 1); k++; t *= -z2 / k; } while (Math.abs(t) > 1e-17 * Math.abs(s) && k < 200);
    r = 1 - 2 / Math.sqrt(Math.PI) * s;
  } else { // phân số liên tục
    let f = 0; for (let k = 60; k >= 1; k--) f = k / 2 / (z + f);
    r = Math.exp(-z * z) / Math.sqrt(Math.PI) / (z + f);
  }
  return x >= 0 ? r : 2 - r;
}
const normCdf = z => 0.5 * erfc(-z / Math.SQRT2);
function normInv(p) {
  if (!(p > 0 && p < 1)) ERR("Math", "Diện tích phải nằm trong (0; 1)");
  const a = [-3.969683028665376e1, 2.209460984245205e2, -2.759285104469687e2, 1.383577518672690e2, -3.066479806614716e1, 2.506628277459239], b = [-5.447609879822406e1, 1.615858368580409e2, -1.556989798598866e2, 6.680131188771972e1, -1.328068155288572e1], c = [-7.784894002430293e-3, -3.223964580411365e-1, -2.400758277161838, -2.549732539343734, 4.374664141464968, 2.938163982698783], d = [7.784695709041462e-3, 3.224671290700398e-1, 2.445134137142996, 3.754408661907416];
  let q, x;
  if (p < 0.02425) { q = Math.sqrt(-2 * Math.log(p)); x = (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1); }
  else if (p > 1 - 0.02425) { q = Math.sqrt(-2 * Math.log(1 - p)); x = -(((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1); }
  else { q = p - 0.5; const r = q * q; x = (((((a[0] * r + a[1]) * r + a[2]) * r + a[3]) * r + a[4]) * r + a[5]) * q / (((((b[0] * r + b[1]) * r + b[2]) * r + b[3]) * r + b[4]) * r + 1); }
  for (let i = 0; i < 3; i++) { const e = normCdf(x) - p, u = e * Math.sqrt(2 * Math.PI) * Math.exp(x * x / 2); x = x - u / (1 + x * u / 2); }
  return x;
}
function lnFact(n) { let s = 0; for (let i = 2; i <= n; i++) s += Math.log(i); return s; }
function binomPD(x, N, p) { if (x < 0 || x > N) return 0; if (p === 0) return x === 0 ? 1 : 0; if (p === 1) return x === N ? 1 : 0; if (N <= 1000) { let c = 1; const k = Math.min(x, N - x); for (let i = 1; i <= k; i++) c = c * (N - k + i) / i; return c * Math.pow(p, x) * Math.pow(1 - p, N - x); } return Math.exp(lnFact(N) - lnFact(x) - lnFact(N - x) + x * Math.log(p) + (N - x) * Math.log(1 - p)); }
function poisPD(x, l) { if (x < 0) return 0; if (l === 0) return x === 0 ? 1 : 0; return Math.exp(-l + x * Math.log(l) - lnFact(x)); }
/* ---- Base-N ---- */
const BASES = { DEC: 10, HEX: 16, BIN: 2, OCT: 8 };
function baseEval(items, base, ans) {
  const src = items.map(it => {
    if (it.t === "c" && it.v === "Ans") { const a = ans || 0n; return base === 10 ? (a < 0n ? "(-" + (-a) + ")" : a.toString()) : BigInt.asUintN(32, a).toString(base).toUpperCase(); }
    if (it.t === "f") { if (it.v === "Not" || it.v === "Neg") return " " + it.v + "("; ERR("Syntax"); }
    if (it.t !== "c") ERR("Syntax", "Base-N chỉ dùng số nguyên và + − × ÷ ( ) and or xor xnor Not Neg");
    const m = { "×": "*", "÷": "/", "−": "-", neg: "-" }; return m[it.v] || (/^(and|or|xor|xnor)$/.test(it.v) ? " " + it.v + " " : it.v);
  }).join("");
  const toks = src.match(/\s*(and|or|xor|xnor|Not\(|Neg\(|[0-9A-F]+|[-+*/()])\s*/g);
  if (!toks || toks.join("").replace(/\s/g, "") !== src.replace(/\s/g, "")) ERR("Syntax");
  const T = toks.map(t => t.trim()); let i = 0;
  const wrap = v => { v = BigInt.asIntN(32, v); return v; };
  const peek = () => T[i];
  function prim() {
    const t = T[i++];
    if (t === undefined) ERR("Syntax");
    if (t === "(") { const v = orx(); if (T[i] === ")") i++; return v; }
    if (t === "Not(" || t === "Neg(") { const v = orx(); if (T[i] === ")") i++; return wrap(t === "Not(" ? ~v : -v); }
    if (t === "-") return wrap(-prim()); if (t === "+") return prim();
    if (/^[0-9A-F]+$/.test(t)) {
      const digs = "0123456789ABCDEF".slice(0, base);
      if ([...t].some(c => !digs.includes(c))) ERR("Syntax", "Chữ số không hợp lệ trong hệ " + base);
      let v = 0n; for (const c of t) v = v * BigInt(base) + BigInt(digs.indexOf(c));
      if (base === 10) { if (v > 2147483647n) ERR("Math", "Vượt phạm vi 32 bit"); return v; }
      if (v > 0xFFFFFFFFn) ERR("Math", "Vượt phạm vi 32 bit"); return wrap(v);
    }
    ERR("Syntax");
  }
  function mulx() { let a = prim(); while (peek() === "*" || peek() === "/") { const o = T[i++], b = prim(); if (o === "/" && b === 0n) ERR("Math"); a = wrap(o === "*" ? a * b : a / b); } return a; }
  function addx() { let a = mulx(); while (peek() === "+" || peek() === "-") { const o = T[i++], b = mulx(); a = wrap(o === "+" ? a + b : a - b); } return a; }
  function andx() { let a = addx(); while (peek() === "and") { i++; a = a & addx(); } return a; }
  function orx() { let a = andx(); while (peek() === "or" || peek() === "xor" || peek() === "xnor") { const o = T[i++], b = andx(); a = wrap(o === "or" ? a | b : o === "xor" ? a ^ b : ~(a ^ b)); } return a; }
  const v = orx(); if (i < T.length) ERR("Syntax");
  return v;
}
function baseStr(v, base) {
  if (base === 10) return v.toString();
  const u = BigInt.asUintN(32, v).toString(base).toUpperCase();
  if (base === 2) return u.padStart(Math.ceil(u.length / 4) * 4, "0").replace(/(\d{4})(?=\d)/g, "$1 ");
  return u;
}
/* =====================================================================
   GIAO DIỆN: trạng thái, màn hình (calc, menu, form, bảng, kết quả)
   ===================================================================== */
const DEF_S = { ang: "D", fmt: "norm1", fmtN: 0, io: "mathO", frac: "improper", sep: false, cform: "rect" };
const LS_KEY = "hdlg_fx880btg_v1";
const KEYSPEC = {
  dot: { c: "." }, exp: { c: "E" }, add: { c: "+" }, sub: { c: "−" }, mul: { c: "×" }, div: { c: "÷" }, lp: { c: "(" }, rp: { c: ")" }, comma: { c: "," },
  neg: { c: "neg" }, inv: { c: "inv" }, fact: { c: "!" }, pct: { c: "%" }, ans: { c: "Ans" }, preans: { c: "PreAns" }, pi: { c: "π" }, e: { c: "e" }, i: { c: "i" },
  xvar: { c: "x" }, yvar: { c: "y" }, ran: { c: "Ran#" }, eq: { c: "=" }, divr: { c: "÷R" }, npr: { c: "nPr" }, ncr: { c: "nCr" }, angle: { c: "∠" }, dms: { c: "°" },
  sin: { f: "sin" }, cos: { f: "cos" }, tan: { f: "tan" }, asin: { f: "asin" }, acos: { f: "acos" }, atan: { f: "atan" }, ln: { f: "ln" },
  gcd: { f: "GCD" }, lcm: { f: "LCM" }, int: { f: "Int" }, intg: { f: "Intg" }, rnd: { f: "Rnd" }, ranint: { f: "RanInt" }, pol: { f: "Pol" }, rec: { f: "Rec" },
  frac: { tpl: "frac" }, mixed: { tpl: "mixed" }, sqrt: { tpl: "sqrt" }, cbrt: { tpl: "cbrt" }, root: { tpl: "root" }, sq: { tpl: "pow", pre: [[CH("2")]] }, cube: { tpl: "pow", pre: [[CH("3")]] },
  pow: { tpl: "pow" }, log: { tpl: "log" }, exp10: { tpl: "exp10" }, expe: { tpl: "expe" }, abs: { tpl: "abs" }, deriv: { tpl: "deriv" }, integ: { tpl: "integ" }, sum: { tpl: "sum" }
};
for (let d = 0; d <= 9; d++) KEYSPEC[String(d)] = { c: String(d) };
const SHIFT = {
  xvar: "yvar", frac: "mixed", sqrt: "cbrt", sq: "cube", pow: "root", log: "exp10", ln: "expe", sin: "asin", cos: "acos", tan: "atan", lp: "pct", rp: "comma",
  neg: "abs", inv: "fact", dms: "i", deriv: "integ", format: "sum", eq: "e", 7: "gcd", 8: "lcm", 9: "divr", del: "undo", ac: "off", 4: "int", 5: "intg", 6: "rnd",
  mul: "npr", div: "ncr", 1: "pol", 2: "rec", 3: "ran", add: "ranint", sub: "angle", 0: "preans", exp: "pi", ans: "sto", exe: "approx"
};
const POSTFIX_KEYS = new Set(["add", "sub", "mul", "div", "sq", "cube", "pow", "inv", "fact", "pct", "divr", "npr", "ncr", "root"]);
function applySpec(ed, sp) {
  if (sp.c) return ed.insert(CH(sp.c));
  if (sp.f) return ed.insert(FN(sp.f));
  if (sp.tpl) return ed.insertTpl(sp.tpl, sp.pre);
  if (sp.items) { sp.items.forEach(it => ed.insert(clone(it))); return true; }
  return false;
}
function editKey(ed, k) { // trả về true nếu đã xử lý
  if (KEYSPEC[k]) { applySpec(ed, KEYSPEC[k]); return true; }
  switch (k) {
    case "left": ed.left(); return true; case "right": ed.right(); return true;
    case "up": return ed.vert("up"); case "down": return ed.vert("down");
    case "del": ed.del(); return true; case "undo": ed.undo(); return true;
  }
  return false;
}
const cellText = v => {
  if (v == null) return "";
  if (v.k === "txt") return v.h;
  if (isMV(v)) return v.k === "mat" ? v.r + "×" + v.c : "dim " + v.a.length;
  if (v.k === "c" || v.k === "cx") return formatValue(v, App.S, "dec").replace(/<[^>]+>/g, "");
  if (v.k === "q" && v.q.isInt && blen(v.q.n) <= 9) return minus(v.q.n.toString());
  const n = toNum(v); if (n === 0) return "0";
  const a = Math.abs(n);
  if (a >= 1e7 || a < 1e-4) return minus(n.toExponential(2).replace("e+", "ᴇ").replace("e-", "ᴇ−"));
  return minus(trimZ(n.toPrecision(6)));
};
const approxHTML = v => (v && (v.k === "s" || v.k === "p" || (v.k === "q" && !v.q.isInt)) ? `<div class="ap">≈ ${decHTML(toNum(v), App.S)}</div>` : "");
const fmt = (v, mode) => (v == null ? "" : v.k === "txt" ? v.h : formatValue(v, App.S, mode));

const App = {
  S: { ...DEF_S }, vars: {}, funcs: { f: [], g: [] }, mats: {}, vcts: {}, ans: null, preAns: null, hist: [], forms: {}, eq: {}, base: "DEC",
  stat: { rows: [], freq: false, kind: "1", type: "lin" }, grp: [],
  stack: [], shift: false, off: false, app: "calc", screens: {},
  env(extra) { return { S: this.S, vars: this.vars, funcs: this.funcs, mats: this.mats, vcts: this.vcts, ans: this.ans, preAns: this.preAns, complex: this.app === "cmplx", ...(extra || {}) }; },
  top() { return this.stack[this.stack.length - 1]; },
  push(s) { this.stack.push(s); },
  pop() { if (this.stack.length > 1) this.stack.pop(); },
  closeMenus() { while (this.stack.length > 1 && this.top().isMenu) this.stack.pop(); },
  target() { for (let i = this.stack.length - 1; i >= 0; i--) if (this.stack[i].feed) return this.stack[i]; return null; },
  feed(spec) { this.closeMenus(); const t = this.target(); if (t) { while (this.top() !== t) this.stack.pop(); t.feed(spec); } },
  run(fn) {
    try { return fn(); }
    catch (e) { if (!(e instanceof CalcErr)) console.error(e); this.push(new ErrScr(e instanceof CalcErr ? e.kind : "Math", e instanceof CalcErr && e.message !== e.kind ? e.message : "")); return null; }
  },
  evalItems(items, extra) { return evaluate(items, this.env(extra)); },
  setAns(v) {
    if (!v || v.k === "list" || v.k === "qr") { if (v && v.k === "list") v = v.items[0][1]; else if (v && v.k === "qr") v = v.q; else return; }
    if (v.k === "mat") { this.mats.Ans = v; return; }
    if (v.k === "vec") { this.vcts.Ans = v; return; }
    if (v.k === "cx") v = V.c(toNum(v.re), toNum(v.im));
    this.preAns = this.ans; this.ans = v;
  },
  /* ---- lưu trữ ---- */
  save() { clearTimeout(this._st); this._st = setTimeout(() => this.flush(), 150); },
  flush() {
    clearTimeout(this._st);
    {
      try {
        const sv = o => Object.fromEntries(Object.entries(o).map(([k, v]) => [k, serV(v)]));
        const d = {
          S: this.S, vars: sv(this.vars), funcs: this.funcs, mats: sv(this.mats), vcts: sv(this.vcts), ans: serV(this.ans), preAns: serV(this.preAns),
          hist: this.hist.slice(-40).map(h => ({ items: h.items, v: serV(h.v), app: h.app })), forms: this.forms, base: this.base,
          eq: Object.fromEntries(Object.entries(this.eq).map(([k, rows]) => [k, rows.map(r => r.map(serV))])),
          stat: { ...this.stat, rows: this.stat.rows.map(r => r.map(serV)) }, grp: this.grp.map(r => r.map(serV)), app: this.app
        };
        localStorage.setItem(LS_KEY, JSON.stringify(d));
      } catch (e) {}
    }
  },
  load() {
    try {
      const d = JSON.parse(localStorage.getItem(LS_KEY) || "null"); if (!d) return;
      const dv = o => Object.fromEntries(Object.entries(o || {}).map(([k, v]) => [k, desV(v)]).filter(([, v]) => v));
      this.S = { ...DEF_S, ...(d.S || {}) }; this.vars = dv(d.vars); this.funcs = { f: [], g: [], ...(d.funcs || {}) };
      this.mats = dv(d.mats); this.vcts = dv(d.vcts); this.ans = desV(d.ans); this.preAns = desV(d.preAns);
      this.hist = (d.hist || []).map(h => ({ items: h.items, v: desV(h.v), app: h.app })).filter(h => h.v);
      this.forms = d.forms || {}; this.base = d.base || "DEC";
      this.eq = Object.fromEntries(Object.entries(d.eq || {}).map(([k, rows]) => [k, rows.map(r => r.map(v => desV(v) || V.int(0)))]));
      if (d.stat) this.stat = { ...this.stat, ...d.stat, rows: (d.stat.rows || []).map(r => r.map(v => desV(v) || V.int(0))) };
      this.grp = (d.grp || []).map(r => r.map(v => desV(v) || V.int(0)));
      if (d.app && APPS[d.app]) this.app = d.app;
    } catch (e) {}
  }
};

/* ---------------- màn hình cơ sở ---------------- */
class Scr { render() { return ""; } key() { return false; } after() {} tap() {} }
class ErrScr extends Scr {
  constructor(kind, msg) { super(); this.kind = kind; this.msg = msg; }
  render() {
    const t = { Math: "Math ERROR", Syntax: "Syntax ERROR", Dim: "Dimension ERROR" }[this.kind] || this.kind + " ERROR";
    return `<div class="err"><b>${t}</b>${this.msg ? `<small>${esc(this.msg)}</small>` : ""}<div class="eh">[AC] / [BACK] : Quay lại</div></div>`;
  }
  key(k) { if (["ac", "back", "left", "right", "exe", "ok", "del"].includes(k)) App.pop(); return true; }
}
/* ---------------- menu ---------------- */
class MenuScr extends Scr {
  constructor(title, items, opt = {}) { super(); this.title = title; this.items = items; this.sel = opt.sel || 0; this.isMenu = true; this.opt = opt; }
  render() {
    return `<div class="menu">${this.title ? `<div class="mt">${this.title}</div>` : ""}<div class="ml">${this.items.map((it, i) =>
      `<div class="mi${i === this.sel ? " on" : ""}" data-tap="${i}"><span class="mn">${i < 9 ? i + 1 : i === 9 ? 0 : ""}</span><span class="mx">${it.label}</span>${it.mark ? '<span class="mk">◆</span>' : ""}${it.sub ? '<span class="ms">▶</span>' : ""}</div>`).join("")}</div></div>`;
  }
  after(el) { const on = el.querySelector(".mi.on"), ml = el.querySelector(".ml"); if (on && ml) { const t = on.offsetTop - ml.offsetTop; if (t < ml.scrollTop) ml.scrollTop = t; else if (t + on.offsetHeight > ml.scrollTop + ml.clientHeight) ml.scrollTop = t + on.offsetHeight - ml.clientHeight; } }
  choose(i) { const it = this.items[i]; if (!it) return; this.sel = i; if (it.act) it.act(); }
  key(k) {
    const n = this.items.length;
    if (k === "up") this.sel = (this.sel - 1 + n) % n;
    else if (k === "down") this.sel = (this.sel + 1) % n;
    else if (k === "ok" || k === "exe" || k === "right") this.choose(this.sel);
    else if (k === "ac" || k === "left") App.pop();
    else if (/^[0-9]$/.test(k)) { const i = k === "0" ? 9 : Number(k) - 1; if (i < n) this.choose(i); }
    return true;
  }
  tap(i) { this.choose(Number(i)); }
}
/* ---------------- kết quả (danh sách cuộn) ---------------- */
class ResultScr extends Scr {
  constructor(title, lines, opt = {}) { super(); this.title = title; this.lines = lines; this.sel = 0; this.opt = opt; }
  render() {
    return `<div class="rs">${this.title ? `<div class="mt">${this.title}</div>` : ""}<div class="rlist">${this.lines.map((l, i) => {
      if (typeof l === "string") return `<div class="rtxt${i === this.sel ? " on" : ""}">${l}</div>`;
      const [k, v] = l;
      return `<div class="rl${i === this.sel ? " on" : ""}" data-tap="${i}"><span class="rk">${k}${k && !/[=:]$/.test(k) ? "=" : ""}</span><span class="rv">${fmt(v)}</span>${approxHTML(v)}</div>`;
    }).join("")}</div>${this.opt.hint ? `<div class="hint">${this.opt.hint}</div>` : ""}</div>`;
  }
  after(el) { const on = el.querySelector(".rlist .on"), ml = el.querySelector(".rlist"); if (on && ml) { const t = on.offsetTop - ml.offsetTop; if (t < ml.scrollTop) ml.scrollTop = t; else if (t + on.offsetHeight > ml.scrollTop + ml.clientHeight) ml.scrollTop = t + on.offsetHeight - ml.clientHeight; } }
  key(k) {
    if (k === "up") this.sel = Math.max(0, this.sel - 1);
    else if (k === "down") this.sel = Math.min(this.lines.length - 1, this.sel + 1);
    else if (k === "exe" && this.opt.onExe) this.opt.onExe();
    else if (k === "ac" || k === "exe" || k === "left" || k === "ok") App.pop();
    return true;
  }
  tap(i) { this.sel = Number(i); }
  tools() { return this.opt.tools ? this.opt.tools() : null; }
}
/* ---------------- màn hình tính toán ---------------- */
const FORMATS = [["Chuẩn", "std"], ["Thập phân", "dec"], ["Phân số", "improper"], ["Hỗn số", "mixed"], ["Thừa số nguyên tố", "prime"], ["Độ ° ′ ″", "dms"], ["Kỹ thuật (ENG)", "eng"], ["Thập phân tuần hoàn", "rec"]];
const BASEN_KEYS = { xvar: "A", frac: "B", sqrt: "C", sq: "D", pow: "E", log: "F" };
class CalcScr extends Scr {
  constructor(app) { super(); this.app = app; this.ed = new Editor(); this.mode = "edit"; this.res = null; this.rmode = "std"; this.last = null; this.hi = -1; this.note = ""; }
  render() {
    if (this.mode === "err") return new ErrScr(this.err.kind, this.err.msg).render().replace("[AC] / [BACK] : Quay lại", "[AC] : Hủy &nbsp; [◀][▶] : Sửa");
    let out = "";
    if (this.mode === "res") out = this.app === "basen" ? this.baseHTML() : formatValue(this.res, App.S, this.rmode);
    let hint = "";
    if (this.mode === "edit" && this.ed.empty) {
      if (this.app === "basen") hint = `<div class="hint">x→A ■/□→B √→C x²→D x^→E log→F · FORMAT: đổi hệ</div>`;
      else if (this.app === "matrix") hint = `<div class="hint">TOOLS: định nghĩa ma trận · VARIABLE: chèn MatA…</div>`;
      else if (this.app === "vector") hint = `<div class="hint">TOOLS: định nghĩa vectơ · VARIABLE: chèn VctA…</div>`;
      else if (this.app === "cmplx") hint = `<div class="hint">SHIFT °′″ → <i>i</i> · CATALOG: Arg, Conjg…</div>`;
    }
    return `<div class="cs${this.mode === "res" ? " done" : ""}"><div class="in nd">${this.mode === "edit" ? this.ed.html(true) : itemsHTML(this.last || [])}</div>${hint}<div class="out nd">${out}</div>${this.note ? `<div class="note">${this.note}</div>` : ""}</div>`;
  }
  after(el) {
    const inp = el.querySelector(".in"), cur = el.querySelector(".cur");
    if (inp && cur) { const x = cur.getBoundingClientRect().left - inp.getBoundingClientRect().left + inp.scrollLeft; if (x > inp.scrollLeft + inp.clientWidth - 14) inp.scrollLeft = x - inp.clientWidth + 24; else if (x < inp.scrollLeft + 6) inp.scrollLeft = Math.max(0, x - 24); }
    const out = el.querySelector(".out");
    if (out) { let fs = 26; out.style.fontSize = fs + "px"; while (out.scrollWidth > out.clientWidth + 1 && fs > 13) { fs -= 2; out.style.fontSize = fs + "px"; } }
  }
  baseHTML() {
    const b = BASES[App.base], main = baseStr(this.res, b);
    const others = Object.entries(BASES).filter(([n]) => n !== App.base).map(([n, bb]) => `<span><b>${n}</b> ${baseStr(this.res, bb)}</span>`).join("");
    return `<div class="bn">${main}</div><div class="bno">${others}</div>`;
  }
  begin(k) { // sau khi có kết quả: bắt đầu biểu thức mới
    if (this.mode === "res" || this.mode === "err") {
      this.ed = new Editor(); if (this.mode === "res" && POSTFIX_KEYS.has(k) && this.app !== "basen") this.ed.insert(CH("Ans"));
      this.mode = "edit";
    }
    this.note = ""; this.hi = -1;
  }
  feed(sp) { this.begin(sp.c === "!" || sp.tpl === "pow" ? "pow" : ""); applySpec(this.ed, sp); }
  key(k) {
    if (this.mode === "err") {
      if (k === "ac") { this.mode = "edit"; this.ed = new Editor(); }
      else if (k === "left" || k === "right" || k === "del") { this.mode = "edit"; if (k === "right") this.ed.home(); else this.ed.end(); }
      return true;
    }
    if (this.app === "basen" && BASEN_KEYS[k]) { this.begin(k); this.ed.insert(CH(BASEN_KEYS[k])); return true; }
    switch (k) {
      case "exe": this.calc(); return true;
      case "approx": this.calc("dec"); return true;
      case "ac": this.ed = new Editor(); this.mode = "edit"; this.note = ""; this.hi = -1; return true;
      case "format": this.formatMenu(); return true;
    }
    if (this.mode === "res") {
      if (k === "left" || k === "right" || k === "del") { this.ed = new Editor(this.last); if (k === "right") this.ed.home(); this.mode = "edit"; if (k === "del") this.ed.del(); return true; }
      if (k === "up" || k === "down") { this.browse(k); return true; }
    }
    if (this.mode === "edit" && (k === "up" || k === "down")) {
      if (this.ed.vert(k)) return true;
      if (k === "up") this.browse(k); return true;
    }
    if (this.app === "basen" && !/^[0-9]$/.test(k) && !["add", "sub", "mul", "div", "lp", "rp", "neg", "left", "right", "del", "undo", "ans"].includes(k)) return true;
    if (KEYSPEC[k] || ["left", "right", "del", "undo"].includes(k)) {
      if (k === "left" || k === "right" || k === "del" || k === "undo") { editKey(this.ed, k); return true; }
      this.begin(k); editKey(this.ed, k); return true;
    }
    return false;
  }
  browse(k) {
    const H = App.hist.map((h, i) => [h, i]).filter(([h]) => h.app === this.app);
    if (!H.length) return;
    let p = this.hi < 0 ? H.length : H.findIndex(([, i]) => i === this.hi);
    if (p < 0) p = H.length;
    p += k === "up" ? -1 : 1;
    if (p < 0) p = 0;
    if (p >= H.length) { this.hi = -1; if (this.mode === "res") return; return; }
    const [h, i] = H[p]; this.hi = i; this.last = clone(h.items); this.res = h.v; this.rmode = "std"; this.mode = "res";
  }
  formatMenu() {
    if (this.app === "basen") {
      App.push(new MenuScr("Hệ cơ số", Object.keys(BASES).map(b => ({ label: b + { DEC: " (thập phân)", HEX: " (thập lục phân)", BIN: " (nhị phân)", OCT: " (bát phân)" }[b], mark: App.base === b, act: () => { App.base = b; App.closeMenus(); App.save(); } }))));
      return;
    }
    App.push(new MenuScr("FORMAT", FORMATS.map(([n, m]) => ({ label: n, act: () => { App.closeMenus(); if (this.mode !== "res") this.calc(); if (this.mode === "res") this.applyFormat(m); } }))));
  }
  applyFormat(m) {
    this.note = "";
    const v = this.res;
    if (m === "prime" && !(v.k === "q" && v.q.isInt && v.q.n > 1n && v.q.n <= 9999999999n)) { this.note = "Chỉ phân tích số nguyên 2 … 9 999 999 999"; return; }
    if ((m === "improper" || m === "mixed") && v.k !== "q") { const g = v.k === "f" ? qFromFloat(v.v, 100000, 1e-10) : null; if (!g) { this.note = "Không biểu diễn được dạng phân số"; this.rmode = "dec"; return; } this.res = V.q(g); }
    if (m === "rec" && !(v.k === "q" && !v.q.isInt)) { this.note = "Không có dạng tuần hoàn"; }
    if (v.k === "list" || v.k === "qr" || isMV(v)) m = m === "dec" ? "dec" : "std";
    this.rmode = m;
  }
  calc(fm) {
    let items = this.ed.root;
    if (this.mode === "res") items = this.last || [];
    if (!items.length) { if (!this.last) return; items = this.last; }
    this.note = "";
    try {
      let v;
      if (this.app === "basen") v = baseEval(items, BASES[App.base], App.ans && App.ans.k === "q" && App.ans.q.isInt ? App.ans.q.n : 0n);
      else if (this.app === "calc" && hasTopEq(items)) v = solveItems(items);
      else v = App.evalItems(items);
      this.res = v; this.last = clone(items); this.mode = "res"; this.rmode = fm || "std"; this.hi = -1;
      if (this.app === "basen") { const vv = V.q(new Q(v)); App.setAns(vv); App.hist.push({ items: clone(items), v: vv, app: this.app }); }
      else { App.setAns(v); if (v.k !== "list" || this.app === "calc") App.hist.push({ items: clone(items), v, app: this.app }); }
      if (App.hist.length > 60) App.hist.shift();
      App.save(); renderSide();
    } catch (e) {
      if (!(e instanceof CalcErr)) console.error(e);
      this.err = { kind: e.kind || "Math", msg: e instanceof CalcErr && e.message !== e.kind ? e.message : "" }; this.mode = "err";
      this.ed = new Editor(items);
    }
  }
  tools() {
    const items = [{ label: "Xóa lịch sử tính", act: () => { App.hist = App.hist.filter(h => h.app !== this.app); App.save(); renderSide(); App.closeMenus(); } }];
    if (this.app === "cmplx") items.unshift({ label: "Kết quả dạng a+b<i>i</i>", mark: App.S.cform !== "polar", act: () => { App.S.cform = "rect"; App.save(); App.closeMenus(); } }, { label: "Kết quả dạng r∠θ", mark: App.S.cform === "polar", act: () => { App.S.cform = "polar"; App.save(); App.closeMenus(); } });
    if (this.app === "matrix") items.unshift({ label: "Định nghĩa ma trận", sub: 1, act: () => matPick("def") }, { label: "Sửa ma trận", sub: 1, act: () => matPick("edit") }, { label: "Xóa tất cả ma trận", act: () => { App.mats = {}; App.save(); App.closeMenus(); } });
    if (this.app === "vector") items.unshift({ label: "Định nghĩa vectơ", sub: 1, act: () => vctPick("def") }, { label: "Sửa vectơ", sub: 1, act: () => vctPick("edit") }, { label: "Xóa tất cả vectơ", act: () => { App.vcts = {}; App.save(); App.closeMenus(); } });
    if (this.app === "basen") items.unshift(...Object.keys(BASES).map(b => ({ label: "Hệ " + b, mark: App.base === b, act: () => { App.base = b; App.save(); App.closeMenus(); } })));
    if (this.app === "calc") items.push({ label: "Mẹo nhập nhanh", act: () => { App.closeMenus(); App.push(helpScr()); } });
    return items;
  }
}
function niceRoot(r) { // nhận dạng nghiệm hữu tỉ hoặc ±√q
  const v = niceFloat(r, 1e-10); if (v.k !== "f") return v;
  const q = qFromFloat(r * r, 10000, 1e-11);
  if (q) { let s = sqrtV(V.q(q)); if (r < 0) s = neg(s); if (Math.abs(toNum(s) - r) < 1e-9 * Math.max(1, Math.abs(r))) return s; }
  return v;
}
function hasTopEq(items) { return items.some(it => it.t === "c" && it.v === "="); }
function solveItems(items) { // Calculate: biểu thức chứa "=" → giải theo x (Solver)
  const k = items.findIndex(it => it.t === "c" && it.v === "=");
  const L = items.slice(0, k), R = items.slice(k + 1);
  if (!L.length || !R.length || hasTopEq(R)) ERR("Syntax");
  const nL = parseItems(L), nR = parseItems(R), env = App.env();
  const f = t => { const b = { ...env, bind: { x: V.f(t) } }; return toNum(evalNode(nL, b)) - toNum(evalNode(nR, b)); };
  const x0 = App.vars.x ? toNum(App.vars.x) : 0, r = solveEq(f, x0), xv = niceRoot(r);
  App.vars.x = xv;
  const lr = f(toNum(xv)), sc = Math.max(1, ...[toNum(evalNode(nL, { ...env, bind: { x: xv } })), toNum(evalNode(nR, { ...env, bind: { x: xv } }))].map(Math.abs));
  return { k: "list", items: [["x", xv], ["L−R", Math.abs(lr) < 1e-13 * sc ? V.int(0) : V.f(lr)]] };
}
/* ---------------- biểu mẫu nhập ---------------- */
class FormScr extends Scr {
  constructor(id, title, fields, onSubmit, opt = {}) {
    super(); this.id = id; this.title = title; this.fields = fields; this.onSubmit = onSubmit; this._i = 0; this.fresh = true; this.opt = opt;
    const saved = App.forms[id] || {};
    this.eds = fields.map(f => {
      if (f.type === "choice") { f.val = saved[f.key] != null ? saved[f.key] : f.opts[0][1]; return null; }
      if (f.bind) return new Editor(f.bind());
      return new Editor(saved[f.key] || strItems(f.def != null ? f.def : ""));
    });
  }
  render() {
    const rows = this.fields.map((f, i) => {
      const act = i === this.i; let v;
      if (f.type === "choice") v = `<span class="ch">${act ? "◀ " : ""}${f.opts.find(o => o[1] === f.val)[0]}${act ? " ▶" : ""}</span>`;
      else v = act ? this.eds[i].html(true) : this.eds[i].empty ? `<span class="dim">${f.optional ? "(trống)" : "?"}</span>` : itemsHTML(this.eds[i].root);
      return `<div class="fo${act ? " on" : ""}${f.type === "raw" ? " raw" : ""}" data-tap="${i}"><span class="fl">${f.label}</span><span class="fv nd">${v}</span></div>`;
    }).join("");
    return `<div class="form">${this.title ? `<div class="mt">${this.title}</div>` : ""}<div class="fl-list">${rows}</div><div class="hint">${this.opt.hint || "EXE: ô tiếp theo · OK: tính"}</div></div>`;
  }
  after(el) {
    const on = el.querySelector(".fo.on"), ml = el.querySelector(".fl-list");
    if (on && ml) { const t = on.offsetTop - ml.offsetTop; if (t < ml.scrollTop) ml.scrollTop = t; else if (t + on.offsetHeight > ml.scrollTop + ml.clientHeight) ml.scrollTop = t + on.offsetHeight - ml.clientHeight; }
    const fv = on && on.querySelector(".fv"), cur = on && on.querySelector(".cur");
    if (fv && cur) { const x = cur.getBoundingClientRect().left - fv.getBoundingClientRect().left + fv.scrollLeft; if (x > fv.scrollLeft + fv.clientWidth - 10) fv.scrollLeft = x - fv.clientWidth + 20; else if (x < fv.scrollLeft) fv.scrollLeft = Math.max(0, x - 20); }
  }
  get ed() { return this.eds[this.i]; }
  get i() { return this._i; }
  set i(v) { if (v !== this._i) this.fresh = true; this._i = v; }
  feed(sp) { if (this.ed) applySpec(this.ed, sp); }
  persist() {
    const o = App.forms[this.id] = App.forms[this.id] || {};
    this.fields.forEach((f, i) => { if (f.type === "choice") o[f.key] = f.val; else if (f.bind) f.store(this.eds[i].root); else o[f.key] = clone(this.eds[i].root); });
    App.save();
  }
  values() {
    const vals = {};
    this.fields.forEach((f, i) => {
      if (f.type === "choice") { vals[f.key] = f.val; return; }
      const it = this.eds[i].root;
      if (f.type === "raw") { vals[f.key] = clone(it); return; }
      if (!it.length) { if (f.optional) { vals[f.key] = null; return; } this.i = i; ERR("Syntax", "Chưa nhập " + f.label.replace(/<[^>]+>/g, "").replace(/[=:]\s*$/, "")); }
      try { vals[f.key] = App.evalItems(it); } catch (e) { this.i = i; throw e; }
      if (vals[f.key].k === "list" || vals[f.key].k === "qr") ERR("Syntax");
    });
    return vals;
  }
  submit() { this.persist(); App.run(() => { const r = this.onSubmit(this.values(), this); if (r) App.push(r); }); }
  key(k) {
    const f = this.fields[this.i];
    if (k === "ok") { this.submit(); return true; }
    if (k === "exe") {
      if (f.type === "expr" && this.ed.root.length) { const r = App.run(() => App.evalItems(this.ed.root)); if (r === null) return true; }
      if (this.i < this.fields.length - 1) this.i++; else this.submit();
      this.persist(); return true;
    }
    if (k === "up" || k === "down") { if (this.ed && this.ed.vert(k)) return true; this.i = (this.i + (k === "up" ? -1 : 1) + this.fields.length) % this.fields.length; return true; }
    if (f.type === "choice") {
      if (k === "left" || k === "right") { const ix = f.opts.findIndex(o => o[1] === f.val), n = f.opts.length; f.val = f.opts[(ix + (k === "left" ? -1 : 1) + n) % n][1]; }
      else if (/^[1-9]$/.test(k) && Number(k) <= f.opts.length) f.val = f.opts[Number(k) - 1][1];
      return true;
    }
    if (k === "ac") { if (this.ed.empty) App.pop(); else this.ed.clear(); return true; }
    if (this.fresh && KEYSPEC[k] && f.type !== "raw" && !POSTFIX_KEYS.has(k)) this.ed.set([]); // gõ mới thay giá trị cũ
    this.fresh = false;
    return editKey(this.ed, k);
  }
  tap(i) { this.i = Number(i); }
  tools() { return this.opt.tools ? this.opt.tools() : null; }
}
/* ---------------- bảng (dữ liệu, ma trận, hệ số) ---------------- */
class GridScr extends Scr {
  /* cols: [{name, i}] · rows: mảng hàng (tham chiếu) · opt: {fixed, max, dir, onExe, tools, onChange, head, ro, newRow, hint} */
  constructor(title, cols, rows, opt = {}) { super(); this.title = title; this.cols = cols; this.rows = rows; this.opt = opt; this.r = 0; this.c = 0; this.ed = null; this.msg = ""; }
  get nrows() { return this.rows.length + (this.opt.fixed || this.opt.ro || this.rows.length >= (this.opt.max || 99) ? 0 : 1); }
  cell(r, c) { const row = this.rows[r]; return row ? row[this.cols[c].i] : null; }
  render() {
    const head = `<tr class="hd"><th></th>${this.cols.map((c, j) => `<th class="${j === this.c ? "on" : ""}">${c.name}</th>`).join("")}</tr>`;
    let body = "";
    for (let r = 0; r < this.nrows; r++) body += `<tr><th>${r + 1}</th>${this.cols.map((c, j) => `<td data-tap="${r},${j}" class="${r === this.r && j === this.c ? "on" : ""}">${r < this.rows.length ? cellText(this.cell(r, j)) : ""}</td>`).join("")}</tr>`;
    let bottom;
    if (this.ed) bottom = `<div class="gb nd edit">${this.ed.html(true)}</div>`;
    else { const v = this.cell(this.r, this.c); bottom = `<div class="gb nd"><span class="gl">${this.cols[this.c].name}${this.r + 1}=</span>${v != null ? fmt(v) : ""}</div>`; }
    return `<div class="grid">${this.title ? `<div class="mt">${this.title}</div>` : ""}${this.opt.head ? `<div class="gh nd">${this.opt.head}</div>` : ""}<div class="gw"><table>${head}${body}</table></div>${this.msg ? `<div class="note">${this.msg}</div>` : ""}${bottom}${this.opt.hint ? `<div class="hint">${this.opt.hint}</div>` : ""}</div>`;
  }
  after(el) {
    const on = el.querySelector("td.on"), w = el.querySelector(".gw");
    if (on && w) {
      const tr = on.parentElement, t = tr.offsetTop - (w.querySelector("tr").offsetHeight || 0);
      if (tr.offsetTop - w.scrollTop < w.querySelector("tr").offsetHeight) w.scrollTop = Math.max(0, t);
      else if (tr.offsetTop + tr.offsetHeight > w.scrollTop + w.clientHeight) w.scrollTop = tr.offsetTop + tr.offsetHeight - w.clientHeight;
      if (on.offsetLeft < w.scrollLeft + 24) w.scrollLeft = Math.max(0, on.offsetLeft - 24); else if (on.offsetLeft + on.offsetWidth > w.scrollLeft + w.clientWidth) w.scrollLeft = on.offsetLeft + on.offsetWidth - w.clientWidth;
    }
    const gb = el.querySelector(".gb"), cur = gb && gb.querySelector(".cur");
    if (gb && cur) { const x = cur.getBoundingClientRect().left - gb.getBoundingClientRect().left + gb.scrollLeft; if (x > gb.scrollLeft + gb.clientWidth - 10) gb.scrollLeft = x - gb.clientWidth + 20; }
  }
  feed(sp) { if (this.opt.ro) return; if (!this.ed) this.ed = new Editor(); applySpec(this.ed, sp); }
  commit() {
    if (!this.ed) return true;
    if (!this.ed.root.length) { this.ed = null; return true; }
    try {
      const v = App.evalItems(this.ed.root);
      if (v.k === "list" || v.k === "qr" || isMV(v)) ERR("Syntax");
      if (this.opt.real && v.k === "c") ERR("Math", "Chỉ nhận số thực");
      if (this.r >= this.rows.length) this.rows.push(this.opt.newRow ? this.opt.newRow() : this.cols.map(() => V.int(0)));
      this.rows[this.r][this.cols[this.c].i] = v; this.ed = null; this.msg = "";
      if (this.opt.onChange) this.opt.onChange();
      return true;
    } catch (e) { this.msg = (e.kind || "Math") + " ERROR" + (e instanceof CalcErr && e.message !== e.kind ? " · " + esc(e.message) : ""); return false; }
  }
  move(dr, dc) { this.r = Math.max(0, Math.min(this.nrows - 1, this.r + dr)); this.c = Math.max(0, Math.min(this.cols.length - 1, this.c + dc)); }
  key(k) {
    this.msg = this.msg && this.ed ? this.msg : "";
    if (this.ed) {
      if (k === "exe" || k === "ok") { if (this.commit()) this.advance(); return true; }
      if (k === "ac") { this.ed = null; this.msg = ""; return true; }
      if ((k === "up" || k === "down") && !this.ed.vert(k)) { if (this.commit()) this.move(k === "up" ? -1 : 1, 0); return true; }
      if (k === "del" && this.ed.empty) { this.ed = null; return true; }
      return editKey(this.ed, k);
    }
    switch (k) {
      case "up": this.move(-1, 0); return true; case "down": this.move(1, 0); return true;
      case "left": this.move(0, -1); return true; case "right": this.move(0, 1); return true;
      case "exe": if (this.opt.onExe) this.opt.onExe(this); return true;
      case "ok": if (this.opt.ro) { if (this.opt.onExe) this.opt.onExe(this); return true; } { const v = this.cell(this.r, this.c); this.ed = new Editor(v ? valueItems(v) : []); } return true;
      case "ac": App.pop(); return true;
      case "del":
        if (this.opt.ro) return true;
        if (!this.opt.fixed && this.r < this.rows.length) { this.rows.splice(this.r, 1); this.move(0, 0); }
        else if (this.r < this.rows.length) this.rows[this.r][this.cols[this.c].i] = V.int(0);
        if (this.opt.onChange) this.opt.onChange(); return true;
    }
    if (this.opt.ro) return true;
    if (KEYSPEC[k]) { this.ed = new Editor(); editKey(this.ed, k); return true; }
    return false;
  }
  advance() {
    if (this.opt.dir === "right") {
      if (this.c < this.cols.length - 1) this.c++;
      else if (this.r < this.nrows - 1) {
        this.r++; this.c = 0;
        if (this.opt.prefill != null && this.r >= this.rows.length && this.rows.length) { this.rows.push(this.opt.newRow()); this.c = this.opt.prefill; if (this.opt.onChange) this.opt.onChange(); }
      }
    }
    else this.move(1, 0);
  }
  tap(v) { const [r, c] = v.split(",").map(Number); if (this.ed && !this.commit()) return; this.r = r; this.c = c; }
  tools() { return this.opt.tools ? this.opt.tools(this) : null; }
}
/* ---------------- màn hình HOME & ứng dụng ---------------- */
const APPS = {
  calc: { name: "Tính toán", en: "Calculate", ic: "<b>+−</b><b>×÷</b>", tag: "" },
  stat: { name: "Thống kê", en: "Statistics", ic: '<svg viewBox="0 0 24 24"><path d="M3 20h18M6 17V10M11 17V5M16 17v-5M20 17V8"/></svg>', tag: "STAT" },
  dist: { name: "Phân phối", en: "Distribution", ic: '<svg viewBox="0 0 24 24"><path d="M2 19C7 19 8 5 12 5s5 14 10 14"/></svg>', tag: "DIST" },
  table: { name: "Bảng giá trị", en: "Table", ic: "<b><i>f</i>(<i>x</i>)</b><small>▦</small>", tag: "TABLE" },
  eqn: { name: "Phương trình", en: "Equation", ic: "<b><i>x</i>=</b><small>?</small>", tag: "EQN" },
  ineq: { name: "Bất phương trình", en: "Inequality", ic: "<b><i>x</i>&gt;</b><small>0</small>", tag: "INEQ" },
  cmplx: { name: "Số phức", en: "Complex", ic: "<b><i>a</i>+<i>bi</i></b>", tag: "CMPLX" },
  basen: { name: "Hệ cơ số", en: "Base-N", ic: "<b>0b</b><small>HEX</small>", tag: "BASE" },
  matrix: { name: "Ma trận", en: "Matrix", ic: "<b>[A]</b>", tag: "MAT" },
  vector: { name: "Vectơ", en: "Vector", ic: "<small>→</small><b><i>v</i></b>", tag: "VCT" },
  ratio: { name: "Tỉ lệ thức", en: "Ratio", ic: "<b>a:b</b>", tag: "RATIO" },
  mathbox: { name: "Hộp toán", en: "Math Box", ic: '<svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="3"/><circle cx="9" cy="9" r="1.3"/><circle cx="15" cy="15" r="1.3"/><circle cx="15" cy="9" r="1.3"/><circle cx="9" cy="15" r="1.3"/></svg>', tag: "BOX" },
  geo: { name: "Hình học & Xác suất", en: "Plus tools", ic: '<svg viewBox="0 0 24 24"><path d="M4 19L12 5l8 14z"/><path d="M8 19a4 4 0 0 1 2-3.4"/></svg>', tag: "PLUS" }
};
const APP_ORDER = Object.keys(APPS);
class HomeScr extends Scr {
  constructor() { super(); this.sel = Math.max(0, APP_ORDER.indexOf(App.app)); this.home = true; }
  render() {
    const a = APPS[APP_ORDER[this.sel]];
    return `<div class="home"><div class="hg">${APP_ORDER.map((id, i) => `<div class="ha${i === this.sel ? " on" : ""}" data-tap="${i}"><span class="hi">${APPS[id].ic}</span></div>`).join("")}</div><div class="hn"><b>${a.name}</b><span>${a.en}</span></div></div>`;
  }
  after(el) { const on = el.querySelector(".ha.on"), g = el.querySelector(".hg"); if (on && g) { if (on.offsetTop - g.offsetTop < g.scrollTop) g.scrollTop = on.offsetTop - g.offsetTop; else if (on.offsetTop - g.offsetTop + on.offsetHeight > g.scrollTop + g.clientHeight) g.scrollTop = on.offsetTop - g.offsetTop + on.offsetHeight - g.clientHeight; } }
  key(k) {
    const n = APP_ORDER.length, C = 4;
    if (k === "left") this.sel = (this.sel - 1 + n) % n; else if (k === "right") this.sel = (this.sel + 1) % n;
    else if (k === "up") this.sel = this.sel - C >= 0 ? this.sel - C : this.sel; else if (k === "down") this.sel = Math.min(n - 1, this.sel + C);
    else if (k === "ok" || k === "exe") openApp(APP_ORDER[this.sel]);
    else if (/^[1-9]$/.test(k) && Number(k) <= n) { this.sel = Number(k) - 1; }
    return true;
  }
  tap(i) { if (this.sel === Number(i)) openApp(APP_ORDER[this.sel]); else this.sel = Number(i); }
}
function openApp(id) {
  App.app = id; App.save();
  const home = App.stack[0] && App.stack[0].home ? App.stack[0] : new HomeScr();
  home.sel = APP_ORDER.indexOf(id);
  App.stack = [home, mainScreen(id)];
  renderSide();
}
function mainScreen(id) {
  if (["calc", "cmplx", "basen", "matrix", "vector"].includes(id)) return App.screens[id] || (App.screens[id] = new CalcScr(id));
  return ({ stat: statMenu, dist: distMenu, table: tableForm, eqn: eqnMenu, ineq: ineqMenu, ratio: ratioMenu, mathbox: boxMenu, geo: geoMenu })[id]();
}
/* ---------- SETTINGS ---------- */
function settingsMenu() {
  const S = App.S, set = (k, v) => () => { S[k] = v; App.save(); App.closeMenus(); };
  const digits = (kind) => new MenuScr(kind === "fix" ? "Fix: số chữ số thập phân" : "Sci: số chữ số có nghĩa", Array.from({ length: 10 }, (_, i) => ({ label: String(i === 0 && kind === "sci" ? 10 : i), mark: S.fmt === kind && S.fmtN === (kind === "sci" && i === 0 ? 10 : i), act: () => { S.fmt = kind; S.fmtN = kind === "sci" && i === 0 ? 10 : i; App.save(); App.closeMenus(); } })));
  return new MenuScr("SETTINGS", [
    { label: "Nhập/Xuất", sub: 1, act: () => App.push(new MenuScr("Nhập/Xuất", [{ label: "MathI/MathO", mark: S.io === "mathO", act: set("io", "mathO") }, { label: "MathI/DecimalO", mark: S.io === "decO", act: set("io", "decO") }])) },
    { label: "Đơn vị góc", sub: 1, act: () => App.push(new MenuScr("Đơn vị góc", [{ label: "Độ (D)", mark: S.ang === "D", act: set("ang", "D") }, { label: "Radian (R)", mark: S.ang === "R", act: set("ang", "R") }, { label: "Gradian (G)", mark: S.ang === "G", act: set("ang", "G") }])) },
    { label: "Định dạng số", sub: 1, act: () => App.push(new MenuScr("Định dạng số", [{ label: "Norm 1", mark: S.fmt === "norm1", act: set("fmt", "norm1") }, { label: "Norm 2", mark: S.fmt === "norm2", act: set("fmt", "norm2") }, { label: "Fix", sub: 1, mark: S.fmt === "fix", act: () => App.push(digits("fix")) }, { label: "Sci", sub: 1, mark: S.fmt === "sci", act: () => App.push(digits("sci")) }])) },
    { label: "Kết quả phân số", sub: 1, act: () => App.push(new MenuScr("Kết quả phân số", [{ label: "Phân số (<i>d</i>/<i>c</i>)", mark: S.frac === "improper", act: set("frac", "improper") }, { label: "Hỗn số (<i>a</i>⌟<i>b</i>/<i>c</i>)", mark: S.frac === "mixed", act: set("frac", "mixed") }])) },
    { label: "Số phức", sub: 1, act: () => App.push(new MenuScr("Dạng số phức", [{ label: "<i>a</i>+<i>bi</i>", mark: S.cform !== "polar", act: set("cform", "rect") }, { label: "<i>r</i>∠<i>θ</i>", mark: S.cform === "polar", act: set("cform", "polar") }])) },
    { label: "Phân cách hàng nghìn", sub: 1, act: () => App.push(new MenuScr("Phân cách hàng nghìn", [{ label: "Bật", mark: S.sep, act: set("sep", true) }, { label: "Tắt", mark: !S.sep, act: set("sep", false) }])) },
    { label: "Khôi phục", sub: 1, act: () => App.push(new MenuScr("Khôi phục", [
      { label: "Cài đặt về mặc định", act: () => { App.S = { ...DEF_S }; App.save(); App.closeMenus(); } },
      { label: "Xóa biến & Ans", act: () => { App.vars = {}; App.ans = App.preAns = null; App.save(); App.closeMenus(); } },
      { label: "Khôi phục tất cả", act: () => { try { localStorage.removeItem(LS_KEY); } catch (e) {} location.reload(); } }])) }
  ]);
}
/* ---------- VARIABLE ---------- */
const VAR_LIST = ["A", "B", "C", "D", "E", "F", "x", "y", "z"];
function storeValue() { // giá trị hiện tại của màn hình (để STO)
  const t = App.target();
  if (t instanceof CalcScr) {
    if (t.mode === "edit" && t.ed.root.length) { t.calc(); if (t.mode !== "res") return null; }
    if (t.mode === "res") { let v = t.res; if (t.app === "basen") v = V.q(new Q(v)); if (v.k === "list") v = v.items[0][1]; if (v.k === "qr") v = v.q; return v; }
  }
  return App.ans || V.int(0);
}
function doStore(name) {
  App.closeMenus(); const v = storeValue(); if (!v) return;
  if (isMV(v)) { App.push(new ErrScr("Math", "Biến chỉ lưu được số")); return; }
  App.vars[name] = v.k === "cx" ? V.c(toNum(v.re), toNum(v.im)) : v; App.save();
  const t = App.target(); if (t instanceof CalcScr) t.note = `Đã lưu → <i>${name}</i>`;
}
function variableMenu(store) {
  if (App.app === "matrix" && !store) return matPick("var");
  if (App.app === "vector" && !store) return vctPick("var");
  return new MenuScr(store ? "STO: lưu vào biến" : "VARIABLE", VAR_LIST.map(n => ({
    label: `<i class="var">${n}</i><span class="vv">= ${cellText(App.vars[n] || V.int(0))}</span>`,
    act: () => store ? doStore(n) : App.push(new MenuScr("Biến " + n, [
      { label: "Gọi (chèn <i>" + n + "</i>)", act: () => App.feed({ c: n }) },
      { label: "Lưu kết quả vào <i>" + n + "</i>", act: () => doStore(n) },
      { label: "Xóa <i>" + n + "</i> (= 0)", act: () => { delete App.vars[n]; App.save(); App.closeMenus(); } }]))
  })));
}
/* ---------- FUNCTION ---------- */
function defineFn(n) {
  return new FormScr("def" + n, "Định nghĩa " + n + "(x)", [{ label: `<i>${n}</i>(<i>x</i>)=`, key: "fx", type: "raw", bind: () => App.funcs[n], store: it => { App.funcs[n] = clone(it); } }],
    (v, form) => { App.funcs[n] = v.fx; if (v.fx.length) parseItems(v.fx); App.save(); App.pop(); return null; }, { hint: "Nhập biểu thức theo <i>x</i> · EXE/OK: lưu" });
}
function functionMenu() {
  const show = n => (App.funcs[n].length ? itemsHTML(App.funcs[n]) : '<span class="dim">chưa định nghĩa</span>');
  return new MenuScr("FUNCTION", [
    { label: `<i>f</i>(<i>x</i>) <span class="vv nd">= ${show("f")}</span>`, act: () => App.feed({ f: "f" }) },
    { label: `<i>g</i>(<i>x</i>) <span class="vv nd">= ${show("g")}</span>`, act: () => App.feed({ f: "g" }) },
    { label: "Định nghĩa <i>f</i>(<i>x</i>)", act: () => { App.closeMenus(); App.push(defineFn("f")); } },
    { label: "Định nghĩa <i>g</i>(<i>x</i>)", act: () => { App.closeMenus(); App.push(defineFn("g")); } }
  ]);
}
/* ---------- CATALOG ---------- */
function catalogMenu() {
  const I = (label, sp) => ({ label, act: () => App.feed(sp) });
  const cats = [];
  if (App.app === "basen") cats.push(["Logic & dấu", [I("and", { c: "and" }), I("or", { c: "or" }), I("xor", { c: "xor" }), I("xnor", { c: "xnor" }), I("Not(", { f: "Not" }), I("Neg(", { f: "Neg" })]]);
  if (App.app === "matrix") cats.push(["Ma trận", ["A", "B", "C", "D", "Ans"].map(n => I("Mat" + n, { c: "Mat" + n })).concat([I("det(", { f: "det" }), I("Trn(", { f: "Trn" }), I("Identity(", { f: "Identity" })])]);
  if (App.app === "vector") cats.push(["Vectơ", ["A", "B", "C", "D", "Ans"].map(n => I("Vct" + n, { c: "Vct" + n })).concat([I("dot( — tích vô hướng", { f: "dot" }), I("angle( — góc", { f: "angle" }), I("UnitV( — vectơ đơn vị", { f: "UnitV" }), I("|■| — độ dài", { tpl: "abs" })])]);
  if (App.app === "cmplx") cats.push(["Số phức", [I("<i>i</i>", { c: "i" }), I("Arg( — acgumen", { f: "Arg" }), I("Conjg( — liên hợp", { f: "Conjg" }), I("ReP( — phần thực", { f: "ReP" }), I("ImP( — phần ảo", { f: "ImP" }), I("∠", { c: "∠" }), I("|■| — môđun", { tpl: "abs" })]]);
  if (App.app !== "basen") cats.push(
    ["Phân tích hàm", [I("d/d<i>x</i>(■)", { tpl: "deriv" }), I("∫■d<i>x</i>", { tpl: "integ" }), I("Σ(■)", { tpl: "sum" }), I("Π(■)", { tpl: "prod" }), I("log<sub>■</sub>(■)", { tpl: "log" }), I("log( — log cơ số 10", { f: "log" }), I("ln(", { f: "ln" }), I("|■| — giá trị tuyệt đối", { tpl: "abs" })]],
    ["Xác suất", [I("<i>x</i>! — giai thừa", { c: "!" }), I("P — chỉnh hợp (nPr)", { c: "nPr" }), I("C — tổ hợp (nCr)", { c: "nCr" }), I("Ran# — số ngẫu nhiên", { c: "Ran#" }), I("RanInt#(a,b)", { f: "RanInt" })]],
    ["Số học", [I("GCD( — ƯCLN", { f: "GCD" }), I("LCM( — BCNN", { f: "LCM" }), I("Int( — phần nguyên", { f: "Int" }), I("Intg( — số nguyên lớn nhất ≤ x", { f: "Intg" }), I("Rnd( — làm tròn", { f: "Rnd" }), I("÷R — chia lấy dư", { c: "÷R" }), I("% — phần trăm", { c: "%" })]],
    ["Góc / Tọa độ", [I("° ′ ″ — độ phút giây", { c: "°" }), I("Pol( — đổi sang tọa độ cực", { f: "Pol" }), I("Rec( — đổi sang tọa độ vuông góc", { f: "Rec" }), I("π", { c: "π" })]],
    ["Hypebolic", ["sinh", "cosh", "tanh", "asinh", "acosh", "atanh"].map(f => I((FN_LABEL[f] || f) + "(", { f }))],
    ["Hằng số khoa học", Object.entries(SCI).map(([k, [h, v, d]]) => I(`<b class="kc">${h}</b> <small>${d}</small>`, { c: "k:" + k }))],
    ["Đổi đơn vị", Object.keys(CONV).map(k => I(esc(k), { c: k }))],
    ["Biến & bộ nhớ", [...VAR_LIST.map(n => I(`<i>${n}</i>`, { c: n })), I("Ans", { c: "Ans" }), I("PreAns", { c: "PreAns" }), I("<i>f</i>(", { f: "f" }), I("<i>g</i>(", { f: "g" })]]
  );
  return new MenuScr("CATALOG", cats.map(([n, items]) => ({ label: n, sub: 1, act: () => App.push(new MenuScr(n, items)) })));
}
function helpScr() {
  return new ResultScr("Mẹo nhập nhanh", [
    "■/□ sau một số: số đó thành tử số", "▲▼ di chuyển giữa tử và mẫu", "◀▶ ra/vào các khuôn (căn, lũy thừa…)", "Sau EXE: bấm + − × ÷ để tính tiếp với Ans",
    "▲ khi đang nhập: gọi lại phép tính trước", "SHIFT EXE (≈): kết quả thập phân", "FORMAT: đổi dạng hiển thị kết quả", "Biểu thức có “=”: giải tìm <i>x</i> (Solver)",
    "SHIFT Ans (STO): lưu vào biến", "SHIFT + phím xóa lùi (UNDO): hoàn tác", "Bàn phím: số, + − * / ^ ( ), Enter, Esc, ←→"
  ]);
}
/* ---------- Ma trận / Vectơ ---------- */
function matPick(mode) {
  const names = mode === "var" ? ["A", "B", "C", "D", "Ans"] : ["A", "B", "C", "D"];
  return (mode === "var" ? x => x : x => App.push(x))(new MenuScr(mode === "def" ? "Định nghĩa ma trận" : mode === "edit" ? "Sửa ma trận" : "Ma trận", names.map(n => {
    const m = App.mats[n];
    return {
      label: `Mat${n} <span class="vv">${m ? m.r + "×" + m.c : "—"}</span>`, act: () => {
        if (mode === "var") return App.push(new MenuScr("Mat" + n, [{ label: "Chèn Mat" + n, act: () => App.feed({ c: "Mat" + n }) }, ...(n !== "Ans" ? [{ label: "Sửa Mat" + n, act: () => { if (App.mats[n]) matEdit(n); else matDims(n); } }, { label: "Định nghĩa lại Mat" + n, act: () => matDims(n) }] : [])]));
        if (mode === "edit" && m) return matEdit(n);
        matDims(n);
      }
    };
  })));
}
function matDims(n) {
  App.push(new MenuScr("Mat" + n + ": số hàng", [1, 2, 3, 4].map(r => ({ label: r + " hàng", act: () => App.push(new MenuScr("Mat" + n + ": số cột", [1, 2, 3, 4].map(c => ({ label: c + " cột", act: () => { App.mats[n] = M(r, c, () => V.int(0)); App.save(); matEdit(n); } })))) })), { sel: 1 }));
}
function matEdit(n) {
  App.closeMenus(); const m = App.mats[n];
  App.push(new GridScr("Mat" + n + " (" + m.r + "×" + m.c + ")", Array.from({ length: m.c }, (_, i) => ({ name: String(i + 1), i })), m.a, { fixed: true, dir: "right", onChange: () => App.save(), hint: "EXE: ô tiếp · AC: xong", onExe: () => App.pop() }));
}
function vctPick(mode) {
  const names = mode === "var" ? ["A", "B", "C", "D", "Ans"] : ["A", "B", "C", "D"];
  return (mode === "var" ? x => x : x => App.push(x))(new MenuScr(mode === "def" ? "Định nghĩa vectơ" : mode === "edit" ? "Sửa vectơ" : "Vectơ", names.map(n => {
    const v = App.vcts[n];
    return {
      label: `Vct${n} <span class="vv">${v ? "dim " + v.a.length : "—"}</span>`, act: () => {
        if (mode === "var") return App.push(new MenuScr("Vct" + n, [{ label: "Chèn Vct" + n, act: () => App.feed({ c: "Vct" + n }) }, ...(n !== "Ans" ? [{ label: "Sửa Vct" + n, act: () => { if (App.vcts[n]) vctEdit(n); else vctDims(n); } }, { label: "Định nghĩa lại Vct" + n, act: () => vctDims(n) }] : [])]));
        if (mode === "edit" && v) return vctEdit(n);
        vctDims(n);
      }
    };
  })));
}
function vctDims(n) { App.push(new MenuScr("Vct" + n + ": số chiều", [2, 3].map(d => ({ label: d + " chiều", act: () => { App.vcts[n] = { k: "vec", a: Array.from({ length: d }, () => V.int(0)) }; App.save(); vctEdit(n); } })), { sel: 1 })); }
function vctEdit(n) {
  App.closeMenus(); const v = App.vcts[n], rows = [v.a];
  App.push(new GridScr("Vct" + n + " (" + v.a.length + " chiều)", v.a.map((_, i) => ({ name: ["x", "y", "z"][i], i })), rows, { fixed: true, dir: "right", onChange: () => App.save(), hint: "EXE: ô tiếp · AC: xong", onExe: () => App.pop() }));
}
/* ---------------- ứng dụng: Thống kê ---------------- */
const STAT_TYPES = [["1", "lin", "1 biến"], ["2", "lin", "<i>y</i>=<i>a</i>+<i>bx</i>"], ["2", "quad", "<i>y</i>=<i>a</i>+<i>bx</i>+<i>cx</i>²"], ["2", "ln", "<i>y</i>=<i>a</i>+<i>b</i>·ln<i>x</i>"], ["2", "exp", "<i>y</i>=<i>a</i>·e<sup><i>bx</i></sup>"], ["2", "abx", "<i>y</i>=<i>a</i>·<i>b</i><sup><i>x</i></sup>"], ["2", "pow", "<i>y</i>=<i>a</i>·<i>x</i><sup><i>b</i></sup>"], ["2", "inv", "<i>y</i>=<i>a</i>+<i>b</i>/<i>x</i>"], ["grp", "", "Dữ liệu ghép nhóm"]];
function statMenu() {
  return new MenuScr("Thống kê", STAT_TYPES.map(([kind, type, label]) => ({
    label, mark: App.stat.kind === kind && (kind !== "2" || App.stat.type === type), act: () => {
      if (kind !== "grp" && (App.stat.kind === "1") !== (kind === "1") && App.stat.kind !== "grp") { /* giữ cột x */ }
      if (kind !== "grp") { App.stat.kind = kind; App.stat.type = type; }
      App.save(); App.push(kind === "grp" ? grpGrid() : statGrid());
    }
  })));
}
function statGrid() {
  const st = App.stat, cols = [{ name: "<i>x</i>", i: 0 }];
  if (st.kind === "2") cols.push({ name: "<i>y</i>", i: 1 });
  if (st.freq) cols.push({ name: "Tần số", i: 2 });
  const title = st.kind === "1" ? "Thống kê 1 biến" : "Hồi quy " + STAT_TYPES.find(t => t[0] === "2" && t[1] === st.type)[2];
  return new GridScr(title, cols, st.rows, {
    max: 160, real: true, newRow: () => [V.int(0), V.int(0), V.int(1)], onChange: () => App.save(), hint: "EXE: tính · OK: sửa ô · TOOLS: tùy chọn",
    onExe: () => App.run(() => App.push(statResult())),
    tools: g => [
      { label: "Kết quả thống kê", act: () => { App.closeMenus(); App.run(() => App.push(statResult())); } },
      ...(st.kind === "2" ? [{ label: "Ước lượng <i>ŷ</i> từ <i>x</i>", act: () => { App.closeMenus(); App.push(estForm("y")); } }, ...(st.type !== "quad" ? [{ label: "Ước lượng <i>x̂</i> từ <i>y</i>", act: () => { App.closeMenus(); App.push(estForm("x")); } }] : [])] : []),
      { label: "Cột tần số: " + (st.freq ? "Bật → Tắt" : "Tắt → Bật"), act: () => { st.freq = !st.freq; App.save(); App.closeMenus(); App.pop(); App.push(statGrid()); } },
      { label: "Xóa toàn bộ dữ liệu", act: () => { st.rows.length = 0; g.r = 0; App.save(); App.closeMenus(); } },
      { label: "Chọn kiểu thống kê khác", act: () => { App.closeMenus(); App.pop(); } }
    ]
  });
}
function statData() {
  const st = App.stat; if (!st.rows.length) ERR("Math", "Chưa có dữ liệu — nhập số vào cột x");
  return { xs: st.rows.map(r => r[0]), ys: st.kind === "2" ? st.rows.map(r => r[1]) : null, fs: st.rows.map(r => (st.freq ? r[2] : V.int(1))) };
}
function statResult() {
  const d = statData(), r = statCalc(d.xs, d.ys, d.fs, App.stat.type), lines = r.list.slice();
  if (r.reg) { lines.unshift(`<b>${r.reg.eq}</b>`, ...r.reg.coef); lines.splice(1 + r.reg.coef.length, 0, "<b>Thống kê</b>"); }
  return new ResultScr(App.stat.kind === "1" ? "Kết quả 1 biến" : "Kết quả hồi quy", lines);
}
function estForm(which) {
  return new FormScr("est" + which, which === "y" ? "Ước lượng ŷ" : "Ước lượng x̂", [{ label: which === "y" ? "<i>x</i>=" : "<i>y</i>=", key: "v", def: "0" }], v => {
    const d = statData(), r = statCalc(d.xs, d.ys, d.fs, App.stat.type).reg, t = toNum(v.v);
    const out = which === "y" ? r.pred(t) : r.predX(t);
    if (!isFinite(out)) ERR("Math");
    return new ResultScr("", [[which === "y" ? "<i>ŷ</i>" : "<i>x̂</i>", niceFloat(out, 1e-11)]]);
  });
}
function grpGrid() {
  return new GridScr("Dữ liệu ghép nhóm [a; b)", [{ name: "Đầu <i>a</i>", i: 0 }, { name: "Đầu <i>b</i>", i: 1 }, { name: "Tần số", i: 2 }], App.grp, {
    max: 40, real: true, dir: "right", prefill: 2, newRow: () => { const L = App.grp[App.grp.length - 1]; return L ? [L[1], add(L[1], sub(L[1], L[0])), V.int(0)] : [V.int(0), V.int(0), V.int(0)]; },
    onChange: () => App.save(), hint: "EXE: tính · TOOLS: tùy chọn",
    onExe: () => App.run(() => App.push(new ResultScr("Mẫu số liệu ghép nhóm", groupedStats(App.grp.map(r => r[0]), App.grp.map(r => r[1]), App.grp.map(r => r[2]))))),
    tools: g => [{ label: "Kết quả", act: () => { App.closeMenus(); g.opt.onExe(); } }, { label: "Xóa toàn bộ dữ liệu", act: () => { App.grp.length = 0; g.r = 0; App.save(); App.closeMenus(); } }]
  });
}
/* ---------------- Phân phối ---------------- */
function distMenu() {
  const num = (v, name) => { const x = toNum(v); if (!isFinite(x)) ERR("Math"); return x; };
  const sig = v => { const s = toNum(v); if (!(s > 0)) ERR("Math", "σ phải > 0"); return s; };
  const res = (title, lines) => new ResultScr(title, lines.map(([k, v]) => [k, typeof v === "number" ? V.f(v) : v]));
  const nat = (v, name) => { const n = toNum(v); if (!Number.isInteger(n) || n < 0) ERR("Math", name + " phải là số tự nhiên"); return n; };
  const prob = v => { const p = toNum(v); if (!(p >= 0 && p <= 1)) ERR("Math", "p phải thuộc [0; 1]"); return p; };
  const items = [
    ["Phân phối chuẩn — PD", "npd", [["<i>x</i>=", "x", "0"], ["σ=", "s", "1"], ["μ=", "m", "0"]], v => { const s = sig(v.s), z = (num(v.x) - num(v.m)) / s; return res("Normal PD", [["<i>p</i>", Math.exp(-z * z / 2) / (s * Math.sqrt(2 * Math.PI))]]); }],
    ["Phân phối chuẩn — CD", "ncd", [["Cận dưới=", "a", "−1"], ["Cận trên=", "b", "1"], ["σ=", "s", "1"], ["μ=", "m", "0"]], v => { const s = sig(v.s), m = num(v.m), a = num(v.a), b = num(v.b); if (b < a) ERR("Math", "Cận trên phải ≥ cận dưới"); return res("Normal CD", [["<i>P</i>", normCdf((b - m) / s) - normCdf((a - m) / s)], ["<i>z</i>:Dưới", (a - m) / s], ["<i>z</i>:Trên", (b - m) / s]]); }],
    ["Nghịch đảo phân phối chuẩn", "ninv", [["Diện tích=", "p", "0.95"], ["σ=", "s", "1"], ["μ=", "m", "0"], ["Đuôi:", "tail", null, [["Trái", "L"], ["Phải", "R"], ["Giữa", "C"]]]], v => {
      const p = num(v.p), s = sig(v.s), m = num(v.m);
      if (v.tail === "C") { const z = normInv(0.5 + p / 2); return res("Inverse Normal", [["<i>x</i>₁", m - z * s], ["<i>x</i>₂", m + z * s]]); }
      const z = normInv(v.tail === "L" ? p : 1 - p); return res("Inverse Normal", [["<i>x</i>", m + z * s]]);
    }],
    ["Nhị thức — PD", "bpd", [["<i>x</i>=", "x", "0"], ["<i>N</i>=", "n", "10"], ["<i>p</i>=", "p", "0.5"]], v => { const N = nat(v.n, "N"), x = nat(v.x, "x"), p = prob(v.p); return res("Binomial PD", [["<i>P</i>", binomPD(x, N, p)]]); }],
    ["Nhị thức — CD", "bcd", [["Cận dưới=", "a", "0"], ["Cận trên=", "b", "5"], ["<i>N</i>=", "n", "10"], ["<i>p</i>=", "p", "0.5"]], v => { const N = nat(v.n, "N"), a = nat(v.a, "Cận dưới"), b = nat(v.b, "Cận trên"), p = prob(v.p); if (b < a) ERR("Math"); let s = 0; for (let k = a; k <= Math.min(b, N); k++) s += binomPD(k, N, p); return res("Binomial CD", [["<i>P</i>", Math.min(1, s)]]); }],
    ["Poisson — PD", "ppd", [["<i>x</i>=", "x", "0"], ["λ=", "l", "1"]], v => { const x = nat(v.x, "x"), l = toNum(v.l); if (!(l > 0)) ERR("Math", "λ phải > 0"); return res("Poisson PD", [["<i>P</i>", poisPD(x, l)]]); }],
    ["Poisson — CD", "pcd", [["Cận dưới=", "a", "0"], ["Cận trên=", "b", "2"], ["λ=", "l", "1"]], v => { const a = nat(v.a, "Cận dưới"), b = nat(v.b, "Cận trên"), l = toNum(v.l); if (!(l > 0)) ERR("Math", "λ phải > 0"); if (b < a) ERR("Math"); let s = 0; for (let k = a; k <= Math.min(b, a + 5000); k++) s += poisPD(k, l); return res("Poisson CD", [["<i>P</i>", Math.min(1, s)]]); }]
  ];
  return new MenuScr("Phân phối", items.map(([label, id, fields, fn]) => ({
    label, act: () => App.push(new FormScr("dist_" + id, label, fields.map(([l, k, d, opts]) => (opts ? { label: l, key: k, type: "choice", opts } : { label: l, key: k, def: d })), fn))
  })));
}
/* ---------------- Bảng giá trị ---------------- */
function tableForm() {
  return new FormScr("table", "Bảng giá trị", [
    { label: "<i>f</i>(<i>x</i>)=", key: "f", type: "raw", bind: () => App.funcs.f, store: it => { App.funcs.f = clone(it); } },
    { label: "<i>g</i>(<i>x</i>)=", key: "g", type: "raw", optional: true, bind: () => App.funcs.g, store: it => { App.funcs.g = clone(it); } },
    { label: "Bắt đầu=", key: "a", def: "1" }, { label: "Kết thúc=", key: "b", def: "5" }, { label: "Bước=", key: "h", def: "1" }
  ], v => {
    if (!v.f.length && !v.g.length) ERR("Syntax", "Chưa nhập f(x)");
    const a = v.a, b = v.b, h = v.h;
    if (!(toNum(h) > 0)) ERR("Math", "Bước phải > 0"); if (toNum(b) < toNum(a)) ERR("Math", "Kết thúc phải ≥ bắt đầu");
    const n = Math.floor((toNum(b) - toNum(a)) / toNum(h) + 1e-9) + 1, max = v.f.length && v.g.length ? 45 : 45;
    if (n > max) ERR("Math", "Tối đa " + max + " hàng — hãy tăng bước");
    const nf = v.f.length ? parseItems(v.f) : null, ng = v.g.length ? parseItems(v.g) : null, env = App.env(), rows = [];
    for (let k = 0; k < n; k++) {
      const x = add(a, mul(V.int(k), h)), ev = node => { try { return evalNode(node, { ...env, bind: { x } }); } catch (e) { return { k: "txt", h: "ERROR" }; } };
      rows.push([x, nf ? ev(nf) : null, ng ? ev(ng) : null]);
    }
    const cols = [{ name: "<i>x</i>", i: 0 }]; if (nf) cols.push({ name: "<i>f</i>(<i>x</i>)", i: 1 }); if (ng) cols.push({ name: "<i>g</i>(<i>x</i>)", i: 2 });
    return new GridScr("", cols, rows, { ro: true, hint: "▲▼◀▶: xem giá trị · AC: quay lại" });
  });
}
/* ---------------- Phương trình ---------------- */
const SUBS = ["₁", "₂", "₃", "₄"], UNK = ["x", "y", "z", "t"], CL = ["a", "b", "c", "d", "e"];
function coefRows(key, r, c) {
  let rows = App.eq[key];
  if (!rows || rows.length !== r || rows[0].length !== c) rows = App.eq[key] = Array.from({ length: r }, () => Array.from({ length: c }, () => V.int(0)));
  return rows;
}
function eqnMenu() {
  return new MenuScr("Phương trình", [
    ...[2, 3, 4].map(n => ({ label: `Hệ PT bậc nhất ${n} ẩn`, act: () => App.push(linGrid(n)) })),
    ...[2, 3, 4].map(d => ({ label: `PT bậc ${d}: ${polyHead(d)}=0`, act: () => App.push(polyGrid(d)) })),
    { label: "Solver — giải PT bất kỳ theo <i>x</i>", act: () => App.push(solverForm()) }
  ]);
}
function polyHead(d) { return Array.from({ length: d + 1 }, (_, i) => { const p = d - i; return `<i>${CL[i]}</i>${p ? "<i>x</i>" + (p > 1 ? "<sup>" + p + "</sup>" : "") : ""}`; }).join("+"); }
function linGrid(n) {
  const head = Array.from({ length: n }, (_, i) => `<i>${CL[i]}</i><sub>n</sub><i>${UNK[i]}</i>`).join("+") + `=<i>${CL[n]}</i><sub>n</sub>`;
  const rows = coefRows("lin" + n, n, n + 1);
  return new GridScr("Hệ " + n + " ẩn", Array.from({ length: n + 1 }, (_, i) => ({ name: `<i>${CL[i]}</i>`, i })), rows, {
    fixed: true, dir: "right", head, onChange: () => App.save(), hint: "Nhập hệ số · EXE (khi không sửa): giải",
    onExe: () => App.run(() => {
      const r = linSolve(rows);
      App.push(new ResultScr("Nghiệm", r.none ? ["<b>Hệ vô nghiệm</b>"] : r.inf ? ["<b>Hệ có vô số nghiệm</b>"] : r.x.map((v, i) => [`<i>${UNK[i]}</i>`, v])));
    })
  });
}
function polyGrid(d) {
  const rows = coefRows("poly" + d, 1, d + 1);
  return new GridScr("PT bậc " + d, Array.from({ length: d + 1 }, (_, i) => ({ name: `<i>${CL[i]}</i>`, i })), rows, {
    fixed: true, dir: "right", head: polyHead(d) + "=0", onChange: () => App.save(), hint: "Nhập hệ số · EXE (khi không sửa): giải",
    onExe: () => App.run(() => App.push(polyResult(rows[0])))
  });
}
function polyResult(cf) {
  const roots = polyRoots(cf), d = cf.length - 1, lines = [];
  const uniq = [];
  roots.forEach(r => { if (!uniq.some(u => u.k === r.k && Math.abs(toNum(u.k === "cx" ? u.re : u) - toNum(r.k === "cx" ? r.re : r)) < 1e-10 && (r.k !== "cx" || Math.abs(toNum(u.im) - toNum(r.im)) < 1e-10))) uniq.push(r); });
  uniq.forEach((r, i) => lines.push([`<i>x</i>${uniq.length > 1 ? SUBS[i] : ""}`, r]));
  if (uniq.length < roots.length && uniq.length === 1) lines[0][0] = "<i>x</i> (nghiệm kép)";
  if (d === 2) { // đỉnh parabol
    const [a, b, c] = cf, xv = div(neg(b), mul(V.int(2), a)), yv = polyEvalV(cf, xv), mn = toNum(a) > 0;
    lines.push(`<b>${mn ? "Giá trị nhỏ nhất" : "Giá trị lớn nhất"}</b>`, [`<i>x</i>`, xv], [`<i>y</i>`, yv]);
  }
  if (d === 3) { // cực trị
    const dc = [mul(V.int(3), cf[0]), mul(V.int(2), cf[1]), cf[2]], cr = polyRoots(dc).filter(r => r.k !== "cx");
    if (cr.length === 2 && cmpV(cr[0], cr[1]) !== 0) {
      const p = cr.map(x => [x, polyEvalV(cf, x)]), up = toNum(cf[0]) > 0;
      lines.push(`<b>Cực đại</b>`, ["<i>x</i>", p[up ? 0 : 1][0]], ["<i>y</i>", p[up ? 0 : 1][1]], `<b>Cực tiểu</b>`, ["<i>x</i>", p[up ? 1 : 0][0]], ["<i>y</i>", p[up ? 1 : 0][1]]);
    }
  }
  return new ResultScr("Nghiệm", lines);
}
function solverForm() {
  return new FormScr("solver", "Solver", [{ label: "PT:", key: "eq", type: "raw", def: "" }, { label: "Giá trị đầu <i>x</i>=", key: "x0", def: "0" }], v => {
    let it = v.eq; if (!it.length) ERR("Syntax", "Chưa nhập phương trình");
    if (!hasTopEq(it)) it = it.concat([CH("="), CH("0")]);
    App.vars.x = v.x0; const r = solveItems(it); App.save();
    return new ResultScr("Solver", r.items, { hint: "Nghiệm gần giá trị đầu; đổi giá trị đầu để tìm nghiệm khác" });
  }, { hint: "Dùng phím = (hàng hàm) · EXE: tiếp · OK: giải" });
}
/* ---------------- Bất phương trình ---------------- */
function ineqMenu() {
  return new MenuScr("Bất phương trình", [2, 3, 4].map(d => ({
    label: `Bậc ${d}`, act: () => App.push(new MenuScr("Bậc " + d + ": chọn dấu", [">", "<", "≥", "≤"].map(rel => ({ label: polyHead(d) + rel + "0", act: () => App.push(ineqGrid(d, rel)) }))))
  })));
}
function ineqGrid(d, rel) {
  const rows = coefRows("poly" + d, 1, d + 1);
  return new GridScr("BPT bậc " + d, Array.from({ length: d + 1 }, (_, i) => ({ name: `<i>${CL[i]}</i>`, i })), rows, {
    fixed: true, dir: "right", real: true, head: polyHead(d) + rel + "0", onChange: () => App.save(), hint: "Nhập hệ số · EXE (khi không sửa): giải",
    onExe: () => App.run(() => {
      const segs = polyIneq(rows[0], rel), X = "<i>x</i>", f = v => fmt(v);
      const lt = s => (s ? " ≤ " : " &lt; ");
      let lines = segs.map(s => {
        if (s.pt) return `${X} = ${f(s.lo)}`;
        if (!s.lo && !s.hi) return "Mọi số thực " + X;
        if (!s.lo) return `${X}${lt(s.hiIn)}${f(s.hi)}`;
        if (!s.hi) return `${f(s.lo)}${lt(s.loIn)}${X}`;
        return `${f(s.lo)}${lt(s.loIn)}${X}${lt(s.hiIn)}${f(s.hi)}`;
      });
      if (!lines.length) lines = ["<b>Vô nghiệm</b>"];
      App.push(new ResultScr("Tập nghiệm", lines.map(l => (l.startsWith("<b>") ? l : `<span class="nd">${l}</span>`))));
    })
  });
}
/* ---------------- Tỉ lệ thức ---------------- */
function ratioMenu() {
  const mk = (id, label, fields, fn) => ({ label, act: () => App.push(new FormScr(id, label, fields.map(([l, k]) => ({ label: l, key: k, def: "1" })), v => new ResultScr("", [["<i>X</i>", fn(v)]]))) });
  return new MenuScr("Tỉ lệ thức", [
    mk("ratio1", "<i>A</i>:<i>B</i>=<i>X</i>:<i>D</i>", [["<i>A</i>=", "a"], ["<i>B</i>=", "b"], ["<i>D</i>=", "d"]], v => div(mul(v.a, v.d), v.b)),
    mk("ratio2", "<i>A</i>:<i>B</i>=<i>C</i>:<i>X</i>", [["<i>A</i>=", "a"], ["<i>B</i>=", "b"], ["<i>C</i>=", "c"]], v => div(mul(v.b, v.c), v.a))
  ]);
}
/* ---------------- Hộp toán: xúc xắc / đồng xu ---------------- */
function boxMenu() {
  const run = (kind, n, T) => {
    const faces = kind === "dice" ? 6 : 2, lo = kind === "dice" ? n : 0, hi = kind === "dice" ? 6 * n : n, cnt = Array(hi - lo + 1).fill(0);
    let total = 0;
    for (let t = 0; t < T; t++) { let s = 0; for (let k = 0; k < n; k++) { const r = Math.floor(Math.random() * faces); s += kind === "dice" ? r + 1 : r; } cnt[s - lo]++; total += s; }
    const rows = cnt.map((c, i) => [V.int(lo + i), V.int(c), V.q(new Q(BigInt(c), BigInt(T)))]);
    return new GridScr("", [{ name: kind === "dice" ? "Tổng" : "Số mặt S", i: 0 }, { name: "Số lần", i: 1 }, { name: "Tần suất", i: 2 }], rows, {
      ro: true, head: `${T} lần · trung bình = ${fmt(V.q(new Q(BigInt(total), BigInt(T))), "dec")}`, hint: "EXE: tung lại · AC: quay lại",
      onExe: () => { App.pop(); App.push(run(kind, n, T)); }
    });
  };
  const form = (kind) => new FormScr("box_" + kind, kind === "dice" ? "Tung xúc xắc" : "Tung đồng xu", [{ label: kind === "dice" ? "Số xúc xắc (1–3)=" : "Số đồng xu (1–3)=", key: "n", def: "1" }, { label: "Số lần tung (1–250)=", key: "t", def: "50" }], v => {
    const n = Number(asInt(v.n)), T = Number(asInt(v.t)); if (n < 1 || n > 3) ERR("Math", "Chọn 1–3"); if (T < 1 || T > 250) ERR("Math", "Số lần 1–250");
    return run(kind, n, T);
  });
  return new MenuScr("Hộp toán", [{ label: "Tung xúc xắc", act: () => App.push(form("dice")) }, { label: "Tung đồng xu", act: () => App.push(form("coin")) }]);
}
/* ---------------- Hình học & Xác suất (Plus) ---------------- */
function angUnit() { return { D: "°", R: " rad", G: " grad" }[App.S.ang]; }
function triResult(a, b, c, extra) {
  const A_ = App.S.ang, two = V.int(2);
  if ([a, b, c].some(v => !(toNum(v) > 0))) ERR("Math", "Cạnh phải > 0");
  const [x, y, z] = [a, b, c].map(toNum); if (x + y <= z * (1 + 1e-12) || x + z <= y * (1 + 1e-12) || y + z <= x * (1 + 1e-12)) ERR("Math", "Ba cạnh không tạo thành tam giác");
  const cosA = div(sub(add(mul(b, b), mul(c, c)), mul(a, a)), mul(two, mul(b, c)));
  const cosB = div(sub(add(mul(a, a), mul(c, c)), mul(b, b)), mul(two, mul(a, c)));
  const cosC = div(sub(add(mul(a, a), mul(b, b)), mul(c, c)), mul(two, mul(a, b)));
  const ang = cv => atrig("acos", isExact(cv) ? cv : niceFloat(Math.max(-1, Math.min(1, toNum(cv))), 1e-12), A_);
  const p = div(add(add(a, b), c), two), S2 = mul(mul(p, sub(p, a)), mul(sub(p, b), sub(p, c))), S = sqrtV(toNum(S2) < 0 ? V.int(0) : S2);
  const u = angUnit();
  return new ResultScr("Tam giác", [...(extra || []), ["<i>a</i>", a], ["<i>b</i>", b], ["<i>c</i>", c], ["<i>Â</i> (" + u.trim() + ")", ang(cosA)], ["<i>B̂</i> (" + u.trim() + ")", ang(cosB)], ["<i>Ĉ</i> (" + u.trim() + ")", ang(cosC)],
    ["Diện tích <i>S</i>", S], ["Chu vi", mul(p, two)], ["<i>R</i> (ngoại tiếp)", div(mul(mul(a, b), c), mul(V.int(4), S))], ["<i>r</i> (nội tiếp)", div(S, p)],
    ["<i>h<sub>a</sub></i>", div(mul(two, S), a)], ["<i>h<sub>b</sub></i>", div(mul(two, S), b)], ["<i>h<sub>c</sub></i>", div(mul(two, S), c)],
    ["<i>m<sub>a</sub></i> (trung tuyến)", div(sqrtV(sub(mul(two, add(mul(b, b), mul(c, c))), mul(a, a))), two)]]);
}
function geoMenu() {
  const F = (id, label, fields, fn) => ({ label, act: () => App.push(new FormScr("geo_" + id, label, fields.map(([l, k, d]) => ({ label: l, key: k, def: d == null ? "0" : d })), fn)) });
  const P3 = (p) => [[`<i>x</i><sub>${p}</sub>=`, "x" + p], [`<i>y</i><sub>${p}</sub>=`, "y" + p], [`<i>z</i><sub>${p}</sub>=`, "z" + p]];
  const sq = v => mul(v, v), u = () => angUnit();
  return new MenuScr("Hình học & Xác suất", [
    F("sss", "Tam giác: biết 3 cạnh", [["<i>a</i>=", "a", "3"], ["<i>b</i>=", "b", "4"], ["<i>c</i>=", "c", "5"]], v => triResult(v.a, v.b, v.c)),
    F("sas", "Tam giác: 2 cạnh + góc xen giữa", [["<i>a</i>=", "a", "3"], ["<i>b</i>=", "b", "4"], ["Góc <i>Ĉ</i>=", "C", "90"]], v => {
      const c2 = sub(add(sq(v.a), sq(v.b)), mul(mul(V.int(2), mul(v.a, v.b)), trig("cos", v.C, App.S.ang))); if (!(toNum(c2) > 0)) ERR("Math");
      return triResult(v.a, v.b, sqrtV(c2));
    }),
    F("asa", "Tam giác: 1 cạnh + 2 góc kề", [["<i>c</i>=", "c", "10"], ["Góc <i>Â</i>=", "A", "60"], ["Góc <i>B̂</i>=", "B", "60"]], v => {
      const full = V.q(Q.int({ D: 180, G: 200 }[App.S.ang] || 1)), half = App.S.ang === "R" ? V.p(Q1) : full, C = sub(sub(half, v.A), v.B);
      if (!(toNum(C) > 0) || !(toNum(v.A) > 0) || !(toNum(v.B) > 0)) ERR("Math", "Tổng hai góc phải nhỏ hơn " + (App.S.ang === "R" ? "π" : toNum(full) + u()));
      const sC = trig("sin", C, App.S.ang);
      return triResult(div(mul(v.c, trig("sin", v.A, App.S.ang)), sC), div(mul(v.c, trig("sin", v.B, App.S.ang)), sC), v.c);
    }),
    F("d2p", "Khoảng cách hai điểm (Oxyz)", [...P3("A"), ...P3("B")], v => {
      const dx = sub(v.xB, v.xA), dy = sub(v.yB, v.yA), dz = sub(v.zB, v.zA);
      return new ResultScr("", [["<i>AB</i>", sqrtV(add(add(sq(dx), sq(dy)), sq(dz)))], ["Trung điểm <i>x</i>", div(add(v.xA, v.xB), V.int(2))], ["Trung điểm <i>y</i>", div(add(v.yA, v.yB), V.int(2))], ["Trung điểm <i>z</i>", div(add(v.zA, v.zB), V.int(2))]]);
    }),
    F("dpl", "Khoảng cách điểm → đường thẳng <i>ax</i>+<i>by</i>+<i>c</i>=0", [["<i>a</i>=", "a", "3"], ["<i>b</i>=", "b", "4"], ["<i>c</i>=", "c", "−5"], ["<i>x</i><sub>0</sub>=", "x"], ["<i>y</i><sub>0</sub>=", "y"]], v => {
      const den = sqrtV(add(sq(v.a), sq(v.b))); if (isZero(den)) ERR("Math", "a, b không đồng thời bằng 0");
      return new ResultScr("", [["<i>d</i>", div(absV(add(add(mul(v.a, v.x), mul(v.b, v.y)), v.c)), den)]]);
    }),
    F("pl3", "Mặt phẳng qua 3 điểm", [...P3("A"), ...P3("B"), ...P3("C")], v => {
      const AB = [sub(v.xB, v.xA), sub(v.yB, v.yA), sub(v.zB, v.zA)], AC = [sub(v.xC, v.xA), sub(v.yC, v.yA), sub(v.zC, v.zA)];
      let n = [sub(mul(AB[1], AC[2]), mul(AB[2], AC[1])), sub(mul(AB[2], AC[0]), mul(AB[0], AC[2])), sub(mul(AB[0], AC[1]), mul(AB[1], AC[0]))];
      if (n.every(isZero)) ERR("Math", "Ba điểm thẳng hàng");
      let d = neg(add(add(mul(n[0], v.xA), mul(n[1], v.yA)), mul(n[2], v.zA))), all = [...n, d];
      if (all.every(x => x.k === "q")) { // rút gọn về số nguyên nhỏ nhất
        const L = all.reduce((s, x) => s / bgcd(s, x.q.d) * x.q.d, 1n), ints = all.map(x => x.q.n * (L / x.q.d)), g = ints.reduce((s, x) => bgcd(s, x), 0n) || 1n;
        const sg = (ints.find(x => x !== 0n) < 0n) ? -1n : 1n; all = ints.map(x => V.q(new Q(x / g * sg)));
      }
      const [a, b, c, dd] = all, term = (k, s, first) => { const t = toNum(k); if (t === 0) return ""; const ab = absV(k), one = ab.k === "q" && ab.q.cmp(Q1) === 0 && s; return (t < 0 ? "−" : first ? "" : "+") + (one ? "" : fmt(ab)) + (s ? `<i>${s}</i>` : ""); };
      let eq = term(a, "x", true); eq += term(b, "y", !eq); eq += term(c, "z", !eq); eq += term(dd, "", !eq);
      return new ResultScr("Mặt phẳng (ABC)", [`<span class="nd">${eq}=0</span>`, ["<i>a</i>", a], ["<i>b</i>", b], ["<i>c</i>", c], ["<i>d</i>", dd], ["Diện tích Δ<i>ABC</i>", div(sqrtV(add(add(sq(n[0]), sq(n[1])), sq(n[2]))), V.int(2))]]);
    }),
    F("dpp", "Khoảng cách điểm → mặt phẳng", [["<i>a</i>=", "a", "1"], ["<i>b</i>=", "b", "2"], ["<i>c</i>=", "c", "2"], ["<i>d</i>=", "d", "−3"], ["<i>x</i><sub>0</sub>=", "x"], ["<i>y</i><sub>0</sub>=", "y"], ["<i>z</i><sub>0</sub>=", "z"]], v => {
      const den = sqrtV(add(add(sq(v.a), sq(v.b)), sq(v.c))); if (isZero(den)) ERR("Math", "a, b, c không đồng thời bằng 0");
      return new ResultScr("", [["<i>d</i>", div(absV(add(add(add(mul(v.a, v.x), mul(v.b, v.y)), mul(v.c, v.z)), v.d)), den)]]);
    }),
    F("sec", "Hình quạt & cung tròn", [["<i>r</i>=", "r", "2"], ["Góc ở tâm <i>α</i> (độ)=", "a", "60"]], v => {
      if (!(toNum(v.r) > 0) || !(toNum(v.a) > 0)) ERR("Math", "r và α phải > 0");
      const rad = v.a.k === "q" ? V.p(v.a.q.div(Q.int(180))) : V.f(toNum(v.a) * Math.PI / 180), two = V.int(2);
      const area = div(mul(sq(v.r), rad), two), tri = div(mul(sq(v.r), trig("sin", v.a, "D")), two);
      return new ResultScr("Hình quạt", [["Độ dài cung <i>l</i>", mul(v.r, rad)], ["Diện tích quạt", area], ["Dây cung", mul(mul(two, v.r), trig("sin", div(v.a, two), "D"))], ["Diện tích viên phân", sub(area, tri)], ["<i>α</i> (rad)", rad]]);
    }),
    F("bay", "Xác suất toàn phần & Bayes", [["<i>P</i>(<i>A</i>)=", "pa", "0.3"], ["<i>P</i>(<i>B</i>|<i>A</i>)=", "pba", "0.8"], ["<i>P</i>(<i>B</i>|<i>Ā</i>)=", "pbn", "0.1"]], v => {
      [v.pa, v.pba, v.pbn].forEach(p => { const t = toNum(p); if (!(t >= 0 && t <= 1)) ERR("Math", "Xác suất phải thuộc [0; 1]"); });
      const one = V.int(1), pn = sub(one, v.pa), pb = add(mul(v.pa, v.pba), mul(pn, v.pbn));
      if (isZero(pb)) ERR("Math", "P(B) = 0");
      return new ResultScr("Bayes", [["<i>P</i>(<i>Ā</i>)", pn], ["<i>P</i>(<i>B</i>)", pb], ["<i>P</i>(<i>A</i>|<i>B</i>)", div(mul(v.pa, v.pba), pb)], ["<i>P</i>(<i>Ā</i>|<i>B</i>)", div(mul(pn, v.pbn), pb)], ["<i>P</i>(<i>B̄</i>)", sub(one, pb)]]);
    })
  ]);
}
/* ---------------- hiển thị, bàn phím, khởi động ---------------- */
const $ = id => document.getElementById(id);
function statusHTML() {
  const S = App.S, tag = (APPS[App.app] || {}).tag, onHome = App.top() && App.top().home;
  const fm = S.fmt === "fix" ? "FIX" : S.fmt === "sci" ? "SCI" : "";
  const appTag = onHome ? "HOME" : App.app === "basen" ? App.base : tag;
  return `<div class="sb"><span class="ind s${App.shift ? " lit" : ""}">S</span><span class="ind box">${S.ang}</span>${S.io === "decO" ? '<span class="ind">Deci</span>' : '<span class="ind">Math</span>'}${fm ? `<span class="ind">${fm}</span>` : ""}<span class="sp"></span>${appTag ? `<span class="ind tag">${appTag}</span>` : ""}<span class="bat"><i></i></span></div>`;
}
function render() {
  const lcd = $("lcd"); if (!lcd) return;
  document.body.classList.toggle("shift-on", App.shift);
  if (App.off) { lcd.classList.add("off"); lcd.innerHTML = '<div class="offmsg">Bấm ON để bật</div>'; return; }
  lcd.classList.remove("off");
  const top = App.top();
  lcd.innerHTML = statusHTML() + `<div class="lb">${top.render()}</div>`;
  try { top.after(lcd.querySelector(".lb")); } catch (e) { console.error(e); }
}
function press(k) {
  if (App.off) { if (k === "on") { App.off = false; render(); } return; }
  if (k === "shift") { App.shift = !App.shift; render(); return; }
  let key = k;
  if (App.shift) { key = SHIFT[k] || k; App.shift = false; }
  try { dispatch(key); } catch (e) { console.error(e); App.push(new ErrScr("Math", "")); }
  render();
}
function dispatch(key) {
  const top = App.top();
  switch (key) {
    case "off": App.off = true; App.save(); return;
    case "on": if (top.isMenu) App.closeMenus(); else top.key("ac"); return;
    case "home": { const h = App.stack[0] && App.stack[0].home ? App.stack[0] : new HomeScr(); h.sel = APP_ORDER.indexOf(App.app); App.stack = [h]; return; }
    case "back":
      if (top.home) { openApp(App.app); return; }
      if (App.stack.length > 2 || (App.stack.length === 2 && !App.stack[0].home)) { App.pop(); return; }
      dispatch("home"); return;
    case "settings": if (top.isMenu && top.title === "SETTINGS") App.pop(); else App.push(settingsMenu()); return;
    case "variable": if (top.home) return; { const m = variableMenu(false); if (m) App.push(m); } return;
    case "sto": if (top.home) return; App.push(variableMenu(true)); return;
    case "function": if (top.home || App.app === "basen") return; App.push(functionMenu()); return;
    case "catalog": if (top.home) return; App.push(catalogMenu()); return;
    case "tools": {
      if (top.home) return;
      let s = null; for (let i = App.stack.length - 1; i >= 0; i--) if (!App.stack[i].isMenu) { s = App.stack[i]; break; }
      const items = (s && s.tools && s.tools()) || [];
      items.push({ label: "Về màn hình HOME", act: () => dispatch("home") });
      App.push(new MenuScr("TOOLS", items)); return;
    }
  }
  if (top instanceof CalcScr && key === "ok") { top.key("exe"); return; }
  top.key(key);
}
/* ---- bố cục phím ---- */
const DEL_SVG = '<svg class="kdi" viewBox="0 0 24 16" aria-hidden="true"><path d="M7 1h15v14H7L1 8z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M11 5l6 6M17 5l-6 6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>';
const KB = {
  nav: { l: [["shift", "SHIFT"], ["back", "BACK"], ["variable", "VARIABLE"], ["function", "FUNCTION"]], r: [["home", "HOME"], ["settings", "SETTINGS"], ["catalog", "CATALOG"], ["tools", "TOOLS"]] },
  fn: [
    [["xvar", "<i>x</i>", "<i>y</i>"], ["frac", '<span class="kfr"><b>■</b><b>□</b></span>', "■⌟<sup>■</sup>⁄<sub>□</sub>"], ["sqrt", "√■", "∛■"], ["sq", "<i>x</i>²", "<i>x</i>³"], ["pow", "<i>x</i><sup>■</sup>", "■√□"], ["log", "log<sub>■</sub>□", "10<sup>■</sup>"]],
    [["ln", "ln", "e<sup>■</sup>"], ["sin", "sin", "sin<sup>−1</sup>"], ["cos", "cos", "cos<sup>−1</sup>"], ["tan", "tan", "tan<sup>−1</sup>"], ["lp", "(", "%"], ["rp", ")", ","]],
    [["neg", "(−)", "|■|"], ["inv", "<i>x</i><sup>−1</sup>", "<i>x</i>!"], ["dms", "° ′ ″", "<i>i</i>"], ["deriv", '<span class="kfr sm"><b>d</b><b>d<i>x</i></b></span>', "∫"], ["format", "FORMAT", "Σ"], ["eq", "=", "<i>e</i>"]]
  ],
  num: [
    [["7", "7", "GCD"], ["8", "8", "LCM"], ["9", "9", "÷R"], ["del", DEL_SVG, "UNDO", "kdel"], ["ac", "AC", "OFF", "kac"]],
    [["4", "4", "Int"], ["5", "5", "Intg"], ["6", "6", "Rnd"], ["mul", "×", "<i>n</i>P<i>r</i>"], ["div", "÷", "<i>n</i>C<i>r</i>"]],
    [["1", "1", "Pol"], ["2", "2", "Rec"], ["3", "3", "Ran#"], ["add", "+", "RanInt"], ["sub", "−", "∠"]],
    [["0", "0", "PreAns"], ["dot", ".", ""], ["exp", "×10<sup><i>x</i></sup>", "π"], ["ans", "Ans", "STO"], ["exe", "EXE", "≈", "kexe"]]
  ]
};
const KEY_NAMES = { xvar: "x", frac: "phân số", sqrt: "căn bậc hai", sq: "bình phương", pow: "lũy thừa", log: "logarit cơ số", ln: "ln", lp: "mở ngoặc", rp: "đóng ngoặc", neg: "dấu âm", inv: "nghịch đảo", dms: "độ phút giây", deriv: "đạo hàm", format: "FORMAT", eq: "dấu bằng", del: "xóa", ac: "AC xóa hết", mul: "nhân", div: "chia", add: "cộng", sub: "trừ", dot: "dấu chấm", exp: "nhân 10 mũ", ans: "Ans", exe: "EXE bằng", up: "lên", down: "xuống", left: "trái", right: "phải", ok: "OK" };
function buildKeys() {
  const kb = $("keys"); if (!kb) return;
  const key = ([k, lab, sh, cls]) => `<div class="kc"><span class="ksh">${sh || "&nbsp;"}</span><button type="button" class="k ${cls || ""}" data-k="${k}" aria-label="${esc((KEY_NAMES[k] || lab.replace(/<[^>]+>/g, "")) + (sh ? " · SHIFT: " + sh.replace(/<[^>]+>/g, "") : ""))}"><span class="kl">${lab}</span></button></div>`;
  const nav = side => side.map(([k, l]) => `<button type="button" class="kn${k === "shift" ? " kshift" : ""}" data-k="${k}">${l}</button>`);
  const L = nav(KB.nav.l), R = nav(KB.nav.r);
  kb.innerHTML = `<div class="knav">${L[0]}${L[1]}<div class="dpad" role="group" aria-label="Phím điều hướng"><button type="button" class="dp up" data-k="up" aria-label="lên">▲</button><button type="button" class="dp left" data-k="left" aria-label="trái">◀</button><button type="button" class="dp ok" data-k="ok">OK</button><button type="button" class="dp right" data-k="right" aria-label="phải">▶</button><button type="button" class="dp down" data-k="down" aria-label="xuống">▼</button></div>${R[0]}${R[1]}${L[2]}${L[3]}${R[2]}${R[3]}</div>`
    + `<div class="kfn">${KB.fn.map(r => r.map(key).join("")).join("")}</div><div class="knum">${KB.num.map(r => r.map(([k, l, s, c]) => key([k, l, s, "kd " + (c || "")])).join("")).join("")}</div>`;
  const REPEAT = new Set(["up", "down", "left", "right", "del"]);
  let timer = null, repeated = false;
  const stop = () => { clearTimeout(timer); clearInterval(timer); timer = null; };
  document.querySelectorAll("[data-k]").forEach(b => {
    const k = b.dataset.k;
    b.addEventListener("mousedown", e => e.preventDefault()); // không giữ focus → Enter luôn là EXE
    b.addEventListener("click", () => { if (repeated) { repeated = false; return; } press(k); });
    if (REPEAT.has(k)) {
      b.addEventListener("pointerdown", () => { repeated = false; stop(); timer = setTimeout(() => { repeated = true; press(k); timer = setInterval(() => press(k), 90); }, 450); });
      ["pointerup", "pointerleave", "pointercancel"].forEach(ev => b.addEventListener(ev, stop));
    }
  });
}
const KBD = { ".": "dot", ",": "comma", "+": "add", "-": "sub", "*": "mul", "/": "div", "^": "pow", "(": "lp", ")": "rp", "!": "fact", "%": "pct", "=": "eq", Enter: "exe", Backspace: "del", Escape: "ac", Delete: "ac", ArrowUp: "up", ArrowDown: "down", ArrowLeft: "left", ArrowRight: "right", x: "xvar", y: "yvar", p: "pi", s: "sin", c: "cos", t: "tan", l: "ln", r: "sqrt", i: "i", E: "exp", Home: "home" };
function onKeyDown(e) {
  const a = document.activeElement;
  if (a && (/^(INPUT|TEXTAREA|SELECT)$/.test(a.tagName) || a.isContentEditable)) return;
  if (e.altKey || ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() !== "z")) return;
  if (document.querySelector(".hdlg-ov:not([hidden])")) return;
  let k = null;
  if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "z") k = "undo";
  else if (App.app === "basen" && /^[a-fA-F]$/.test(e.key) && !(App.top() && App.top().home)) { e.preventDefault(); App.feed({ c: e.key.toUpperCase() }); render(); return; }
  else if (/^[0-9]$/.test(e.key)) k = e.key;
  else if (e.key === "Enter" && a && a.matches && a.matches("button[data-k]")) return; // để nút xử lý
  else k = KBD[e.key] || null;
  if (!k) return;
  e.preventDefault(); press(k);
  const b = document.querySelector(`[data-k="${k}"]`); if (b) { b.classList.add("hit"); setTimeout(() => b.classList.remove("hit"), 120); }
}
/* ---- lịch sử bên cạnh ---- */
function renderSide() {
  const box = $("historyList"); if (!box) return;
  const list = App.hist.map((h, i) => [h, i]).reverse().slice(0, 40);
  if (!list.length) { box.innerHTML = '<p class="empty-history">Các phép tính của bạn sẽ xuất hiện ở đây.</p>'; return; }
  box.innerHTML = list.map(([h, i]) => {
    let out = ""; try { out = h.app === "basen" ? baseStr(h.v.q.n, 10) + "<small> (DEC)</small>" : fmt(h.v); } catch (e) { out = "?"; }
    return `<button type="button" class="hitem" data-i="${i}" title="Đưa biểu thức trở lại màn hình"><span class="happ">${APPS[h.app] ? APPS[h.app].name : ""}</span><span class="hq nd">${itemsHTML(h.items)}</span><span class="hres nd">${out}</span></button>`;
  }).join("");
}
function recallHist(i) {
  const h = App.hist[i]; if (!h) return;
  if (App.app !== h.app || !(App.top() instanceof CalcScr)) openApp(h.app);
  const s = App.screens[h.app]; App.stack = [App.stack[0], s];
  s.ed = new Editor(h.items); s.mode = "edit"; s.note = ""; render();
}
function init() {
  App.load();
  buildKeys();
  App.stack = [new HomeScr()]; openApp(App.app);
  render(); renderSide();
  document.addEventListener("keydown", onKeyDown);
  $("lcd").addEventListener("click", e => { const t = e.target.closest("[data-tap]"); if (t && App.top().tap) { App.top().tap(t.dataset.tap); render(); } });
  const hl = $("historyList"); if (hl) hl.addEventListener("click", e => { const b = e.target.closest(".hitem"); if (b) recallHist(Number(b.dataset.i)); });
  const ch = $("clearHistory"); if (ch) ch.addEventListener("click", () => { App.hist = []; App.save(); renderSide(); });
  const back = $("backBtn");
  if (back) back.addEventListener("click", e => {
    try { if (document.referrer && new URL(document.referrer).origin === location.origin && history.length > 1) { e.preventDefault(); history.back(); } } catch (err) {}
  });
  window.addEventListener("pagehide", () => App.flush());
  document.addEventListener("visibilitychange", () => { if (document.hidden) App.flush(); });
}
if (typeof document !== "undefined") { if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init(); }
})();

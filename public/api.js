/* HỌC ĐỂ LÀM GÌ — API helper */
window.HOC_API_BASE = window.HOC_API_BASE ||
  ((["127.0.0.1", "localhost"].includes(location.hostname) && location.port !== "8000")
    ? "http://127.0.0.1:8000/api"
    : "/api");

async function hocApi(path, options = {}) {
  const response = await fetch(`${window.HOC_API_BASE}${path}`, {
    headers: { "Content-Type": "application/json", ...(options.headers || {}) },
    ...options
  });
  if (!response.ok) throw new Error(`API ${response.status}: ${await response.text()}`);
  return response.json();
}
window.hocApi = hocApi;

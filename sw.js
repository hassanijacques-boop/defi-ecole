/* Service worker — mode hors ligne */
const CACHE = "defi-ecole-2026-11-10-c";
const CORE = ["./", "./index.html", "./trivial.html"];

self.addEventListener("install", e => {
  e.waitUntil(
    caches.open(CACHE)
      .then(c => Promise.all(CORE.map(u => c.add(u).catch(() => null))))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", e => {
  e.waitUntil(
    caches.keys()
      .then(ks => Promise.all(ks.filter(k => !k.startsWith("defi-ecole-") || k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", e => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;
  // ne pas intercepter les URL versionnees (?v=) : elles doivent venir du reseau
  if (url.search && url.search.includes("v=")) return;

  // version.json : toujours le reseau, sinon cache
  if (url.pathname.endsWith("version.json")) {
    e.respondWith(fetch(req, {cache: "no-store"}).catch(() => caches.match(req)));
    return;
  }
  // tout le reste : reseau d'abord, cache en secours
  e.respondWith(
    fetch(req).then(r => {
      if (r && r.status === 200) {
        const copie = r.clone();
        caches.open(CACHE).then(c => c.put(req, copie)).catch(() => {});
      }
      return r;
    }).catch(() => caches.match(req).then(m => m || caches.match(CORE[0])))
  );
});

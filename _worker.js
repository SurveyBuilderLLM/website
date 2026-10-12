const APP_ORIGIN = 'https://app.aayvu.io';

function appRequest(request, pathname) {
  const incoming = new URL(request.url);
  const target = new URL(pathname + incoming.search, APP_ORIGIN);
  return new Request(target, request);
}

async function proxyApp(request, pathname, embeddable = false) {
  const response = await fetch(appRequest(request, pathname));
  if (!embeddable) return response;

  const headers = new Headers(response.headers);
  headers.delete('x-frame-options');
  headers.set('content-security-policy', "frame-ancestors 'self' https://www.aayvu.io");
  return new Response(response.body, {
    status: response.status,
    statusText: response.statusText,
    headers,
  });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.pathname.startsWith('/f/')) {
      return proxyApp(request, url.pathname, true);
    }

    if (url.pathname.startsWith('/_next/') || url.pathname.startsWith('/api/')) {
      return proxyApp(request, url.pathname);
    }

    return env.ASSETS.fetch(request);
  },
};

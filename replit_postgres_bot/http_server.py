import asyncio
from aiohttp import web

async def handle(request):
    return web.Response(text="Бот работает!")

async def run_http_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()

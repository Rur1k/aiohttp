from aiohttp import web

app = web.Application()


async def get_info(request):
    data = {"user": "User"}
    return web.json_response(data)

app.add_routes([web.get("/api/user", get_info)])

if __name__ == "__main__":
    web.run_app(app)

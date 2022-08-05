from aiohttp import web
from tortoise import Tortoise, run_async
from models import User # noqa


TORTOISE_ORM = {
    "connections": {"default": 'sqlite://db.sqlite3'},
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


async def start_db():
    await Tortoise.init(config=TORTOISE_ORM)


# async def init_db():
#     # Here we create a SQLite DB using file "db.sqlite3"
#     #  also specify the app name of "models"
#     #  which contain models from "app.models"
#     await Tortoise.init(
#         db_url='sqlite://db.sqlite3',
#         modules={'models': ['models', "aerich.models"]}
#     )
#     # Generate the schema
#     await Tortoise.generate_schemas()


routes = web.RouteTableDef()


@routes.view('/api/user')
class MyView(web.View):
    async def get(self):
        data = await User.all()
        print(data)
        # for obj in data:
        #     print(obj.first_name)
        return web.json_response(status=200)

    async def post(self):
        data = await self.request.post()
        print(data['first_name'])

        create_user = User(first_name=data['first_name'])
        await create_user.save()

        return web.json_response(status=200)


app = web.Application()
# Создаем руты
app.add_routes(routes)

if __name__ == "__main__":
    run_async(start_db())
    web.run_app(app, port=8000)

import falcon.asgi
from coreback import route

app = falcon.asgi.App(
    middleware=falcon.CORSMiddleware(
        allow_origins='*', allow_credentials='*'
    )
)

route.add(app)

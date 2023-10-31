from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get('/')
async def root():
    return "Welcome to the swagger API!"


@app.get("/github")
async def redirect_to_github():
    return RedirectResponse("https://github.com/ipesotskiiy")


@app.get('/telegram')
async def redirect_to_telegram():
    return RedirectResponse("https://t.me/ipesotskiiy")


@app.get('/hh')
async def redirect_to_hh():
    return RedirectResponse("https://rostov.hh.ru/resume/c07a3e06ff099416b10039ed1f354354454a6f")


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Swagger API",
        version="1.0.0",
        description="Swagger API with Redirect URLs",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

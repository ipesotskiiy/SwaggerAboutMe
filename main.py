from fastapi import FastAPI, Request
from fastapi.openapi.utils import get_openapi
from fastapi.responses import RedirectResponse
from starlette.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return RedirectResponse(url="/docs")


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
        description="Swagger about me, please erase /docs in the address bar and add /github , /telegram or /hh "
                    "to go to my github, telegram or headhunter",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

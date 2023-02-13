import uvicorn

from fastapi import FastAPI

from api.resources.v1.routers import ocr, get_hwp, kogpt2


def create_app():
    app = FastAPI()
    app.include_router(ocr.router)
    app.include_router(get_hwp.router)
    app.include_router(kogpt2.router)
    return app


service = create_app()

if __name__ == '__main__':
    # uvicorn.run("app:service", host="0.0.0.0", port=3000, reload=True)
    uvicorn.run("app:service", host="0.0.0.0", port=3000, reload=False)

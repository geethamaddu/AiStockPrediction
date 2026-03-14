import uvicorn
from config.settings import settings


if __name__ == "__main__":
    uvicorn.run("api.main:app", host=settings.app_host, port=settings.app_port, reload=True)
import os

import uvicorn

if __name__ == "__main__":
    workers = int(os.getenv("WORKERS", "1"))
    uvicorn.run("myproject.asgi:application", host='0.0.0.0', port=8040, workers=workers, reload=False, log_level='debug', access_log=False)

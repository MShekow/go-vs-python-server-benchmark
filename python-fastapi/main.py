import os

import uvicorn

from app import app  # only imported for Nuitka

if __name__ == "__main__":
    workers = int(os.getenv("WORKERS", "1"))
    uvicorn.run("app:app", host='0.0.0.0', port=8040, workers=workers, reload=False, log_level='debug', access_log=False)

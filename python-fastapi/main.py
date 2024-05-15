import os

import uvicorn

if __name__ == "__main__":
    workers = int(os.getenv("WORKERS", "1"))
    # multiprocessing.freeze_support()
    uvicorn.run("app:app", host='0.0.0.0', port=8040, workers=workers, reload=False, log_level='debug', access_log=False)

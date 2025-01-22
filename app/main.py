import logging.config
from logging import LogRecord
from os import sep
from pathlib import Path
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.routers import health_check, spec


class HealthCheckFilter(logging.Filter):
    def filter(self, record: LogRecord) -> bool:
        return not record.getMessage().startswith("/health")


app = FastAPI(
    title="Test Service",
    version="0.1.0",
)
app.include_router(health_check.router)

spec.register_router(app)

app_directory = Path(__file__).parent
log_filename = f"{app_directory.parent}{sep}logs{sep}debug_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.config.fileConfig(
    fname=f"{app_directory}{sep}config{sep}logger_config.ini",
    disable_existing_loggers=False,
    defaults={"logfilename": log_filename},
)
logging.getLogger("root").addFilter(HealthCheckFilter())
logging.getLogger("uvicorn.access").addFilter(HealthCheckFilter())


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    logging.debug(f"Validation error for request {request.method} {request.url}: {exc}")
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )

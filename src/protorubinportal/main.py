"""The main application factory for the protorubinportal service.

Notes
-----
Be aware that, following the normal pattern for FastAPI services, the app is
constructed when this module is loaded and is not deferred until a function is
called.
"""

from fastapi import FastAPI
from safir.dependencies.http_client import http_client_dependency
from safir.logging import configure_logging
from safir.middleware.x_forwarded import XForwardedMiddleware

from .config import config
from .handlers.router import router

__all__ = ["app", "config"]


configure_logging(
    profile=config.profile,
    log_level=config.log_level,
    name=config.logger_name,
)

app = FastAPI(
    docs_url="/_docs",
    redoc_url=None
)
"""The main FastAPI application for protorubinportal."""

app.include_router(router)


@app.on_event("startup")
async def startup_event() -> None:
    app.add_middleware(XForwardedMiddleware)


@app.on_event("shutdown")
async def shutdown_event() -> None:
    await http_client_dependency.aclose()

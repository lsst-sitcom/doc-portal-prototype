from __future__ import annotations

from fastapi import Depends
from safir.dependencies.logger import logger_dependency
from starlette.responses import HTMLResponse
from structlog.stdlib import BoundLogger

from .router import router


@router.get(
    "/",
    description="The app homepage",
    summary="Homepage",
)
async def get_index(
    logger: BoundLogger = Depends(logger_dependency),
) -> HTMLResponse:
    """The portal's homepage.
    """
    return HTMLResponse("<html><body><h1>Hello, world!</h1></body></html>")

from __future__ import annotations

from pathlib import Path

from fastapi import Depends
from safir.dependencies.logger import logger_dependency
from starlette.requests import Request
from structlog.stdlib import BoundLogger
from starlette.templating import Jinja2Templates, _TemplateResponse

from .router import router

templates = Jinja2Templates(directory=Path(__file__).parent / 'templates')


@router.get(
    "/",
    description="The app homepage",
    summary="Homepage",
)
async def get_index(
    request: Request,
    logger: BoundLogger = Depends(logger_dependency),
) -> _TemplateResponse:
    """The portal's homepage."""
    return templates.TemplateResponse('homepage.jinja', {'request': request})

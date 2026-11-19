"""
process liveness endpoint
"""

import fastapi

router = fastapi.APIRouter()


@router.get("/health")
async def health_check() -> dict[str, str]:
    """
    report that the application can serve requests without checking dependencies
    """

    return {"status": "ok"}

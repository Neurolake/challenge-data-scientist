"""This module includes API routers."""
from fastapi import APIRouter
from .endpoints.performance import router as perf_router
from .endpoints.aderencia import router as ader_router
router = APIRouter()

# Routers from each endpoint
router.include_router(perf_router)
router.include_router(ader_router)

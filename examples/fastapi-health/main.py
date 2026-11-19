"""FastAPI application for the health check example."""

import fastapi

import health

app = fastapi.FastAPI(title="Health API")
app.include_router(health.router)

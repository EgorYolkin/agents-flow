"""
serve the health check example with FastAPI
"""

import fastapi

import health

app = fastapi.FastAPI(title="Health API")
app.include_router(health.router)

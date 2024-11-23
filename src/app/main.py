from starlette.middleware.cors import CORSMiddleware

from .api import router
from .core.config import settings
from .core.setup import create_application

app = create_application(router=router, settings=settings, create_tables_on_start=False)

# CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

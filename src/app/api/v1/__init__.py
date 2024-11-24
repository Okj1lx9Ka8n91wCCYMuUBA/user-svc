from fastapi import APIRouter

from .login import router as login_router
from .logout import router as logout_router
from .posts import router as posts_router
from .rate_limits import router as rate_limits_router
from .tasks import router as tasks_router
from .tiers import router as tiers_router
from .users import router as users_router
from .questions import router as questions
# from .parsing_results import router as parser
from .news import router as news_router
from .startup import router as startup
from .parsed_data.grants import router as grants
from .docs.passport import router as passport


router = APIRouter(prefix="/v1")
router.include_router(login_router)
router.include_router(logout_router)
router.include_router(users_router)
router.include_router(posts_router)
router.include_router(tasks_router)
router.include_router(tiers_router)
router.include_router(rate_limits_router)
router.include_router(questions)
# router.include_router(parser)
router.include_router(news_router)
router.include_router(startup)
router.include_router(grants)
router.include_router(passport)

from django import urls
from rest_framework import routers

import apps.polls.views as pollsviews


router = routers.DefaultRouter()
router.register(r'polls', pollsviews.PollView)

urlpatterns = [
    urls.path('', urls.include(router.urls)),
]

from django.urls import path, include
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

# from .views import ArticleList, ArticleDetails

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')

urlpatterns = [
    path('', include(router.urls))


    # path('articles/', ArticleList.as_view()), #MON FAVORIE
    # path('articles/<int:id>/', ArticleDetails.as_view())
]

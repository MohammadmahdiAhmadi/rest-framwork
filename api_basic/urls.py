from django.urls import path, include
# from .views import article_list, article_detail
# from .views import ArticleAPIView, ArticleDetail
# from .views import ArticleGenericAPIView, DetailGenericAPIView
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    # path('articles/', article_list), 
    # path('articles/', ArticleAPIView.as_view()),
    # path('articles/', ArticleGenericAPIView.as_view()),
    # path('detail/<int:pk>/', article_detail),
    # path('detail/<int:id>/', ArticleDetail.as_view()),
    # path('detail/<int:id>/', DetailGenericAPIView.as_view()),
    
    path('viewset/', include(router.urls))
]

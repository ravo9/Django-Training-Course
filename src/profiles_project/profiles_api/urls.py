from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    # APIView
    url(r'^hello-view/', views.HelloApiView.as_view()),
    # Viewset
    url(r'', include(router.urls))
    # Right now the app will check APIView's url first - if it's not gonna be
    # matched - it will go to check the viewset (that's why we pass an empty
    # string).
]

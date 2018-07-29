from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
# When we register a model viewset, we don't hae to provide a base nameself.
# It's gonna be retrieved from our model.
# The first argument is an URL prefix.
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    # APIView
    url(r'^hello-view/', views.HelloApiView.as_view()),
    # Viewset
    url(r'', include(router.urls))
    # Right now the app will check APIView's url first - if it's not gonna be
    # matched - it will go to check the viewset (that's why we pass an empty
    # string).
]

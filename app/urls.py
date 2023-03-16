

from django.contrib import admin
from django.urls import path, include
from app.views import UserRegistrationView, SchoolView, ClassesView, UserDetails, LoginView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("classes", ClassesView, basename="Class-details")
router.register("schools", SchoolView, basename="school-details")
router.register("register-details", UserDetails,
                basename="user details")
urlpatterns = [
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('register/', UserRegistrationView.as_view(), name="user registration")
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls

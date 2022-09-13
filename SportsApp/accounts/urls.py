from django.urls import path, include
from accounts.views import MyTokenObtainPairView, UserViewset, AccountForgetViewSet
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from django.urls import path
router = DefaultRouter()
# User_Register_API_URL
router.register(r'register', UserViewset, basename='register'),
router.register(r'forget-password', AccountForgetViewSet, basename='forgetpass')


urlpatterns = [
    path('', include(router.urls)),
    # User_Login_API_URL
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


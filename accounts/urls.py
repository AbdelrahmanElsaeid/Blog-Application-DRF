from django.urls import include, path
from .views import SignUp,ProfileDetailView


urlpatterns = [
    
    path('auth/', include('dj_rest_auth.urls')),
    path('signup/',SignUp.as_view(), name='signup'),
    path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
    
]
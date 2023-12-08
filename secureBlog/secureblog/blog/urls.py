from . import views
from django.urls import path
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

"""
router = routers.DefaultRouter()
router.register(r'users',  views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts',  views.PostViewSet)
"""

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('summernote/', include('django_summernote.urls')),
    path('markdownx/', include('markdownx.urls')),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('search/', views.search, name='search'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path('users/logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('captcha/', include('captcha.urls')),
    #path('post/<slug>/', views.PostDetail.as_view(), name = 'post'),
    # path('api/', include(router.urls)),
    # path('api/auth/', include('rest_framework.urls', namespace="rest_framework")),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

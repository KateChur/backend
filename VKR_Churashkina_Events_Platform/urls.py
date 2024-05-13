"""
URL configuration for VKR_Churashkina_Events_Platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path(r'api/v1/', include('mainpage.urls')),
    path(r'api/v1/', include('eventpage.urls')),
    path(r'api/v1/', include('login.urls')),
    path(r'api/v1/', include('register.urls')),
    path(r'api/v1/', include('locations.urls')),
    path(r'api/v1/', include('order.urls')),
    path(r'api/v1/', include('recommendations.urls')),
    path(r'admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

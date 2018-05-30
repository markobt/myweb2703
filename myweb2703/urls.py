"""myweb2703 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path, re_path
from todos import  views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('', views.HomePageView.as_view(), name='home'),
    re_path(r'^(?P<deploy_id>\d+)/$', views.deploy_detail, name='deploy_detail.html'),
]


#repath
# example.com/1/
# example.com/33/

#\d
#When the UNICODE flag is not specified, matches any decimal digit; this is equivalent to the set [0-9].
#With UNICODE, it will match whatever is classified as a decimal digit in the Unicode character properties database.
"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_swagger.views import get_swagger_view
from django.views.generic.base import TemplateView
from django.conf import settings
from django.views.static import serve

schema_view = get_swagger_view(title='ShipTalent API')

urlpatterns = [
  url(r'^apis', schema_view),
  url(r'^admin/', admin.site.urls),
  url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
  url(r'^api/v1/auth/', include('authentication.urls')),
  url(r'^api/v1/talent', include('talent.urls')),
  url(r'^api/v1/talent_position_type', include('talent_position_type.urls')),
  url(r'^api/v1/talent_position_sub_type', include('talent_position_sub_type.urls')),
  url(r'^api/v1/talent_additional_position_type', include('talent_additional_position_type.urls')),
  url(r'^api/v1/talent_additional_position_sub_type', include('talent_additional_position_sub_type.urls')),
  url(r'^api/v1/talent_visa', include('talent_visa.urls')),
  url(r'^api/v1/talent_language', include('talent_language.urls')),
  url(r'^api/v1/talent_picture', include('talent_picture.urls')),
  url(r'^api/v1/talent_resume', include('talent_resume.urls')),
  url(r'^api/v1/talent_video', include('talent_video.urls')),
  url(r'^api/v1/talent_medical', include('talent_medical.urls')),
  url(r'^api/v1/question', include('question.urls')),
  url(r'^api/v1/shiptalent_info', include('shiptalent_info.urls')),
  url(r'^api/v1/submission', include('submission.urls')),
  url(r'^api/v1/video_interview_settings', include('admin_setting.urls')),
  url(r'^api/v1/client_casting_request', include('client_casting_request.urls')),
]

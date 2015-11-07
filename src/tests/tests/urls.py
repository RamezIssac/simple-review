from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from test_app import views
from simple_review.views import post_review
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^detail-test/(?P<pk>\w+)$', views.InfoDetail.as_view(), name='info_detail'),
    url(r'^post_review/$', post_review, name='post_review'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
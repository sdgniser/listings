from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

app_name = 'main'
urlpatterns = [
    path('', index, name = 'index'),
    path('submit/', SubmitView.as_view(), name = 'submit'),
    path('listing/<int:pk>', ListingDetail.as_view(), name = 'listing'),
    path('search/', search, name = 'search'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

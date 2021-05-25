from django.urls import path, include
from . import views
from gram.views import AddDislike, ImageList, PostCreate, PostDetail, AddLike
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', ImageList.as_view(), name='list'),
    path('new/', PostCreate.as_view(), name='new'),
    path('post/<pk>/', PostDetail.as_view(), name='detail'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),




]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
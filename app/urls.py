from django.urls import path

from app.views import PostListApiView, OfficeListApiView


urlpatterns = [
    path(
        'posts/',  # урл для posts
        PostListApiView.as_view()  # вызываем класс представления как вью
    ),

    path(
        'office/',  # урл для office
        OfficeListApiView.as_view()  # вызываем класс представления как вью
    ),
]

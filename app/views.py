from rest_framework import generics  # Готовые представления для наследования
from rest_framework.permissions import AllowAny  # Импорт прав доступа к представлению

from .models import Office, Post
from .serializers import OfficeSerializer, PostSerializer


class OfficeListApiView(generics.ListAPIView):
	"""
	Класс представления для просмотра данных Offcie
	ListAPIView - предоставляет логику для просмотра записей
	есть множество других, их можно найти провалившись в модуль generics (нажать cntrl + лкм)
	:param queryset, serializer_class, permission_classes
	"""

	queryset = Office.objects.all()  # Данные с которыми хотим производить манипуляции
	serializer_class = OfficeSerializer  # Класс сериализации для валидации и сериализации данных
	permission_classes = [AllowAny, ]  # Права доступа к представлению. AllowAny - доступ открыт для всех


class PostListApiView(generics.ListAPIView):
	"""
	Класс представления для просмотра данных Post
	:param queryset, serializer_class, permission_classes
	"""

	queryset = Post.objects.all()  # Данные с которыми хотим производить манипуляции
	serializer_class = PostSerializer  # Класс сериализации для валидации и сериализации данных
	permission_classes = [AllowAny, ]  # Права доступа к представлению

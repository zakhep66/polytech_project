from rest_framework import serializers

from .models import Office, Post


class OfficeSerializer(serializers.ModelSerializer):
	"""
	Сериалайзер для модели Office
	:param модель которую нужно валидировать и преобразовать в json\xml
	:return сериализованный объект
	"""

	# определяем поле, которое нужно вытащить из связной модели
	post_name = serializers.SerializerMethodField('get_post_name')  # get_post_name - название метода на 16 строке

	def get_post_name(self, obj):
		"""
		Метод для добавления поля name через связь между моделями Post и Office
		Вместо id будет отображаться name
		:param obj: объект модели Office
		:return: name из модели Post
		"""
		return obj.post.name

	class Meta:
		model = Office  # Модель с которой работает сериалайзер
		fields = [
			'name',
			'post_name',
		]  # поля из модели Office которые нужно сериализовать + те, что мы добавили с помощью SerializerMethodField


class PostSerializer(serializers.ModelSerializer):
	"""
	Сериалайзер для модели Post
	:param модель которую нужно валидировать и преобразовать в json\xml
	:return сериализованный объект
	"""

	class Meta:
		model = Post  # Модель с которой работает сериалайзер
		fields = [
			'id',
			'name',
		]  # поля из модели Post которые нужно сериализовать

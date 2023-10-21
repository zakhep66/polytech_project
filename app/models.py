from django.db import models


class Office(models.Model):
	name = models.CharField(max_length=100)
	post = models.ForeignKey(  # Здесь будет храниться id связанной записи
		'Post',  # Модель с которой связываем
		on_delete=models.CASCADE,  # Сценарий при удалении связной записи
		related_name='office'  # Имя обратного обращения
	)  # Внешний ключ к модели Post

	class Meta:
		verbose_name = 'Офис'
		verbose_name_plural = 'Офисы'


class Post(models.Model):
	name = models.CharField(max_length=100)

	class Meta:
		verbose_name = 'Письмо'
		verbose_name_plural = 'Письма'



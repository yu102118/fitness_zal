from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    verbose_name='Пользователь',
    null=True, blank=True
)  # связь с пользователем
    
    age = models.IntegerField('Возраст')
    text = models.TextField('Отзыв')
    date_posted = models.DateTimeField('Дата отзыва', auto_now_add=True)

    def __str__(self):
        return f' {self.age}'

    def get_absolute_url(self):
        return f'/reviews/{self.id}'
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
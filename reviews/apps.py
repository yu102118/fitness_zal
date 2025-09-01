from django.apps import AppConfig


class ReviewsConfig(AppConfig):  # ✅ Имя класса тоже меняем
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reviews'             # ✅ Название нового приложения
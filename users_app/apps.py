from django.apps import AppConfig



class UsersAppConfig(AppConfig):
    name = 'users_app'
    verbose_name = 'Пользователи'

    def ready(self):
        import users_app.signals  # noqa: F401

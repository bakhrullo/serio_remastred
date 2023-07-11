# import django
from django.apps import AppConfig
# django.setup()
class SerioAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'serio_app'
    verbose_name = 'Boshqaruv'
    def ready(self):
        sections = ['Bosh menu', 'Bosh kategoriya', 'Kategoriya', 'Kichik kategoriya', 'Xizmatlar']
        from serio_app.models import Images
        if len(Images.objects.all()) == 0:
            for i in sections:
                Images.objects.create(name=i)

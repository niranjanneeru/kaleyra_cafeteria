from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "kaleyra_cafeteria.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import kaleyra_cafeteria.users.signals  # noqa F401
        except ImportError:
            pass

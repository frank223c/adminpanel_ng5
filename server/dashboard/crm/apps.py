from django.apps import AppConfig


class CrmConfig(AppConfig):
    name = 'dashboard.crm'
    verbose_name = "Crm"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass

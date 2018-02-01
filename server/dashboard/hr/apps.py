from django.apps import AppConfig


class HrConfig(AppConfig):
    name = 'dashboard.hr'
    verbose_name = "HumanResources"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass

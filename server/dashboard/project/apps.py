from django.apps import AppConfig


class ProjectConfig(AppConfig):
    name = 'dashboard.project'
    verbose_name = "Project"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass

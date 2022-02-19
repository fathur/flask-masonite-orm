"""Application Observer"""
import inspect


class ApplicationObserver:

    def creating(self, application):
        """Handle the Application "creating" event.

        Args:
            application (masoniteorm.models.Model): Application model.
        """
        pass

    def created(self, application):
        """Handle the Application "created" event.

        Args:
            application (masoniteorm.models.Model): Application model.
        """

        from app.models.audit_log import AuditLog

        event = inspect.currentframe().f_code.co_name
        AuditLog.audit_model(application, event)

    def saving(self, application):
        """Handle the Application "saving" event.

        Args:
            application (masoniteorm.models.Model): Application model.
        """
        pass

    def saved(self, application):
        """Handle the Application "creating" event.

        Args:
            application (masoniteorm.models.Model): Application model.
        """
        pass

    def updating(self, application):
        """Handle the Application "creating" event.

        Args:
            application (masoniteorm.models.Model): Application model.
        """
        # Check that is application status locked
        pass

    def updated(self, application):
        """Handle the Application "creating" event.

        Args:
            application (masoniteorm.models.Model): Application model.
        """
        from app.models.audit_log import AuditLog

        event = inspect.currentframe().f_code.co_name
        AuditLog.audit_model(application, event)

    def booted(self, application):
        """Handle the Application "creating" event.

        Args:
            application (masoniteorm.models.Model): Application model.
        """
        pass

    def booting(self, application):
        """Handle the Application "creating" event.

        Args:
            application (masoniteorm.models.Model): Application model.
        """
        pass

    def hydrating(self, application):
        """Handle the Application "creating" event.

        Args:
            application (masoniteorm.models.Model): Application model.
        """
        pass

    def hydrated(self, application):
        """Handle the Application "creating" event.

        Args:
            application (masoniteorm.models.Model): Application model.
        """
        pass

    def deleting(self, application):
        """Handle the Application "creating" event.

        Args:
            application (masoniteorm.models.Model): Application model.
        """
        pass

    def deleted(self, application):
        """Handle the Application "creating" event.

        Args:
            application (masoniteorm.models.Model): Application model.
        """
        from app.models.audit_log import AuditLog

        event = inspect.currentframe().f_code.co_name
        AuditLog.audit_model(application, event)

"""User Observer"""
import inspect


class UserObserver:

    def creating(self, user):
        """Handle the User "creating" event.

        Args:
            user (masoniteorm.models.Model): User model.
        """
        pass

    def created(self, user):
        """Handle the User "created" event.

        Args:
            user (masoniteorm.models.Model): User model.
        """
        from app.models.audit_log import AuditLog

        event = inspect.currentframe().f_code.co_name
        AuditLog.audit_model(user, event=event)

    def saving(self, user):
        """Handle the User "saving" event.

        Args:
            user (masoniteorm.models.Model): User model.
        """
        from argon2 import PasswordHasher
        ph = PasswordHasher()
        user.password = ph.hash(user.password)

    def saved(self, user):
        """Handle the User "creating" event.

        Args:
            user (masoniteorm.models.Model): User model.
        """
        pass

    def updating(self, user):
        """Handle the User "creating" event.

        Args:
            user (masoniteorm.models.Model): User model.
        """
        pass

    def updated(self, user):
        """Handle the User "creating" event.

        Args:
            user (masoniteorm.models.Model): User model.
        """
        from app.models.audit_log import AuditLog

        event = inspect.currentframe().f_code.co_name
        AuditLog.audit_model(user, event=event)

    def booted(self, user):
        """Handle the User "creating" event.

        Args:
            user (masoniteorm.models.Model): User model.
        """
        pass

    def booting(self, user):
        """Handle the User "creating" event.

        Args:
            user (masoniteorm.models.Model): User model.
        """
        pass

    def hydrating(self, user):
        """Handle the User "creating" event.

        Args:
            user (masoniteorm.models.Model): User model.
        """
        pass

    def hydrated(self, user):
        """Handle the User "creating" event.

        Args:
            user (masoniteorm.models.Model): User model.
        """
        pass

    def deleting(self, user):
        """Handle the User "creating" event.

        Args:
            user (masoniteorm.models.Model): User model.
        """
        pass

    def deleted(self, user):
        """Handle the User "creating" event.

        Args:
            user (masoniteorm.models.Model): User model.
        """
        from app.models.audit_log import AuditLog

        event = inspect.currentframe().f_code.co_name
        AuditLog.audit_model(user, event=event)

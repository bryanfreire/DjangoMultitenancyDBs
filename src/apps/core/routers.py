from django.conf import settings
import apps.core.middlewares as coremiddle


class AuthRouter:

    auth_db_name = 'auth'

    route_app_labels = {
        'admin',
        'auth',
        'authtoken',
        'core',
        'sessions',

        'contenttypes',
    }

    exclusive_route_app_labels = route_app_labels - {
        'contenttypes',
    }

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.exclusive_route_app_labels:
            return self.auth_db_name
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.exclusive_route_app_labels:
            return self.auth_db_name
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels and
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == self.auth_db_name and app_label in self.route_app_labels:
            result = True
        elif db == self.auth_db_name or app_label in self.exclusive_route_app_labels:
            result = False
        else:
            result = None
        return result


class RealmsRouter:

    def db_for_read(self, model, **hints):
        return coremiddle.get_db_name()

    def db_for_write(self, model, **hints):
        return coremiddle.get_db_name()

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return None

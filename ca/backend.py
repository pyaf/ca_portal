from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



class PasswordlessAuthBackend(ModelBackend):

    """Log in to Django without providing a password.
    """
    def authenticate(self, username=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel._default_manager.get_by_natural_key(username)
            return user
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

            # def authenticate(self, hash=None):
            #     user = get_user_from_hash(hash)
            #     return user

    # def authenticate(self, username=None):
    #     try:
    #         return User.objects.get(username=username)
    #     except User.DoesNotExist:
    #         return None

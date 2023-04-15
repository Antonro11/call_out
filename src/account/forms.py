from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class PerformerRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "photo",
            "nickname",
            "first_name",
            "last_name",
            "email",
            "gender",
            "dance_style",
            "promo_video",
            "password1",
            "password2",
        )


class SpectatorRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("photo", "first_name", "last_name", "email", "gender", "password1", "password2")

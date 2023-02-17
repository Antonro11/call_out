from account.models import Customer


def sample_account(**params):
    default = {
        "email": "anton@admin.com",
        "first_name": "Anton",
        "last_name": "Riabkov",
        "password": "admin",
        "user_type": "performer",
        "nickname": "Anton",
        "dance_style": "Popping",
        "country": "Ukraine",
        "city": "Dnipro",
        "gender": "M",
    }
    default.update(params)
    return Customer.objects.create(**default)

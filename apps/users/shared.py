# import random
# import string
#
# import requests
# from django.conf import settings
from django.core.cache import cache
from django.utils import timezone

from apps.users.cache import generate_cache_key


def send_verification_code(phone, type_, session):
    # message_id = str(timezone.now())
    # code = "".join(random.choice(string.digits) for _ in range(6))
    code = "123456"
    # requests.post(
    #     settings.SMS_URL,
    #     auth=(settings.SMS_LOGIN, settings.SMS_PASSWORD),
    #     json={
    #         "messages": [
    #             {
    #                 "recipient": phone,
    #                 "message-id": message_id,
    #                 "sms": {
    #                     "originator": "3700",
    #                     "content": {
    #                         "text": f"auto.uz <#> Sizning maxfiy kodingiz: {code}",
    #                     },
    #                 },
    #             }
    #         ]
    #     },
    # )

    cache.set(generate_cache_key(type_, phone, session), code, timeout=120)

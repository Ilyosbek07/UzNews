class CacheTypes:
    registration_sms_verification = "registration_sms_verification"
    forget_pass_verification = "forget_pass_verification"


def generate_cache_key(type_, *args):
    # Ensure that all arguments are valid strings
    args = [str(arg) for arg in args if arg is not None]

    # Concatenate the type and arguments
    cache_key = f"{type_}{''.join(args)}"
    return cache_key


def require_not_none(obj):
    if obj is None:
        raise ValueError("Value cannot be None!")
    return obj
import functools

def wrap(func):
    @functools.wraps(func)
    def wrapper(**kwargs):
        return func(**kwargs)

    return wrapper


def add_path(rest_method, api_path):
    """
    bypass decorator to modify the original function
    it replaces the original @api_request decorator
    Returns:
        function with additional attributs
        new attributs = decorator parmaeters
    The simplest option would have been to add args to the func kwargs,
    but the func is generic and it may not have **kwargs...
    """

    def outer_wrap(func):
        func.rest_method = rest_method
        func.api_path = api_path
        return wrap(func)

    return outer_wrap
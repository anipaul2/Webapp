from functools import wraps
def decorator_name(func) :
    @wraps(func)
    def wrapper(*args, **kwargs) :
        # 1. Code to execute before calling the executed function.
        # 2. Call the decorated function as required, returning it's results if needed.
             return func(*args, **kwargs)
             
        # 3. code to execute instead of calling the decorated function.
    return wrapper

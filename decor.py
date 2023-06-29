# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         return original_function(*args, **kwargs)

#     return wrapper_function


# @decorator_function
# def display():
#     print("display function ran successfully")


# @decorator_function
# def display_info(name, age):
#     print("display_info with args {}, {}".format(name, age))


# display()

# display_info("Damodar", 39)

# decorated_display = decorator_function(display)
# decorated_display()


# decorated_display_info = decorator_function(display_info)
# decorated_display_info("damodar", 22)


def outer_func():
    message = "Hi"

    def inner_func():
        print(message)

    return inner_func


result_inner = outer_func()

result_inner()

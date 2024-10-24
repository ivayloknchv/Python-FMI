def handle_input(valid_types, *args, **kwargs):
    """Check if the types of the arguments are valid."""
    all_args = args + tuple(kwargs.values())
    for arg in all_args:
        if not isinstance(arg, valid_types):
            formatted_message = ', '.join([str(valid_type) for valid_type in valid_types])
            print(f'Invalid input arguments, expected {formatted_message}!')
            return


def handle_output(result, valid_types):
    """Check if the type of the returned value is valid."""
    if not isinstance(result, valid_types):
        formatted_message = ', '.join([str(valid_type) for valid_type in valid_types])
        print(f'Invalid output value, expected {formatted_message}!')


def type_check(io_operation):
    """Verify input and output of a function."""
    def valid_types_wrapper(*valid_types):
        def decorator(func):
            def function_arguments_wrapper(*args, **kwargs):
                if io_operation == 'in':
                    handle_input(valid_types, *args, **kwargs)
                result = func(*args, **kwargs)
                if io_operation == 'out':
                    handle_output(result, valid_types)
                return result
            return function_arguments_wrapper
        return decorator
    return valid_types_wrapper

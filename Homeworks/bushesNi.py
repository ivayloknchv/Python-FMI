def is_valid_bush(potential_bush):
    valid_keys = ('храст', 'shrub', 'bush')

    if type(potential_bush) is dict:
        if 'name' in potential_bush:
            if potential_bush['name'].lower() in valid_keys:
                return True
    return False


def not_too_expensive(total_cost):
    max_cost = 42.00
    return total_cost <= max_cost


def one_that_looks_nice(unique_letters, total_cost):
    integer_cost = int(total_cost)
    return integer_cost != 0 and len(unique_letters) % integer_cost == 0


def function_that_says_ni(*args, **kwargs):
    total_cost = 0.00
    unique_letters = set()

    for arg in args:
        if is_valid_bush(arg):
            total_cost += arg.get('cost', 0)

    for key, value in kwargs.items():
        if is_valid_bush(value):
            current_letters = set(key)
            unique_letters |= current_letters
            total_cost += value.get('cost', 0)

    if not_too_expensive(total_cost) and one_that_looks_nice(unique_letters, total_cost):
        return f'{total_cost:.2f}лв'

    else:
        return 'Ni!'

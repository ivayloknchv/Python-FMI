
def swap_decorator(func):
    def args_wrapper(**kwargs):
        new_kwargs = {}
        for key, value in kwargs.items():
            new_kwargs[value] = key
        res = func(**new_kwargs)
        return res
    return args_wrapper

@swap_decorator
def func_demo(**kwargs):
    concat_str1='-'.join(kwargs.keys())
    concat_str2 = '-'.join(kwargs.values())
    return concat_str1+'\n'+concat_str2


class InfiniteContextManager:
    _counter=1

    def __int__(self):
        self._counter+=1

    def __enter__(self):
        return  self

    def __call__(self):
        self._counter+=1
        return self

    def __len__(self):
        return self._counter

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._counter = 0


class Storage:

    def __init__(self, my_type, **kwargs):
        self.my_type = my_type
        self.storage = {}

        for key, value in kwargs.items():
            temp = my_type(key = value)
            self.storage[key]= temp

    def __len__(self):
        return len(self.storage)

    def __getitem__(self, name):
        return self.storage[name]


class Example:

    def __init__(self, **kwargs):
        print(f'New example instance created from {kwargs}')
        self._kwargs = kwargs

    def __str__(self):
        return f"Example instance created form {self._kwargs}"

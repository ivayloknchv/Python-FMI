import re
from collections import OrderedDict
from random import randint


class SingletonMeta(type):

    _all_instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._all_instances:
            instance = super().__call__(*args, **kwargs)
            cls._all_instances[cls] = instance
        return cls._all_instances[cls]


class Kid(type):

    def __new__(cls, name, bases, attr_dict):
        if '__call__' not in attr_dict:
            raise NotImplementedError("Error")

        def age_up(self):
            self.age += 1

        def be_good(self):
            self.is_naughty = False

        original_init = attr_dict.get('__init__', None)

        attr_dict['__init__'] = cls._init_decorator(original_init)
        attr_dict['age_up'] = age_up
        attr_dict['be_good'] = be_good

        for method_name, method in attr_dict.items():
            if callable(method) and not method_name.startswith('_'):
                attr_dict[method_name] = cls._class_method_naughty_decorator(method)

        return type.__new__(cls, name, bases, attr_dict)

    @staticmethod
    def _class_method_naughty_decorator(func):
        def wrapper(self, *args, **kwargs):
            try:
                res = func(self, *args, **kwargs)
                return res
            except:
                self.is_naughty = True
                raise

        return wrapper

    @staticmethod
    def _init_decorator(init_func):
        def wrapper(self, *args, **kwargs):
            if init_func:
                init_func(self, *args, **kwargs)
            self.is_naughty = False
            self.age = 0
            Santa.detect_new_kid(self)

        return wrapper


class Santa(metaclass=SingletonMeta):

    _XMAS_LIMIT = 5
    _NAUGHTY_KIDS_GIFT = 'coal'
    _all_kids = {} # id -> instance
    _gifts = OrderedDict() # id -> gift

    @classmethod
    def detect_new_kid(cls, kid):
        cls._all_kids[id(kid)] = kid

    @staticmethod
    def _get_signature(wish):
        target = re.search(r'^\s*(\d+)\s*$', wish, re.MULTILINE)
        return target.group(1)

    @staticmethod
    def _get_gift(wish):
        if res := re.search(r'"([A-Za-z0-9 ]+)"', wish):
            return res.group(1)
        elif res := re.search(r'\'([A-Za-z0-9 ]+)\'', wish):
            return res.group(1)

    def __call__(self, child, call):
        self._gifts[id(child)] = self._get_gift(call)

    def __matmul__(self, letter):
        signature = int(self._get_signature(letter))
        self._gifts[signature] = self._get_gift(letter)

    def __iter__(self):
        return SantaIter(list(self._gifts.values()))

    def _post_xmas(self):
        """Age up all kids and make them well-behaved again"""

        for kid in self._all_kids.values():
            kid.age_up()
            kid.be_good()

        self._gifts.clear()

    def _get_most_frequent_gifts(self):

        freq_dict = {}

        for gift in self._gifts.values():
            if gift not in freq_dict:
                freq_dict[gift] = 1
            else:
                freq_dict[gift] += 1

        max_freq = max(freq_dict.values())

        return [gift for gift, count in freq_dict.items() if count == max_freq]

    def _give_gifts(self):
        most_freq_gifts = self._get_most_frequent_gifts()

        for kid_id, kid in self._all_kids.items():
            if kid.age < self._XMAS_LIMIT:
                if kid.is_naughty:
                    kid(self._NAUGHTY_KIDS_GIFT)
                elif kid_id in self._gifts.keys():
                    kid(self._gifts[kid_id])
                else:
                    random_idx = randint(0, len(most_freq_gifts) - 1)
                    kid(most_freq_gifts[random_idx])

    def xmas(self):
        if self._gifts:
            self._give_gifts()
        self._post_xmas()


class SantaIter:

    def __init__(self, gifts):
        self.gifts = gifts
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < len(self.gifts):
            curr = self.gifts[self.idx]
            self.idx += 1
            return curr
        else:
            self.idx = 0
            raise StopIteration

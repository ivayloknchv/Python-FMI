BASICS_DENSITY = {
    'Concrete': 2500,
    'Brick': 2000,
    'Stone': 1600,
    'Wood': 600,
    'Steel': 7700
}

class Material:
    _DENSITY = 1

    def __init__(self, mass):
        self.mass = mass
        self.is_used = False

    @property
    def volume(self):
        return self.mass / self._DENSITY


class Concrete(Material):
    _DENSITY = BASICS_DENSITY['Concrete']


class Brick(Material):
    _DENSITY = BASICS_DENSITY['Brick']


class Stone(Material):
    _DENSITY = BASICS_DENSITY['Stone']


class Wood(Material):
    _DENSITY = BASICS_DENSITY['Wood']


class Steel(Material):
    _DENSITY = BASICS_DENSITY['Steel']


class Factory:
    """Create different building materials including some interesting 'alloys'.
    A fancy way to demonstrate the factory design pattern"""

    _valid_classes = {
        'Concrete': Concrete,
        'Brick': Brick,
        'Stone': Stone,
        'Wood': Wood,
        'Steel': Steel
    }  # we start with the basic classes first and gradually add dynamic ones

    _all_produced_materials = []

    def __init__(self):
        self._produced_materials = []

    def _handle_kwargs(self, **kwargs):
        materials_list = []
        for material_name, mass in kwargs.items():
            if material_name not in self._valid_classes:
                raise ValueError('Invalid class name!')
            materials_list.append(self._valid_classes[material_name](mass))
        self._produced_materials.extend(materials_list)
        self._all_produced_materials.extend(materials_list)
        return tuple(materials_list)

    @staticmethod
    def _create_new_class(class_name, density):
        new_class = type(class_name, (Material,), { '_DENSITY': density })
        return new_class

    def _handle_args(self, *args):
        total_mass = 0
        all_names = []

        for arg in args:
            if arg.is_used:
                raise AssertionError('This material is already used in some factory!')
            arg_class_name = type(arg).__name__
            total_mass += arg.mass
            split_names = arg_class_name.split('_')
            all_names.extend(split_names)

        for arg in args:  # in another loop to make sure no fails happen when we mix used and unused args
            arg.is_used = True

        all_names = sorted(all_names)
        combined_name = '_'.join(all_names)

        if combined_name not in self._valid_classes:
            avg_density = sum(BASICS_DENSITY[name] for name in all_names) / len(all_names)
            self._valid_classes[combined_name] = self._create_new_class(combined_name, avg_density)

        to_return = self._valid_classes[combined_name](total_mass)

        self._produced_materials.append(to_return)
        self._all_produced_materials.append(to_return)

        return to_return

    def __call__(self, *args, **kwargs):
        if (not args and not kwargs) or (args and kwargs):
            raise ValueError('Invalid arguments!')
        if kwargs:
            return self._handle_kwargs(**kwargs)
        elif args:
            return self._handle_args(*args)

    def can_build(self, target_volume):
        total_volume = sum(material.volume for material in self._produced_materials if not material.is_used)
        return total_volume >= target_volume

    @classmethod
    def can_build_together(cls, target_volume):
        total_volume = sum(material.volume for material in cls._all_produced_materials if not material.is_used)
        return total_volume >= target_volume

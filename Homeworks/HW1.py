viktors_ingredients = [
    'чушки', 'домати', 'моркови', 'ябълки',
    'сол', 'черен пипер', 'кимион', 'зехтин'
]

georgis_ingredients = (
    'чушки', 'домати', 'патладжан', 'люти чушки', 'олио',
    'захар', 'чубрица', 'черен пипер', 'врачанска ракия'
)

shopping_list = []
shopping_list.extend(viktors_ingredients)
shopping_list.extend(georgis_ingredients)
shopping_list = shopping_list[::-1]

unique_ingredients = set(shopping_list)
ingredient_quantities = dict.fromkeys(unique_ingredients, 5)
ingredient_quantities['skyr'] = 1

number_of_ingredients_to_buy = len(ingredient_quantities)

from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipes_view(request, dish):
    servings = int(request.GET.get('servings', 1))
    recipe = {}
    recipe_checker = DATA.get(dish)
    for key, value in recipe_checker.items():
        recipe[key] = float(value) * servings
    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context)



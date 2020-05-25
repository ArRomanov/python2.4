def get_cookbook():
    with open('recipes.txt', 'r') as file:
        cookbook = dict()
        current_recipe = ''
        for line in file:
            line = line.strip()
            if line and not any(map(str.isdigit, line)):
                current_recipe = line
                cookbook.setdefault(current_recipe, [])
            elif line and not line.isnumeric():
                name, count, measure = line.split(' | ')
                ingredient = {'ingredient_name': name, 'quantity': int(count), 'measure': measure}
                cookbook[current_recipe].append(ingredient)
    return cookbook


def get_shop_list_by_dishes(dishes, person_count):
    cookbook = get_cookbook()
    all_ingredients = dict()
    for dish in dishes:
        if dish in cookbook:
            dish_ingredients = cookbook[dish]
            for dish_ingredient in dish_ingredients:
                ingredient_name = dish_ingredient['ingredient_name']
                if ingredient_name not in all_ingredients:
                    all_ingredients[ingredient_name] = {'measure': dish_ingredient['measure'],
                                                        'quantity': person_count * dish_ingredient['quantity']}
                else:
                    all_ingredients[ingredient_name]['quantity'] += person_count * dish_ingredient['quantity']
    return all_ingredients


if __name__ == "__main__":
    shop_list = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
    print(shop_list)

def print_cook_book():
    with open('recipes.txt', 'r') as file:
        cook_book = dict()
        current_recipe = ''
        for line in file:
            line = line.strip()
            if line and not any(map(str.isdigit, line)):
                current_recipe = line
                cook_book.setdefault(current_recipe, [])
            elif line and not line.isnumeric():
                name, count, measure = line.split(' | ')
                ingredient = {'ingredient_name': name, 'quantity': count, 'measure': measure}
                cook_book[current_recipe].append(ingredient)
    from pprint import pprint
    pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    pass


if __name__ == "__main__":
    print_cook_book()

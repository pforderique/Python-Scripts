### Code Signal Practice Questions
#####################################

def groupingDishes(dishes):
    #for each dish's ingredient, add it to hash
    ingredients = {}
    for dish in dishes:
        dishName = dish[0]
        for idx in range(1, len(dish)):
            ingre = dish[idx]
            try:
                ingredients[ingre].append(dishName)
            except:
                ingredients[ingre] = []
                ingredients[ingre].append(dishName)
    
    out = []
    for key in sorted(ingredients.keys()):
        if len(ingredients[key]) >= 2:
            out.append([key]+sorted(ingredients[key]))
    return out

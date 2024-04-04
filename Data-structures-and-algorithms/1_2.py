# Операції над множинами. Реалізувати операції над множинами, 
# що задані у вигляді масивів. Операції – об’єднання, перетин, доповнення, 
# різниця, симетрична різниця.


def union(set1, set2):
    return list(set(set1 + set2))

def intersection(set1, set2):
    return list(set(set1) & set(set2))

def difference(set1, set2):
    return list(set(set1) - set(set2))

def symmetric_difference(set1, set2):
    return list(set(set1) ^ set(set2))

def complement(universe, set1):
    return list(set(universe) - set(set1))

# Приклад використання
set1 = [1, 2, 3, 4]
set2 = [3, 4, 5, 6]
universe = list(range(1, 11))

print("Об'єднання:", union(set1, set2))
print("Перетин:", intersection(set1, set2))
print("Доповнення до universe для множини 1:", complement(universe, set1))
print("Доповнення до universe для множини 2:", complement(universe, set2))
print("Різниця між множиною 1 та множиною 2:", difference(set1, set2))
print("Симетрична різниця:", symmetric_difference(set1, set2))

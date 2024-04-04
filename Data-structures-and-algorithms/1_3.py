# Дано рядок символів, що містить дужки різних видів 
# (круглі, фігурні, квадратні). Перевірте правильність розставлення в ньому 
# круглих дужок, будь-яких дужок.
# Наприклад, [ { ( } ) { ] [ } ( [ ] ) { }.

def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False
        else:
            continue
    return not stack

input_string = "[{()}]()"
if is_valid_parentheses(input_string):
    print("Дужки розставлені правильно.")
else:
    print("Дужки розставлені неправильно.")

input_string = "[{(}){][}([]){}"
if is_valid_parentheses(input_string):
    print("Дужки розставлені правильно.")
else:
    print("Дужки розставлені неправильно.")
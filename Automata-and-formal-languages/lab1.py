# Варіант - 17
# Соловей Євгеній

class Automaton:
    def __init__(self):
        self.transitions = {
            'q0': {'0': 'q0', '1': 'q0', '2': 'q1'},
            'q1': {'0': 'q1', '1': 'q1', '2': 'q2'},
            'q2': {'0': 'q2', '1': 'q2', '2': 'q3'},
            'q3': {'0': 'q3', '1': 'q3', '2': 'q4'},
            'q4': {'0': 'q4', '1': 'q4', '2': 'q5'},
            'q5': {'0': 'q5', '1': 'q5', '2': 'q5'}
        }
        self.start_state = 'q0'
        self.accept_states = {'q0', 'q1', 'q2', 'q3', 'q4'}

    def is_valid_input(self, input_string):
        for char in input_string:
            if char not in {'0', '1', '2'}:
                return False
        return True

    def process_input(self, input_string):
        current_state = self.start_state
        for char in input_string:
            if char not in self.transitions[current_state]:
                return False
            current_state = self.transitions[current_state][char]
        return current_state in self.accept_states


automaton = Automaton()


inputs = ["1012", "202", "00112", "2222", "102", "12a0", "22222", "22210"]
for inp in inputs:
    if automaton.is_valid_input(inp):
        if automaton.process_input(inp):
            print(f"'{inp}' - ПРИЙНЯТО")
        else:
            print(f"'{inp}' - НЕ ПРИЙНЯТО")
    else:
        print(f"'{inp}' - НЕВІРНИЙ ВВІД")

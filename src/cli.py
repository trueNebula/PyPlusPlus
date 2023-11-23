from finite_automata import FiniteAutomata

class CLI:
    def __init__(self) -> None:
        self.finite_automata = None
        self.commands = {
            '1': self.read,
            '2': self.print_states,
            '3': self.print_alphabet,
            '4': self.print_transitions,
            '5': self.print_initial_state,
            '6': self.print_final_states,
            '7': self.verify_deterministic,
            '8': self.verify_sequence,
        }
    
    def print_menu(self) -> None:
        print('1. Read FA')
        print('2. Print States')
        print('3. Print Alphabet')
        print('4. Print Transitions')
        print('5. Print Initial State')
        print('6. Print Final States')
        print('7. Verify DFA')
        print('8. Verify Sequence')

    def read(self) -> None:
        self.finite_automata = FiniteAutomata()
        file = input('Enter path: ')
        result = self.finite_automata.read(file)

        print(result)

    def print_states(self) -> None:
        print('States:')
        print(self.finite_automata.get_states())
    
    def print_alphabet(self) -> None:
        print('Alphabet:')
        print(self.finite_automata.get_alphabet())
    
    def print_transitions(self) -> None:
        print('Transitions:')
        print(self.finite_automata.get_transitions())
    
    def print_initial_state(self) -> None:
        print('Initial State:')
        print(self.finite_automata.get_initial_state())
    
    def print_final_states(self) -> None:
        print('Final States')
        print(self.finite_automata.get_final_states())
    
    def verify_deterministic(self) -> None:
        if self.finite_automata.is_deterministic():
            print('Deterministic Finite Automata')
        
        else:
            print('Non Deterministic Finite Automata')

    def verify_sequence(self) -> None:
        if self.finite_automata.is_deterministic():
            sequence = input('Enter sequence: ')

            if self.finite_automata.is_accepted(sequence):
                print('Accepted')
            
            else:
                print('Not Accepted')
        
        else:
            print('Non Deterministic Finite Automata')

    def run(self) -> None:
        self.print_menu()
        
        while True:
            cmd = input('> ')

            if cmd in self.commands.keys():
                self.commands[cmd]()
            
            else:
                print('Invalid Command')

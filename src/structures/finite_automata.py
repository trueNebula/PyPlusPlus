class FiniteAutomata:
    def __init__(self) -> None:
        self.states = []
        self.alphabet = []
        self.transitions = {}
        self.initial_state = None
        self.final_states = []
        self.err = None

    def read(self, filename) -> str:
        with open(filename, 'r') as f:
            lines = f.readlines()
            lines = [line.replace('\n', '').strip() for line in lines]

            self.states = lines[0].split(' ')
            self.alphabet = lines[1].split(' ')
            self.initial_state = lines[2]
            self.final_states = lines[3].split(' ')

            for i in range(4, len(lines)):
                transition = lines[i].split(' ')
                initial = transition[0]
                route = transition[1]
                final = transition[2]

                if (initial, route) in self.transitions.keys():
                    self.transitions[(initial, route)].append(final)
                else:
                    self.transitions[(initial, route)] = []
                    self.transitions[(initial, route)].append(final)

        self.validate()

        if self.err is not None:
            return self.err
        
        return 'All good!'

    def validate(self) -> None:
        if self.initial_state not in self.states:
            self.err = 'Initial state not found among given states.'
            return
        
        for state in self.final_states:
            if state not in self.states:
                self.err = 'Final state ' + state + ' not found among given states.'
                return
        
        for transition in self.transitions.keys():
            if transition[0] not in self.states or transition[1] not in self.alphabet:
                self.err = 'Transition ' + str(transition) + ' invalid!'
                return

            for final_state in self.transitions[transition]:
                if final_state not in self.states:
                    self.err = 'Transition ' + str(transition) + ' invalid ' + final_state
                    return

        for state in self.states:
            if state in self.alphabet:
                self.err = 'State ' + state + ' overlapping alphabet.'
        
        return
    
    def is_deterministic(self) -> bool:
        for key in self.transitions.keys():
            if len(self.transitions[key]) > 1:
                return False

        return True
    
    def is_accepted(self, sequence) -> bool:
        if not self.is_deterministic():
            return False
        
        state = self.initial_state
        for symbol in sequence:
            if (state, symbol) in self.transitions.keys():
                state = self.transitions[(state, symbol)][0]
            else:
                return False
        
        return state in self.final_states

    def get_states(self):
        return self.states
    
    def get_alphabet(self):
        return self.alphabet

    def get_transitions(self):
        return self.transitions

    def get_initial_state(self):
        return self.initial_state
    
    def get_final_states(self):
        return self.final_states

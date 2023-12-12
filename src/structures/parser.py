from structures.config import Configuration
from structures.grammar import Grammar

class Parser:
    def __init__(self, grammar: Grammar, word) -> None:
        self.grammar = grammar
        self.word = word
        self.config = Configuration(grammar.start_symbol)

    def momentary_insuccess(self) -> None:
        self.config.current_state = 'back'

    def advance(self) -> None:
        head = self.config.pop_input()
        terminal = head[0]

        if len(head) > 1:
            self.config.push_input(head[1:])
        
        self.config.push(terminal)
        self.config.increment()
    
    def back(self) -> None:
        self.config.decrement()
        head = self.config.pop()
        self.config.push_input([head])
    
    def success(self) -> None:
        self.config.current_state = 'final'

    def get_config(self):
        return self.config

from structures.config import Configuration
from structures.grammar import Grammar


class Parser:
    def __init__(self, grammar: Grammar, word, state='normal') -> None:
        self.grammar = grammar
        self.word = word
        self.state = state
        self.config = Configuration(grammar.start_symbol)

    def expand(self):
        # WHEN: head of input stack is a nonterminal
        # (q, i, 𝜶, A𝜷) ⊢ (q, i, 𝜶A1, 𝜸1𝜷)
        # where:
        # A → 𝜸1 | 𝜸2 | … represents the productions corresponding to A
        # 1 = first prod of A
        print('\nEXPAND')

        head_input = self.config.pop_input()
        print("head ", head_input[0])
        # if isinstance(head_input[0])
        non_terminal = head_input[0]
        prods = self.grammar.get_productions_for_nonterminals(non_terminal)
        print("prods", prods[0][0])

        first_production = []

        for i in prods[0]:
            first_production.append(i)

        first_production[0].extend(self.config.get_input())
        print(self.grammar.get_productions_for_nonterminals(non_terminal))
        self.config.input = first_production[0]
        self.config.push((non_terminal, first_production[1]))
        
        print("index", self.config.get_current_position())
        print("work ", self.config.get_stack())
        print("input", self.config.get_input())

    def advance(self) -> None:
        # WHEN: head of input stack is a terminal = current symbol from input
        # (q, i, 𝜶, ai𝜷) ⊢ (q, i+1, 𝜶ai, 𝜷)
        print('\nADVANCE')

        head_input = self.config.pop_input()
        print("head ", head_input)

        self.config.push(head_input)
        self.config.increment()

        print("prod", self.grammar.get_productions())
        print("index", self.config.get_current_position())
        print("work ", self.config.get_stack())
        print("input", self.config.get_input())

    def momentary_insuccess(self) -> None:
        # WHEN: head of input stack is a terminal ≠ current symbol from input
        # (q,i, 𝜶, ai𝜷) ⊢ (b,i, 𝜶, ai𝜷)
        print('\nMOMENTARY INSUCCESS')
        print(self.grammar.get_productions())

        self.config.current_state = 'back'

        print("index", self.config.get_current_position())
        print("work ", self.config.get_stack())
        print("input", self.config.get_input())

    def back(self) -> None:
        # WHEN: head of working stack is a terminal
        # (b,i, 𝜶a, 𝜷) ⊢ (b,i-1, 𝜶, a𝜷)
        print('\nBACK')

        head_work = self.config.pop()
        print("head ", head_work)

        self.config.push_input(head_work)
        print(self.grammar.get_productions())
        self.config.decrement()

        print("index", self.config.get_current_position())
        print("work ", self.config.get_stack())
        print("input", self.config.get_input())

    def success(self) -> None:
        # WHEN: index is at the end of the word and the input stack is empty
        # (q,n+1, 𝜶, 𝜀) ⊢ (f,n+1, 𝜶, 𝜀)
        print('\nSUCCESS')

        self.config.current_state = 'final'

        print("index", self.config.get_current_position())
        print("work ", self.config.get_stack())
        print("input", self.config.get_input())

    def another_try(self):
        # WHEN: head of working stack is a nonterminal
        # (b, i, 𝜶 Aj, 𝜸j 𝜷) ⊢ (q, i, 𝜶Aj+1, 𝜸j+1𝜷) , if ∃ A → 𝜸j+1
        #                      (e, i, 𝜶, 𝜷), if i=1, A =S, ERROR
        #                      (b, i, 𝜶, A 𝜷)
        print('\nANOTHER TRY')

        head_work = self.config.peek()
        prods = self.grammar.get_productions_for_nonterminals(head_work[0])
        print('prods:::', prods)

        if prods[-1][1] > head_work[1]:
            self.another_try1()
        elif self.config.get_current_position() == 1 and head_work[0] == self.grammar.start_symbol:
            self.another_try3()
        else:
            self.another_try2()

        print("index", self.config.get_current_position())
        print("work ", self.config.get_stack())
        print("input", self.config.get_input())

    def another_try1(self):
        # (b, i, 𝜶 Aj, 𝜸j 𝜷) ⊢ (q, i, 𝜶Aj+1, 𝜸j+1𝜷)
        print('\nANOTHER TRY 1')
        
        head_work = self.config.pop()
        prods = self.grammar.get_productions_for_nonterminals(head_work[0])

        # print("prods ", prods)
        # print([production for production in prods if production[1] == head_work[1]][0][0])

        l = len([production for production in prods if production[1] == head_work[1]][0][0])
        print(self.grammar.get_productions())
        print('lol')
        for i in range(l):
            self.config.pop_input()
        print(self.grammar.get_productions())
        
        new_prod = [production for production in prods if production[1] == head_work[1] + 1][0][0]
        new_prod.extend(self.config.get_input())
        self.config.input = new_prod

        self.config.current_state = 'normal'

    def another_try2(self):
        # (b, i, 𝜶 Aj, 𝜸j 𝜷) ⊢ (e, i, 𝜶, 𝜷)
        print('\nANOTHER TRY 2')

        head_work = self.config.pop()
        prods = self.grammar.get_productions_for_nonterminals(head_work[0])

        print("prods ", prods)

        l = 0
        for p in prods:
            if p[1] == head_work[1]:
                l = len(p[0])
                break
                
        for _ in range(l):
            self.config.pop_input()

        self.config.current_state = 'error'

    def another_try3(self):
        # (b, i, 𝜶 Aj, 𝜸j 𝜷) ⊢ (b, i, 𝜶, A 𝜷)
        print('\nANOTHER TRY 3')

        head_work = self.config.pop()
        prods = self.grammar.get_productions_for_nonterminals(head_work[0])

        print("head ", head_work)
        print("prods", prods)

        l = len([production for production in prods if production[1] == head_work[1]])

        self.config.push_input(head_work[0])

    def parse(self):
        while self.config.get_current_state() not in ['final', 'error']:
            if self.config.get_current_state() == 'normal':
                if self.config.get_current_position() > len(self.word) and len(self.config.get_input()) == 0:
                    self.success()
                elif self.config.peek_input() in self.grammar.get_nonterminals():
                    self.expand()
                elif self.config.peek_input() in self.grammar.get_terminals() and self.config.peek_input() == self.check_in_word(self.config.get_current_position() - 1):
                    print(self.config.peek_input(), self.check_in_word(self.config.get_current_position() - 1))
                    self.advance()
                else:
                    print(self.config.peek_input(), self.check_in_word(self.config.get_current_position() - 1))
                    self.momentary_insuccess() 
            else:
                if self.config.peek() in self.grammar.get_terminals():
                    self.back()
                else:
                    self.another_try()     

        if self.config.get_current_state == 'error':
            print('ERROR')
        else:
            print('GOOD')                

    def get_tree(self, production_string):
        if not production_string:
            return []
        result = [(production_string[0].split('|')[0], -1, -1)]
        i = 0
        j = 0
        while j < len(production_string) and i < len(result):
            top = result[i]
            if top[0] not in self.grammar.nonterminals:
                i += 1
                continue
            expand_with = None
            while j < len(production_string):
                if '|' not in production_string[j]:
                    j += 1
                    continue
                non_terminal, production_number = production_string[j].split('#')
                if non_terminal == top[0]:
                    expand_with = (non_terminal, production_number)
                    j += 1
                    break
                j += 1
            if j == len(production_string):
                break
            non_terminal, production_number = expand_with
            production_number = int(production_number)
            production = self.grammar.get_productions_for_nonterminals(non_terminal)[production_number][1].split()
            added = 1
            for symbol in production:
                result.insert(i + added, (symbol, i, i + 1 + added))
                added += 1
            result[i + added - 1] = (*result[i + added - 1][:-1], -1)
            i += 1
        return result

    def get_config(self):
        return self.config

    def check_in_word(self, index):
        if len(self.word) <= index:
            return None
        
        return self.word[index]

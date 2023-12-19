class Configuration:
    def __init__(self, starting_symbol) -> None:
        self.current_state = 'normal'
        self.current_position = 1
        self.stack = []
        self.input = [starting_symbol]

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        if len(self.stack) == 0:
            return None
        
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None
        
        return self.stack[-1]

    def push_input(self, elem):
        print('push', self.input)
        self.input.insert(0, elem)
        print('push', self.input)

    def pop_input(self):
        if len(self.input) == 0:
            return None
        
        return self.input.pop(0)
    
    def peek_input(self):
        if len(self.input) == 0:
            return None
         
        return self.input[0]

    def increment(self):
        self.current_position += 1

    def decrement(self):
        self.current_position -= 1

    def get_current_state(self):
        return self.current_state

    def set_current_state(self, new_state):
        self.current_state = new_state

    def get_current_position(self):
        return self.current_position

    def get_stack(self):
        return self.stack

    def get_input(self):
        return self.input
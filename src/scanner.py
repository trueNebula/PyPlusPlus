from tables.symbol_table import SymbolTable
from tables.pif import PIF
from finite_automata import FiniteAutomata
import re

class Scanner:
    def __init__(self) -> None:
        self.sym_table = SymbolTable()
        self.pif = PIF()
        self.operators, self.separators, self.keywords = self.get_tokens()
        self.errors = []
        self.identifier_fa = FiniteAutomata()
        self.int_fa = FiniteAutomata()

        self.identifier_fa.read('./examples/automatas/fa_id.in')
        self.int_fa.read('./examples/automatas/fa_int.in')
        

    def detect(self, token) -> None:
        if token in self.tokens:
            self.PIF.add(token, -1)
        else:
            if token in self.constants:
                p = self.sym_table.find(token)
                self.PIF.add("const", p)
            else:
                if self.is_identifier(token):
                    p = self.sym_table.find(token)
                    self.PIF.add("id", p)
                else: 
                    raise Exception("Lexical error")

    def error(self, token, line_no):
        self.errors.append("Lexical error at line " + str(line_no) + ": " + token)

    def scan(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        nrLine = 0

        for line in lines:
            nrLine +=1
            tokens = self.tokenize(line)

            for token in tokens:
                if token in self.keywords or token in self.operators or token in self.separators:
                    # operators, separators and keywords
                    self.pif.add(token, -1)
                else:
                    if self.identifier_fa.is_accepted(token):
                        # identifiers
                        index = self.sym_table.add(token)
                        self.pif.add("id", index)
                    elif  re.match("^\"[A-Za-z0-9\.\?\!, ]*\"$", token) is not None or token == "0" or self.int_fa.is_accepted(token):
                        # constants
                        index = self.sym_table.add(token)
                        self.pif.add("const", index)
                    else:
                        self.error(token, nrLine)

        if(len(self.errors) == 0):
            print("Lexically correct")
            self.output()
        else:
            print("Error")
            for err in self.errors:
                print(err)

    def get_tokens(self):
        operators = []
        separators = []
        keywords = []

        with open('../docs/token.in', 'r') as file:
            lines = file.readlines()

        spaces = 0
        for line in lines:
            line = line.replace("\n", "")
            if line == " ":
                spaces +=1
            else:
                if spaces == 0:
                    operators.append(line)
                if spaces == 1:
                    if line == "space":
                        line = "  "
                    elif line == "enter":
                            line = "\n"
                    separators.append(line)
                if spaces == 2:
                    keywords.append(line)
        return operators, separators, keywords

    def tokenize(self, line):
        # remove spaces and newlines
        line = line.replace('\n', '').strip()
        if line == '':
            return []

        # handle the strings and the operators
        line, strings = self.search_for_strings(line)
        line = self.search_for_operators(line)

        # split the line by the separators
        for separator in self.separators:
            line = line.replace(separator, " "+separator+" ")
        tokens = line.split(" ")
        tokens = [t for t in tokens if t != '']

        # replace back the string tokens
        for i in range(len(tokens)):
            if re.match("^\$[0-9]+\$$", tokens[i]) is not None:
                tokens[i] = strings[int(tokens[i][1:-1])]

        return tokens

    def search_for_operators(self, line):
        result = ""
        i = 0
        while i < len(line):
            # check for compound operators
            if i+1<len(line) and line[i]+line[i+1] in self.operators:
                result += " " + line[i]+line[i+1] + " "
                i +=1
            # check for simple operators
            elif line[i] in self.operators:
                result += " " + line[i] + " "
            else:
                result += line[i]
            i +=1
        return result

    def search_for_strings(self, line):
        # replace the strings ("...") with $id$, where id is the index in the list of strings
        strings = []
        line_without_strings = ""

        i = 0
        isString = False
        string = ""

        while i<len(line):

            # when encountering a '"', its either the beginning or end of a string
            if line[i] == '"':
                # we add the finished string to the list as $index$
                if isString:
                    string += '\"'
                    strings.append(string)
                    line_without_strings += " $" + str(len(strings)-1) + "$ "
                # otherwise we start a new string
                else:
                    string = '\"'
                isString = not isString

            else:
                if isString:
                    string += line[i]
                else:
                    line_without_strings += line[i]
            i +=1

        if isString:
            strings.append(string)
            line_without_strings += " $" + str(len(strings)-1) + "$ "

        return line_without_strings, strings

    def output(self):
        self.pif.export()
        self.sym_table.export()

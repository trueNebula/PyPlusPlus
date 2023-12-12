import sys
from structures.grammar import Grammar

if len(sys.argv) == 1:
    raise Exception("No filename found")

n = (sys.argv[1])

grammar = Grammar()
grammar.read("examples/grammars/" + n)
grammar.export()
nt = input("Enter Nonterminal: ")
print(grammar.get_productions_for_nonterminals(nt))

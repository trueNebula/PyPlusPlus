import sys
from scanner import Scanner

if len(sys.argv) == 1:
    raise Exception("No filename found")

n = (sys.argv[1])

scanner = Scanner()
scanner.scan("examples/" + n)
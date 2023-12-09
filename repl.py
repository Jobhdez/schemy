from parser import parser
from interp import interp

def repl(prompt='lambda> '):
    while True:
        tree = parser.parse(input(prompt))
        val = interp(tree, {})
        print(val)

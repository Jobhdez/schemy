from scheme_interp.parser import parser
from scheme_interp.interp import interp

def repl(prompt='lambda> '):
    while True:
        tree = parser.parse(input(prompt))
        val = interp(tree)
        print(val)

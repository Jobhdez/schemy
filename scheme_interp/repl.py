from scheme_interp.parser import parser
from scheme_interp.interp import interp

def repl(prompt='lambda> '):
    while True:
        tree = parser.parse(input(prompt))
        val = interp(tree)
        if val is not None:
            print(py_to_scheme(val))

def py_to_scheme(e):
    match e:
        case [*exps]:
            return '(' + ' '.join(map(py_to_scheme, exps)) + ')'
        case _:
            return str(e)

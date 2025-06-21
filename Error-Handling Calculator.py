import math
import operator
import difflib

class SmartCalculator:
    def __init__(self):
        self.binary_ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': self.safe_divide,
            '^': operator.pow,
            'pow': operator.pow
        }
        self.unary_funcs = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'asin': math.asin,
            'acos': math.acos,
            'atan': math.atan,
            'log': math.log,
            'log10': math.log10,
            'sqrt': math.sqrt,
            'exp': math.exp,
            'degrees': math.degrees,
            'radians': math.radians,
            'factorial': math.factorial,
            'ceil': math.ceil,
            'floor': math.floor,
            'abs': abs
        }

    def safe_divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError('Division by zero')
        return a / b

    def autocorrect(self, token, choices):
        match = difflib.get_close_matches(token, choices, n=1, cutoff=0.7)
        return match[0] if match else None

    def evaluate(self, expr):
        tokens = expr.strip().split()
        if len(tokens) == 2:
            func = self.autocorrect(tokens[0], self.unary_funcs.keys())
            if not func:
                raise ValueError(f'Unknown function: {tokens[0]}')
            try:
                val = float(tokens[1])
            except:
                raise ValueError(f'Invalid number: {tokens[1]}')
            return self.unary_funcs[func](val)
        elif len(tokens) == 3:
            try:
                a = float(tokens[0])
                b = float(tokens[2])
            except:
                raise ValueError('Invalid number')
            op = self.autocorrect(tokens[1], self.binary_ops.keys())
            if not op:
                raise ValueError(f'Unknown operator: {tokens[1]}')
            return self.binary_ops[op](a, b)
        else:
            raise SyntaxError('Invalid format')


if __name__ == '__main__':
    calc = SmartCalculator()
    try:
        expr = input('Enter expression (e.g. 3 + 4 or squrt 25): ')
        result = calc.evaluate(expr)
        print(f'Result: {result}')
    except Exception as e:
        print(f'Error: {e}')

import unittest
import io
import sys
from unittest.mock import patch
from ShimMTGinter import ShimMTGInterpreter

class TestShimMTGInterpreter(unittest.TestCase):
    def setUp(self):
        self.interpreter = ShimMTGInterpreter()
        # Очищаем пространство имен перед каждым тестом
        self.interpreter.namespace = {
            'print': print,
            'input': input,
            'int': int,
            'random': __import__('random'),
            'math': __import__('math'),
            'Library': True,
            'Graveyard': False
        }

    def capture_output(self, code):
        captured = io.StringIO()
        sys.stdout = captured
        self.interpreter.execute(code)
        sys.stdout = sys.__stdout__
        return captured.getvalue().strip()

    def test_variable_assignment(self):
        self.interpreter.execute("player x = 10")
        self.assertEqual(self.interpreter.namespace.get('x'), 10)

    def test_print_statement(self):
        output = self.capture_output('cast("Hello World")')
        self.assertEqual(output, "Hello World")

    def test_arithmetic_operations(self):
        test_cases = [
            ('player x = 5 redraw 3', 'x', 8),
            ('player y = 10 mill 4', 'y', 6),
            ('player z = 2 redrawx 8', 'z', 16),
            ('player w = 10 millx 2', 'w', 5),
            ('player v = 2 delirium 3', 'v', 8)
        ]
        for code, var, expected in test_cases:
            with self.subTest(code=code):
                self.interpreter.execute(code)
                self.assertEqual(self.interpreter.namespace.get(var), expected)

    def test_conditional_logic(self):
        code = """
player x = 10
wintheroll x crew 5:
    player result = "greater"
losetheroll:
    player result = "less"
"""
        self.interpreter.execute(code)
        self.assertEqual(self.interpreter.namespace.get('result'), "greater")

    def test_while_loop(self):
        code = """
player count = 0
whenever count saddle 3:
    player count = count redraw 1
"""
        self.interpreter.execute(code)
        self.assertEqual(self.interpreter.namespace.get('count'), 3)

    @patch('builtins.input', return_value='42')
    def test_input_handling(self, mock_input):
        self.interpreter.execute('player x = exile(draw())')
        self.assertEqual(self.interpreter.namespace.get('x'), 42)

    def test_random_library(self):
        self.interpreter.execute('player x = random.randint(1, 1)')
        self.assertEqual(self.interpreter.namespace.get('x'), 1)

    def test_math_library(self):
        self.interpreter.execute('player x = math.sqrt(4)')
        self.assertEqual(self.interpreter.namespace.get('x'), 2.0)

    def test_library_constant(self):
        self.interpreter.execute('player x = Library')
        self.assertTrue(self.interpreter.namespace.get('x'))

    def test_graveyard_constant(self):
        self.interpreter.execute('player x = Graveyard')
        self.assertFalse(self.interpreter.namespace.get('x'))

    def test_complex_program(self):
        code = """
player total = 0
player i = 0
whenever i saddle 5:
    player total = total redraw i
    player i = i redraw 1
"""
        self.interpreter.execute(code)
        self.assertEqual(self.interpreter.namespace.get('total'), 10)

    def test_function_definition(self):
        code = """
spell test_func():
    conjure 42
player x = test_func()
"""
        self.interpreter.execute(code)
        self.assertEqual(self.interpreter.namespace.get('x'), 42)

    def test_undefined_variable(self):
        with self.assertRaises(NameError):
            self.interpreter.execute('cast(undefined_var)')

    def test_syntax_error(self):
        with self.assertRaises(SyntaxError):
            self.interpreter.execute('player x = ')

    @patch('builtins.input', side_effect=['player x = 5', 'cast(x)', 'destroy'])
    def test_interactive_mode(self, mock_input):
        captured = io.StringIO()
        sys.stdout = captured
        self.interpreter.interactive_mode()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn('5', output)

if __name__ == "__main__":
    unittest.main()
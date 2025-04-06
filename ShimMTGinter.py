import sys
import random
import math
import datetime

class ShimMTGInterpreter:
    def __init__(self):
        self.libraries = {
            'random': random,
            'math': math,
            'datetime': datetime,
            'time': __import__('time'),
            'os': __import__('os'),
            'sys': sys
        }
        self.namespace = {
            'print': print,
            'input': input,
            'int': int,
            'str': str,
            'float': float,
            'bool': bool,
            'list': list,
            'dict': dict,
            'set': set,
            'tuple': tuple,
            'range': range,
            'len': len,
            'sum': sum,
            'min': min,
            'max': max,
            'abs': abs,
            'round': round,
            'Library': True,
            'Graveyard': False,
            'True': True,
            'False': False
        }
        for lib_name, lib in self.libraries.items():
            self.namespace[lib_name] = lib
    def translate_code(self, code):
        code = code.replace('Library', 'True')
        code = code.replace('Graveyard', 'False')
        replaces = [
            ('player ', ''),
            ('cast(', 'print('),
            ('draw(', 'input('),
            ('attack(', 'int('),
            ('block(', 'str('),
            (' redraw ', ' + '),
            (' mill ', ' - '),
            (' redrawx ', ' * '),
            (' millx ', ' / '),
            (' delirium ', ' ** '),
            (' keep ', ' == '),
            (' mulligan ', ' != '),
            (' saddle ', ' < '),
            (' crew ', ' > '),
            (' saddle_keep ', ' <= '),
            (' crew_keep ', ' >= '),
            ('wintheroll', 'if'),
            ('losetheroll', 'else'),
            ('rollagain', 'elif'),
            ('whenever', 'while'),
            ('surveil', 'for'),
            ('destroy', 'break'),
            ('blink', 'continue'),
            ('spell', 'def'),
            ('conjure', 'return')
        ]
        
        for old, new in replaces:
            code = code.replace(old, new)
        return code

    def execute(self, code):
        try:
            python_code = self.translate_code(code)
            exec(python_code, self.namespace)
        except Exception as e:
            if 'unittest' in sys.modules:  # Если запущены тесты
                raise  # Пробрасываем оригинальное исключение
            print(f"MTGExecutionError (ошибка выполнения): {e}")
    def interactive_mode(self):
        print("ShimMTG REPL (введите 'destroy' для выхода)")
        while True:
            try:
                line = input(">>> ").strip()
                if line == 'destroy':
                    break
                self.execute(line)
            except KeyboardInterrupt:
                print("\nЗавершение работы...")
                break
            except Exception as e:
                print(f"MTGReplError: {e}")

def main():
    interpreter = ShimMTGInterpreter()
    
    if len(sys.argv) == 1:
        interpreter.interactive_mode()
    elif len(sys.argv) == 2:
        try:
            with open(sys.argv[1], 'r') as f:
                interpreter.execute(f.read())
        except FileNotFoundError:
            print(f"MTGFileNotFoundError {sys.argv[1]} not found")
    else:
        print("Использование: python shimlang.py [файл.mtg]")

if __name__ == "__main__":
    main()
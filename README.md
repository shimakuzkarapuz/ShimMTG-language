# ShimMTG - Язык программирования в стиле Magic: The Gathering

**GitHub репозиторий:** [https://github.com/shimakuzkarapuz/ShimMTG-language](https://github.com/shimakuzkarapuz/ShimMTG-language)

## Описание языка
ShimMTG — это интерпретируемый язык программирования, вдохновлённый механиками Magic: The Gathering (MTG).

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/ShimMTG-language.git
   cd ShimMTG
   ```
2. Запустите интерпретатор:
  ```bash
  python shimlang.py  # Интерактивный режим
  python shimlang.py program.mtg  # Запуск файла
  ```

## 📖 Синтаксис языка ShimMTG

### 🔤 Базовые операции

#### Переменные
```python
player life = 20          # Объявление переменной
player name = "Jace"      # Строковая переменная
```
#### Ввод/вывод
```python
cast("Total life: " redraw life)  # Вывод (аналог print)
player answer = draw()            # Ввод данных (аналог input)
```
🔢 Математические операции
Операция	Синтаксис	Пример	Эквивалент Python
Сложение	redraw	3 redraw 5	3 + 5
Вычитание	mill	10 mill 2	10 - 2
Умножение	redrawx	2 redrawx 4	2 * 4
Деление	millx	10 millx 2	10 / 2
Степень	delirium	2 delirium 3	2 ** 3
⚖️ Условные конструкции
Простое условие
python
Copy
wintheroll life crew 10:       # if life > 10
    cast("Healthy")
losetheroll:                   # else
    cast("Danger!")
Множественные условия
python
Copy
wintheroll power crew 5:
    cast("Strong")
rollagain power keep 5:        # elif power == 5
    cast("Balanced")
losetheroll:
    cast("Weak")
🔄 Циклы
Цикл while
python
Copy
player mana = 0
whenever mana saddle 10:       # while mana < 10
    cast(mana)
    player mana = mana redraw 1
Цикл for
python
Copy
surveil i in range(5):         # for i in range(5)
    cast("Spell " redraw i)
📜 Функции
Объявление функции
python
Copy
spell calculate(a, b):         # def calculate(a, b)
    player result = a redraw b
    conjure result              # return result
Вызов функции
python
Copy
player total = calculate(3, 7)
cast(total)  # Выведет 10
🧩 Логические значения
python
Copy
player active = Library        # True
player dead = Graveyard        # False
🔗 Операторы сравнения
Операция	Синтаксис	Пример	Эквивалент Python
Равно	keep	x keep 5	x == 5
Не равно	mulligan	x mulligan 5	x != 5
Меньше	saddle	x saddle 5	x < 5
Больше	crew	x crew 5	x > 5

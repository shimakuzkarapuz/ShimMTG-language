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

## Синтаксис языка ShimMTG

### Базовые операции

#### Переменные

```python
player life = 20          # Объявление переменной
player name = "Jace"      # Строковая переменная
```
#### Ввод/вывод
```python
cast("Total life: " redraw block(life))  # Вывод cast() (аналог print()) + block() (аналог str())
player answer = draw()            # Ввод данных (аналог input)
```

#### Преобразования
```python
player planeswalker = "Nissa "
player loaylity = 7
player damage = "3"
cast(planeswalker redraw loaylity) # error
cast(planeswalker redraw block(loyality)) # Nissa 7
cast(loyality mill damage) #error
cast(loyality mill attack(damage)) # 4
```

#### Математические операции

| Операция   | Синтаксис | Пример        | Эквивалент Python |
|------------|-----------|---------------|-------------------|
| Сложение   | `redraw`  | `3 redraw 5`  | `3 + 5`           |
| Вычитание  | `mill`    | `10 mill 2`   | `10 - 2`          |
| Умножение  | `redrawx` | `2 redrawx 4` | `2 * 4`           |
| Деление    | `millx`   | `10 millx 2`  | `10 / 2`          |
| Степень    | `delirium`| `2 delirium 3`| `2 ** 3`          |


### Условные конструкции
#### Простое условие
```python
wintheroll life crew 10:       # if life > 10
    cast("Healthy")
losetheroll:                   # else
    cast("Danger!")
```
#### Множественные условия
```python
wintheroll power crew 5:
    cast("Strong")
rollagain power keep 5:        # elif power == 5
    cast("Balanced")
losetheroll:
    cast("Weak")
```
### Циклы
#### Цикл while
```python
player mana = 0
whenever mana saddle 10:       # while mana < 10
    cast(mana)
    player mana = mana redraw 1
```
#### Цикл for
##### Просто for
```python
surveil i in range(5):         # for i in range(5)
    cast("Spell " redraw block(i))
```
##### Destroy и Blink
```python
surveil mana in range(8):
    player howmany = attack(draw())
    wintheroll howmany perpetual 2 keep 0:
        blink #continue
    wintheroll howmany crew_keep 100:
        destroy #break
    cast(howmany)
```

### Функции
#### Объявление функции
```python
spell calculate(a, b):         # def calculate(a, b)
    player result = a redraw b
    conjure result             # return result
```
#### Вызов функции
```python
player total = calculate(3, 7)
cast(total)  # Выведет 10
```
### Логические значения
```python
player active = Library        # True
player dead = Graveyard        # False
```
#### Операторы сравнения
| Операция       | Синтаксис    | Пример          | Эквивалент Python |
|----------------|--------------|-----------------|-------------------|
| Равно          | `keep`       | `x keep 5`      | `x == 5`          |
| Не равно       | `mulligan`   | `x mulligan 5`  | `x != 5`          |
| Меньше         | `saddle`     | `x saddle 5`    | `x < 5`           |
| Больше         | `crew`       | `x crew 5`      | `x > 5`           |
| Меньше или равно | `saddle_keep` | `x saddle_keep 5` | `x <= 5`        |
| Больше или равно | `crew_keep`  | `x crew_keep 5`  | `x >= 5`        |

### Тест операторов сравнения через логические выражения
```python
player a = 5
player b = 3
cast(a saddle b, a crew b, a keep b, a mulligan b, a saddle_keep b, a crew_keep b) # F T F T F T
player c = 5
player d = 5
cast(c saddle d, c crew d, c keep d, c mulligan d, c saddle_keep d, c crew_keep d) # F F T F T T
player e = 5
player f = 7
cast(e saddle f, e crew f, e keep f, e mulligan f, e saddle_keep f, e crew_keep f) # T F F T T F
```

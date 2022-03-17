# SnakeBiteAlpha: Expert Circuit Python

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Modules](#modules)
- [Classes](#classes)
- [RGB LED](#rgb-led)
- [About Me](#about-me)

## Modules

### Modules Assignment

Goal: Create a module with a function inside. Then, in a separate file, import that module and successfully execute the function.

`hello.py`: A very small module:

```python
def world():
    print("Hello, World!")
```

This module is very simple. It `def`ines the `world` function that is used later. The `world` function prints `Hello, World!`.

`genesis.py`: A *s*imilarly *s*mall *s*cript:

```python
import hello

hello.world()
```

It imports the `hello` module from the above file `hello.py`. When a module is imported, its functions can be called via `module.function`. In this case, the `world` function is called via `hello.world`.

### Modules Code

| Filename                    | Description                              | Dependencies            |
| --------------------------- | ---------------------------------------- | ----------------------- |
| [`hello.py`](/hello.py)     | Contains `world` module for `genesis.py` | n/a                     |
| [`genesis.py`](/genesis.py) | Prints `Hello, World!` using `hello.py`  | [`hello.py`](/hello.py) |

### Modules Reflection

This assignment was simple, but an introduction to pure
Python. I think a takeaway is something I said above:

> When a module is imported, its functions can be called via `module.function`.

I didn't understand this before, especially in the context of importing libraries on the Metro Express board, but now I do. Looking ahead at the [Classes Assignment](#classes-assignment), I think this will be useful.

## Classes

### Classes Assignment

Goal: Create and modify objects from a class.

(In this case, just copying code from the example. But, still reviewing it to understand how it works.)

The explanation for the code is in the files. Look below for the files.

### Classes Code

| Filename                                      | Description                                                                           | Dependencies        |
| --------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------- |
| [`dog.py`](/dog.py)                           | Class with different functions                                                        | n/a                 |
| [`kennel.py`](/kennel.py)                     | Modified example code for formatting                                                  | [`dog.py`](/dog.py) |
| [`olddog-newtricks.py`](/olddog-newtricks.py) | Original example code from Karl Helmstetter [(helmstk1)](https://github.com/helmstk1) | [`dog.py`](/dog.py) |

### Classes Reflection

Classes are odd. They still don't entirely make sense *(Note from future Henry: this bites you in the butt. Learn classes!)*. They are important, my partner wrote one for the project we just did. They just aren't clicking with me. Thankfully, that's why classmates and teachers exist.

But, something I learned: f-strings. The [`olddog-newtricks.py`](/olddog-newtricks.py) file has the original tutorial code. When you run it, there's an ugly little problem on `ln 22` when it prints a list of Rex's attributes:

Code: `print(Rex.kind, ", ", Rex.breed, ", ", Rex.age, ", ", Rex.tricks)`

Output: `Canis familiaris , Golden , 8 , ['roll over']`

There's a space before every comma, with actual separating spaces having to be input. But, modify this print statement with f-strings, and we get a better result:

Code: `print(f"{Rex.kind}, {Rex.breed}, {Rex.age}, {Rex.tricks}")`

Output: `Canis familiaris, Golden, 8, ['roll over']`

Here's an article on f-strings I used:

[freeCodeCamp](https://www.freecodecamp.org/news/python-f-strings-tutorial-how-to-use-f-strings-for-string-formatting/) ([Offline .pdf copy](/Resources/f-Strings.pdf))

## RGB LED

### RGB Assignment

Goal: PLACEHOLDER

### RGB Code

| Filename | Description | Dependencies |
| -------- | ----------- | ------------ |
|          |             |              |

### RGB Reflection

PLACEHOLDER

## About Me

Hi! I'm Henry Heisig, an Engineering III student in the Charlottesville High School class of 2024. You can contact me at [hheisig51+github@charlottesvilleschools.org](mailto:hheisig51+github@charlottesvilleschools.org) or [henry+github@eheisig.com](mailto:henry+github@eheisig.com) with any comments, questions, or concerns.

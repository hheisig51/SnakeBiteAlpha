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

| Filename                    | Purpose                                  | Dependencies            |
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

Goal: PLACEHOLDER

### Classes Code

| Filename                  | Purpose     | Dependencies        |
| ------------------------- | ----------- | ------------------- |
| [`dog.py`](/dog.py)       | PLACEHOLDER | n/a                 |
| [`kennel.py`](/kennel.py) | PLACEHOLDER | [`dog.py`](/dog.py) |

### Classes Reflection

f-strings. PLACEHOLDER

## RGB LED

### RGB Assignment

Goal: PLACEHOLDER

### RGB Code

| Filename | Purpose | Dependencies |
| -------- | ------- | ------------ |
|          |         |              |

### RGB Reflection

PLACEHOLDER

## About Me

Hi! I'm Henry Heisig, an Engineering III student in the Charlottesville High School class of 2024. You can contact me at [hheisig51+github@charlottesvilleschools.org](mailto:hheisig51+github@charlottesvilleschools.org) or [henry+github@eheisig.com](mailto:henry+github@eheisig.com) with any comments, questions, or concerns.

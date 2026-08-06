# 🍵 Exploring Data Science with Hitesh Sir

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/MySQL-SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4EAE4E?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

**A complete, structured Data Science learning journey — from Python fundamentals to full EDA projects.**
*Python core via [Full Stack AI with Python (Udemy)](https://www.udemy.com/course/full-stack-ai-with-python/) | Data Science modules via official docs and YouTube* ☕

> 📖 This is the **English version** of the README. For the Hinglish version, see [README_Hinglish.md](./README_Hinglish.md).

</div>

---

## 📚 Table of Contents

1. [Repository Overview](#-repository-overview)
2. [Repository Structure](#-repository-structure)
3. [Python Learning](#-python-learning)
4. [SQL Learning](#-sql-learning)
5. [NumPy Learning](#-numpy-learning)
6. [Pandas Learning](#-pandas-learning)
7. [Matplotlib Learning](#-matplotlib-learning)
8. [Seaborn Learning](#-seaborn-learning)
9. [EDA Learning](#-eda-learning)
10. [Key Themes and Teaching Style](#-key-themes--teaching-style)
11. [Tech Stack and Requirements](#-tech-stack--requirements)
12. [How to Use This Repo](#-how-to-use-this-repo)
13. [Learning Path](#-learning-path)
14. [Roadmap — Coming Soon](#-roadmap--coming-soon)
15. [File Count Summary](#-file-count-summary)

---

## 🧭 Repository Overview

This repository is a **comprehensive, beginner-to-intermediate Data Science learning resource** built across two parallel learning tracks:

- 🎓 **Python core** — completed via Hitesh Sir's Udemy course: **[Full Stack AI with Python](https://www.udemy.com/course/full-stack-ai-with-python/)** (by Hitesh Choudhary & Piyush Garg)
- 📊 **Data Science stack** (NumPy, Pandas, Matplotlib, Seaborn, EDA) — learned through official documentation and YouTube tutorials

Every concept is taught using **Indian chai (tea) culture** as an analogy — variables like `sugar_amount`, classes like `MasalaChai`, datasets like `chai_sales.csv` — making even complex topics approachable and memorable.

The repo covers the **complete data science toolkit**:

| Topic          | Coverage                  | Files/Notebooks  |
|----------------|---------------------------|------------------|
| 🐍 Python       | Core to Advanced          | 40+ `.py` files  |
| 🗄️ SQL (MySQL)  | Basics to Mini Project    | 10 `.sql` files  |
| 🔢 NumPy        | Arrays to Linear Algebra  | 4 notebooks      |
| 🐼 Pandas       | DataFrames to TimeSeries  | 5 notebooks      |
| 📊 Matplotlib   | Plots to Visualization    | 4 notebooks      |
| 🎨 Seaborn      | Statistical Plots         | 2 notebooks      |
| 🔍 EDA          | Full Workflow + Project   | 8 notebooks      |

> **Total: 7 learning modules, 70+ code files, 1 real-world dataset** — and more coming soon! 🚀

---

## 🗂️ Repository Structure

```
📁 Exploring Data Science With Hitesh Sir/
│
├── 📁 Python Learning/
│   ├── 📁 01_basic introduction/          # First Python program
│   ├── 📁 02_datatypes/                   # 11 chapters on Python data types
│   ├── 📁 03_conditional/                 # 5 mini-projects using conditionals
│   ├── 📁 04_loops/                       # for/while loop examples
│   ├── 📁 05_functions/                   # 12 files on function concepts
│   ├── 📁 06_chai_business/                # Mini project using modules
│   ├── 📁 07_Generators_and_Decorators/   # 7 files on generators and decorators
│   ├── 📁 08_Object_Programming/          # 8 files on OOP concepts
│   └── 📁 09_File_Handling/               # 6 files on file I/O and exceptions
│
├── 📁 SQL Learning/                       # 10 SQL lecture files + IPL project
├── 📁 Numpy Learning/                     # 4 Jupyter notebooks
├── 📁 Pandas Learning/                    # 5 Jupyter notebooks
├── 📁 Matplotlib Learning/                # 4 Jupyter notebooks
├── 📁 Seaborn Learning/                   # 2 Jupyter notebooks
└── 📁 EDA Learning/                       # 8 notebooks + chai_sales.csv dataset
    ├── chai_sales.csv                     # Real dataset (650+ records)
    └── README.md                          # EDA-specific readme
```

---

## 🐍 Python Learning

### 01 - Basic Introduction

**File:** `01_basic introduction/test.py`

The very first program — a simple `print` statement. This is where the entire journey begins.

```python
print("Govind Jangid ")
```

---

### 02 - Data Types

**11 chapter files** (`chapter1.py` to `chapter11.py`) covering all of Python's core and advanced data types. Each chapter uses chai-themed examples to make concepts concrete.

| File | Topic | Key Concept |
|------|-------|-------------|
| `chapter1.py` | Immutable Objects (Numbers) | `id()`, variable reassignment, memory addresses |
| `chapter2.py` | Mutable Objects (Set) | `set()`, `.add()`, `.remove()`, same `id()` after mutation |
| `chapter3.py` | Booleans & Comparison | `True/False`, comparison operators, type checking |
| `chapter4.py` | Tuples | Immutable sequences, indexing, packing/unpacking |
| `chapter5.py` | None & Type Checking | `None`, `isinstance()`, `type()` |
| `chapter6.py` | Strings | Slicing syntax, `[::-1]`, UTF-8 `.encode()` / `.decode()` |
| `chapter7.py` | Comprehensions | List/set/dict comprehensions |
| `chapter8.py` | Lists & Operator Overloading | `append`, `insert`, `remove`, `pop`, `+` and `*` on lists, `bytearray` |
| `chapter9.py` | Tuples Deep Dive | Immutability, tuple methods |
| `chapter10.py` | Dictionaries | key-value pairs, `.get()`, `.keys()`, `.values()`, `.items()`, `.pop()` |
| `chapter11.py` | Advanced Types | `datetime`, `namedtuple` from `collections` |

**Highlight — chapter8.py:** Operator overloading on lists:

```python
water = ["water"]
milk  = ["milk"]
liquid_mix = water + milk  # ["water", "milk"] — + concatenates lists!

strong_brew = "black tea " * 3  # string repetition

raw_spice_data = bytearray(b"cinnamon")  # mutable binary data
```

**Highlight — chapter10.py:** Complete dictionary reference:

```python
chai_order = {"type": "masala chai", "size": "large", "sugar": 2}
chai_order["liquid"] = "milk"          # Add a new key
del chai_order["liquid"]               # Delete a key
chai_order.get("notes", "No notes")   # Safe access with a default value
```

---

### 03 - Conditionals

**5 mini-projects** using practical, input-driven programs:

| File | Scenario | Concept Used |
|------|----------|-------------|
| `mini_project_1.py` | Snack suggestion at a café | `if/else`, `.lower()`, `or` operator |
| `mini_project_2.py` | Chai size pricing | Nested `if/elif/else` |
| `mini_project_3.py` | Discount eligibility | Logical operators `and/or` |
| `mini_project_4.py` | Movie ticket pricing | Chained conditionals |
| `mini_project_5.py` | Railway seat features | Python 3.10+ `match-case` |

**Highlight — mini_project_5.py:** Python's `match/case` (equivalent to switch statements in other languages):

```python
match seat_type:
    case "sleeper": print("No AC, beds available")
    case "ac":      print("Air conditioned, comfy ride")
    case "luxury":  print("Premium seats with meals")
    case _:         print("Invalid seat type")
```

---

### 04 - Loops

**7 files** covering both `for` and `while` loops and their common patterns:

| File | Topic |
|------|-------|
| `01_basic_loop.py` | `for` loop with `range()` |
| `03_Batch_Chai_Preparation.py` | Looping for batch processing |
| `04_Looping_through_list_Orders_Name.py` | Iterating over a list |
| `05_Why_to_use_Enumerate.py` | `enumerate()` for index + value |
| `06_Zip_Can_Combine_Lists.py` | `zip()` to pair two lists |
| `07_Introducing_While_Loop_in_Python.py` | `while` loop with conditions |
| `2-Tea-Token-Dispenser.py` | Interactive token dispenser |

---

### 05 - Functions

**12 files** covering everything from basic definitions to advanced patterns:

| File | Topic | Key Concepts |
|------|-------|-------------|
| `01_duplication.py` | Why functions exist | Avoiding code duplication |
| `02_complex.py` | Managing complexity | Breaking problems into functions |
| `06_scopes.py` | Variable Scopes | Local vs. global scope |
| `07_nonlocal.py` | `nonlocal` keyword | Enclosing scope access |
| `09_input_params.py` | Parameter Types | `*args`, `**kwargs`, mutable default args |
| `11_types_of_functions.py` | Pure/Impure, Recursion, Lambda | `filter()`, `lambda`, recursive functions |
| `12_built_in.py` | Built-in Functions | `map()`, `filter()`, `sorted()`, `zip()` |

**Highlight — 09_input_params.py:** The mutable default argument bug:

```python
# Bug: the same list object is reused on every call
def chai_order(order=[]):
    order.append("Masala")

# Fix: use None and create a fresh list inside the function
def chai_order(order=None):
    if order is None:
        order = []
```

---

### 06 - Chai Business Project

A modular mini-project demonstrating Python's package architecture:

```
06_chai_business/
├── _main.py          # Entry point
├── recipes/
│   ├── ___init__.py  # Package initializer
│   └── _flavors.py   # Chai flavor definitions
└── utils/
    └── _discounts.py # Discount utility functions
```

Teaches **separation of concerns** — keeping business logic separate from utility code.

---

### 07 - Generators & Decorators

**7 files** on two of Python's most powerful advanced features.

**Generators** — produce values one at a time (memory-efficient):

```python
def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"

stall = serve_chai()
next(stall)  # "Cup 1: Masala Chai" — lazy evaluation
```

**Decorators** — add behaviour to a function without modifying it:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello from ChaiCode!")
```

**Authorization decorator** (real-world use case):

```python
def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied: Admins only")
            return None
        return func(user_role)
    return wrapper
```

---

### 08 - Object-Oriented Programming (OOP)

**8 files** — complete OOP curriculum:

| File | Topic | Concepts |
|------|-------|---------|
| `01_classes_objects.py` | Classes & Objects | Blueprint vs instance, `type()` |
| `03_self_and_init.py` | `__init__` & `self` | Constructor, instance variables |
| `04_inheritance_composition.py` | Inheritance & Composition | IS-A vs HAS-A |
| `05_super_and_base_class.py` | `super()` | Parent class methods |
| `06_multiple_inheritance.py` | Multiple Inheritance | MRO |
| `07_static_and_class_methods.py` | Static & Class Methods | Alternative constructors |
| `08_property_getter_setter.py` | Properties | `@property` pattern |

**IS-A vs HAS-A:**

```python
class MasalaChai(BaseChai):          # IS-A (Inheritance)
    def add_spices(self): pass

class ChaiShop:
    def __init__(self):
        self.chai = BaseChai("Regular")  # HAS-A (Composition)
```

---

### 09 - File Handling & Exceptions

**6 files** covering error handling and file I/O:

| File | Topic |
|------|-------|
| `01_common_errors.py` | `NameError`, `TypeError`, `ValueError`, `IndexError` |
| `02_try_except.py` | try/except blocks |
| `04_custom_exceptions.py` | Custom exception classes |
| `05_mini_project.py` | Chai billing with full error handling |
| `06_file_handling_with.py` | `with` statement for file I/O |

**The `with` statement:**

```python
# Modern approach — file is closed automatically
with open("order.txt", "w") as file:
    file.write("Ginger tea - 7 cups")
```

---

## 🗄️ SQL Learning

**10 SQL lecture files** covering MySQL from basics to a complete project:

| File | Topics Covered |
|------|---------------|
| `01_SQL_Basics.sql` | DDL/DML/DQL/DCL/TCL, `CREATE`, `INSERT`, `SELECT` |
| `04_SELECT_WHERE_Operators.sql` | `WHERE`, `BETWEEN`, `IN`, `LIKE`, `IS NULL` |
| `05_Aggregate_Functions_Subqueries.sql` | `AVG`, `MAX`, `MIN`, `COUNT`, `SUM`, subqueries |
| `07_Joins.sql` | `INNER`, `LEFT`, `RIGHT`, `CROSS`, `SELF` JOIN |
| `09_Views_Stored_Procedures.sql` | `CREATE VIEW`, `CREATE PROCEDURE` |
| `10_IPL_Mini_Project.sql` | Complete relational DB design + analytics |

### 🏏 IPL Mini Project

A fully normalized IPL database:

```
TEAMS              → TEAM_ID (PK), TEAM_NAME, CITY, OWNER
PLAYERS            → PLAYER_ID (PK), NAME, ROLE, AGE, COUNTRY, TEAM_ID (FK)
MATCHES            → MATCH_ID (PK), TEAM1_ID, TEAM2_ID, DATE, VENUE, WINNER_TEAM_ID (FK)
PLAYER_PERFORMANCE → PERF_ID (PK), MATCH_ID, PLAYER_ID, RUNS, BALLS, WICKETS, CATCHES
```

Teams: `MI` · `CSK` · `RCB` · `KKR` · `RR`

---

## 🔢 NumPy Learning

**Learning Source:** [Official NumPy Docs](https://numpy.org/doc/) + [NumPy Full Course on YouTube](https://www.youtube.com/watch?v=x7ULDYs4X84)

**4 Jupyter Notebooks:**

| Notebook | Topics |
|----------|--------|
| `01_NumPy_Fundamentals.ipynb` | Arrays, `dtype`, `shape`, `arange`, `zeros`, `linspace` |
| `02_Indexing_Slicing_Reshaping.ipynb` | Indexing, slicing, `reshape`, `flatten` |
| `03_Operations_Broadcasting_Statistics.ipynb` | Broadcasting, `mean`, `std`, `sum` |
| `04_Joining_Random_LinearAlgebra_Practice.ipynb` | `concatenate`, random, dot product |

---

## 🐼 Pandas Learning

**Learning Source:** [Official Pandas Docs](https://pandas.pydata.org/docs/) + YouTube tutorials

**5 Jupyter Notebooks:**

| Notebook | Topics |
|----------|--------|
| `01_Pandas_Fundamentals.ipynb` | `Series`, `DataFrame`, `info()`, `describe()` |
| `02_Selection_Filtering_Cleaning.ipynb` | `loc`, `iloc`, `isnull()`, `fillna()`, `dropna()` |
| `03_Data_Manipulation_GroupBy.ipynb` | `apply()`, `map()`, `groupby()`, aggregation |
| `04_Merge_Reshape_TimeSeries.ipynb` | `merge()`, `pivot_table()`, `melt()`, datetime |
| `05_File_IO_Advanced_Practice.ipynb` | `read_csv()`, `read_excel()`, `read_json()` |

---

## 📊 Matplotlib Learning

**Learning Source:** [Official Matplotlib Docs](https://matplotlib.org/stable/index.html) + YouTube tutorials

**4 Jupyter Notebooks** covering line plots, bar charts, scatter plots, histograms, pie charts, heatmaps, and subplots.

---

## 🎨 Seaborn Learning

**Learning Source:** [Official Seaborn Docs](https://seaborn.pydata.org/) + YouTube tutorials

**2 Jupyter Notebooks** covering `histplot`, `boxplot`, `scatterplot`, `heatmap`, `pairplot`, `violinplot`, `FacetGrid`, and palette customisation.

---

## 🔍 EDA Learning

**Learning Source:** Official documentation + YouTube videos + self-directed practice

**8 Jupyter Notebooks** + `chai_sales.csv` (650+ records).

The dataset intentionally contains missing values, duplicates, inconsistent formatting, and outliers to simulate real data cleaning.

### EDA Workflow

```
Raw Data → Understanding → Cleaning → Univariate → Bivariate
        → Multivariate → Feature Engineering → Preprocessing → Full Project
```

---

## 🎯 Key Themes & Teaching Style

### 🎓 Course Source

| Module | Source |
|--------|--------|
| Python Learning | [Full Stack AI with Python — Udemy](https://www.udemy.com/course/full-stack-ai-with-python/) by Hitesh Choudhary & Piyush Garg |
| SQL Learning | Supplementary practice (Hitesh Sir style) |
| NumPy Learning | [NumPy Docs](https://numpy.org/doc/) + [YouTube](https://www.youtube.com/watch?v=x7ULDYs4X84) |
| Pandas Learning | [Pandas Docs](https://pandas.pydata.org/docs/) + YouTube tutorials |
| Matplotlib Learning | [Matplotlib Docs](https://matplotlib.org/stable/index.html) + YouTube tutorials |
| Seaborn Learning | [Seaborn Docs](https://seaborn.pydata.org/) + YouTube tutorials |
| EDA Learning | Official docs + YouTube + self-directed practice |

---

## 🛠️ Tech Stack & Requirements

```bash
pip install numpy pandas matplotlib seaborn jupyter notebook
```

- Python 3.10+, MySQL 8.0+, Jupyter Notebook, VS Code

---

## 🚀 How to Use This Repo

```bash
git clone https://github.com/GovindJangid75/Exploring-Data-Science.git
pip install numpy pandas matplotlib seaborn jupyter notebook
jupyter notebook   # open any notebook
```

For SQL: run files in order 01 → 10 in MySQL.

---

## 🗺️ Learning Path

```
Week 1-2:  Python Fundamentals  ✅
Week 3-4:  Python Advanced      ✅
Week 5:    SQL                  ✅
Week 6:    NumPy + Pandas       ✅
Week 7:    Matplotlib + Seaborn ✅
Week 8:    EDA Capstone         ✅
Week 9-10: More EDA Projects    🕓
Week 11-12: Machine Learning    🕓
Week 13-14: Deep Learning       🕓
Week 15+:  GenAI & LLMs         🕓
```

---

## 🚀 Roadmap — Coming Soon

- [ ] **More EDA Projects** — real-world datasets (e-commerce, health, finance)
- [ ] **Machine Learning** — Scikit-learn, Regression, Trees, SVM, KNN, Clustering, PCA
- [ ] **Deep Learning** — TensorFlow, PyTorch, CNNs, RNNs, LSTMs
- [ ] **Generative AI & LLMs** — OpenAI/Gemini API, RAG, LangChain, LangGraph, MCP
- [ ] **MLOps** — Docker, FastAPI, model versioning

> 💡 *Star this repository to stay updated when new modules are added!*

---

## 📁 File Count Summary

| Module | Status | Files | Type |
|--------|--------|-------|------|
| Python Learning | ✅ Complete | 40+ | `.py` |
| SQL Learning | ✅ Complete | 10 | `.sql` |
| NumPy Learning | ✅ Complete | 4 | `.ipynb` |
| Pandas Learning | ✅ Complete | 5 | `.ipynb` |
| Matplotlib Learning | ✅ Complete | 4 | `.ipynb` |
| Seaborn Learning | ✅ Complete | 2 | `.ipynb` |
| EDA Learning | ✅ Complete | 8 + 1 dataset | `.ipynb` + `.csv` |
| Machine Learning | 🔜 Coming Soon | — | — |
| Deep Learning | 🔜 Coming Soon | — | — |
| Generative AI / LLMs | 🔜 Coming Soon | — | — |
| **Current Total** | — | **74+ files** | — |

---

## 👨‍💻 Author

**Govind Jangid**
Student — Python via [Full Stack AI with Python (Udemy)](https://www.udemy.com/course/full-stack-ai-with-python/) | Data Science self-directed practice

> *"This repository is my living Data Science journey — from writing my first `print()` to full EDA projects, and soon ML, DL, and Generative AI. Every commit is a step forward."*

---

## 🙏 Acknowledgements

- **Hitesh Choudhary & Piyush Garg** — [Full Stack AI with Python (Udemy)](https://www.udemy.com/course/full-stack-ai-with-python/)
- **NumPy, Pandas, Matplotlib, Seaborn teams** — for excellent official documentation
- **YouTube creators** — for supplementary tutorials
- **ChaiCode Community** — for the peer learning environment

---

<div align="center">

Made with ☕ chai, 🐍 Python, and a lot of ❤️ by Govind Jangid

*"Good code needs chai!"*

</div>

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
*Python core learned via Hitesh Sir's Udemy course — [Full Stack AI with Python](https://www.udemy.com/course/full-stack-ai-with-python/) | Data Science modules as supplementary practice* ☕

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
10. [Key Themes & Teaching Style](#-key-themes--teaching-style)
11. [Tech Stack & Requirements](#-tech-stack--requirements)
12. [How to Use This Repo](#-how-to-use-this-repo)
13. [Learning Path](#-learning-path)
14. [🚀 Roadmap — Coming Soon](#-roadmap--coming-soon)
15. [File Count Summary](#-file-count-summary)

---

## 🧭 Repository Overview

Ye repository ek **beginner-to-intermediate Data Science learning resource** hai jo maine do tracks me build ki hai:

- 🎓 **Python core** — Hitesh Sir ke Udemy course se seekha: **[Full Stack AI with Python](https://www.udemy.com/course/full-stack-ai-with-python/)** (by Hitesh Choudhary & Piyush Garg)
- 📊 **Data Science stack** (NumPy, Pandas, Matplotlib, Seaborn, EDA) — ek supplementary practice ke roop mein

Har concept ko **Indian chai culture** ke through samjhaya gaya hai — jaise `sugar_amount`, `chai_type`, `MasalaChai` — taaki boring topics bhi interesting lage!

Is repo mein ye sab cover hota hai:

| Topic             | Coverage              | Files/Notebooks |
|-------------------|-----------------------|-----------------|
| 🐍 Python          | Core to Advanced      | 40+ `.py` files |
| 🗄️ SQL (MySQL)     | Basics to Mini Project| 10 `.sql` files |
| 🔢 NumPy           | Arrays to Linear Algebra | 4 notebooks |
| 🐼 Pandas          | DataFrames to TimeSeries | 5 notebooks |
| 📊 Matplotlib      | Plots to Visualization | 4 notebooks   |
| 🎨 Seaborn         | Statistical Plots      | 2 notebooks    |
| 🔍 EDA             | Full Workflow + Project | 8 notebooks   |

> **Total: 7 learning modules, 70+ code files, 1 real-world dataset** — aur aage aur bhi aayega! 🚀

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
│   ├── 📁 06_chai_buisnes/                # Mini project using modules
│   ├── 📁 07_Generators_and_Decorators/   # 7 files on generators & decorators
│   ├── 📁 08_Object_Programming/          # 8 files on OOP concepts
│   └── 📁 09_File_Handling/               # 6 files on file I/O and exceptions
│
├── 📁 SQL Learning/                       # 10 SQL lecture files + IPL project
│
├── 📁 Numpy Learning/                     # 4 Jupyter notebooks
│
├── 📁 Pandas Learning/                    # 5 Jupyter notebooks
│
├── 📁 Matplotlib Learning/                # 4 Jupyter notebooks
│
├── 📁 Seaborn Learning/                   # 2 Jupyter notebooks
│
└── 📁 EDA Learning/                       # 8 notebooks + chai_sales.csv dataset
    ├── chai_sales.csv                     # Real dataset (650+ records)
    └── README.md                          # EDA-specific readme
```

---

## 🐍 Python Learning

### 01 - Basic Introduction

**File:** `01_basic introduction/test.py`

Sabse pehla program — sirf ek `print` statement. Yahi se journey shuru hoti hai bhai!

```python
print("Govind Jangid ")
```

Chhota sa program hai, but iska matlab bada hai — Python ka pehla kadam!

---

### 02 - Data Types

**11 chapter files** (`chapter1.py` → `chapter11.py`) — Python ke saare core aur advanced data types cover hote hain. Har chapter mein chai ke examples use kiye gaye hain taaki concept clearly samajh aaye.

| File | Topic | Key Concept |
|------|-------|-------------|
| `chapter1.py` | Immutable Objects (Numbers) | `id()`, variable reassignment, memory addresses |
| `chapter2.py` | Mutable Objects (Set) | `set()`, `.add()`, `.remove()`, same `id()` after mutation |
| `chapter3.py` | Booleans & Comparison | `True/False`, comparison operators, type checking |
| `chapter4.py` | Tuples | Immutable sequences, indexing, packing/unpacking |
| `chapter5.py` | None & Type Checking | `None`, `isinstance()`, `type()` |
| `chapter6.py` | Strings (Indexing, Slicing, Encoding) | Slicing syntax, `[::-1]`, UTF-8 `.encode()` / `.decode()` |
| `chapter7.py` | Comprehensions | List/set/dict comprehensions |
| `chapter8.py` | Lists & Operator Overloading | `append`, `insert`, `remove`, `pop`, `+` and `*` on lists, `bytearray` |
| `chapter9.py` | Tuples Deep Dive | Immutability, tuple methods |
| `chapter10.py` | Dictionaries | key-value pairs, `.get()`, `.keys()`, `.values()`, `.items()`, `.pop()` |
| `chapter11.py` | Advanced Types (collections) | `datetime`, `namedtuple` from `collections` |

**Highlight — chapter8.py:** Ek hi file mein list operations AUR operator overloading dono cover kiya gaya hai:

```python
# Operator Overloading - + on lists
water = ["water"]
milk  = ["milk"]
liquid_mix = water + milk  # ["water", "milk"] — plus ne dono lists jod diye!

# String multiplication — string ko repeat karna
strong_brew = "black tea " * 3

# Bytearray — binary data ke liye mutable sequence
raw_spice_data = bytearray(b"cinnamon")
```

**Highlight — chapter10.py:** Dictionary ke saare important operations ek jagah:

```python
chai_order = {"type": "masala chai", "size": "large", "sugar": 2}
chai_order["liquid"] = "milk"          # Add key
del chai_order["liquid"]               # Delete key
chai_order.get("notes", "No notes")   # Safe access with default
```

---

### 03 - Conditionals

**5 mini-projects** (`mini_project_1.py` se `mini_project_5.py` tak) — sab practical, input-driven programs hain. Sirf theory nahi, seedha real-world scenarios!

| File | Scenario | Concept Used |
|------|----------|-------------|
| `mini_project_1.py` | Snack suggestion at a local café | `if/else`, `.lower()`, `or` operator |
| `mini_project_2.py` | Chai size pricing | Nested `if/elif/else` |
| `mini_project_3.py` | Discount eligibility checker | Logical operators `and/or` |
| `mini_project_4.py` | Age-based movie ticket pricing | Chained conditionals |
| `mini_project_5.py` | Railway seat feature lookup | Python `match-case` (switch-statement equivalent) |

**Highlight — mini_project_5.py** — Python 3.10+ ka `match/case` use kiya gaya hai (C/Java wala switch-case jaisa, but better!):

```python
match seat_type:
    case "sleeper": print("No AC, beds available")
    case "ac":      print("Air conditioned, comfy ride")
    case "luxury":  print("Premium seats with meals")
    case _:         print("Invalid seat type")  # default case
```

---

### 04 - Loops

**7 files** — Python ke dono main loops (`for` aur `while`) aur unke saare useful patterns cover kiye gaye hain.

| File | Topic |
|------|-------|
| `01_basic_loop.py` | `for` loop with `range()` |
| `03_Batch_Chai_Preparation.py` | Looping to simulate batch processing |
| `04_Looping_through_list_Orders_Name.py` | Iterating over a list |
| `05_Why_to_use_Enumerate.py` | `enumerate()` for index + value |
| `06_Zip_Can_Combine_Lists.py` | `zip()` to pair two lists together |
| `07_Introducing_While_Loop_in_Python.py` | `while` loop with break conditions |
| `2-Tea-Token-Dispenser.py` | Interactive token dispenser simulation |

---

### 05 - Functions

**12 files** — ye sabse detailed section hai. Simple function definition se lekar `*args`, `**kwargs`, recursion, lambda, aur pure vs impure functions tak sab kuch cover kiya gaya hai!

| File | Topic | Key Concepts |
|------|-------|-------------|
| `01_duplication.py` | Why functions exist | Avoiding code duplication |
| `02_complex.py` | Managing complexity | Breaking big problems into small functions |
| `03_hiding.py` | Information hiding | Abstraction through functions |
| `04_readability.py` | Readability | Self-documenting function names |
| `05_trace.py` | Tracing function calls | Call stack understanding |
| `06_scopes.py` | Variable Scopes | Local vs. global scope |
| `07_nonlocal.py` | `nonlocal` keyword | Accessing enclosing scope variables |
| `08_global_scope.py` | `global` keyword | When & why to avoid global |
| `09_input_params.py` | Parameter Types | `*args`, `**kwargs`, mutable default args |
| `10_return.py` | Return values | Multiple returns, tuple unpacking |
| `11_types_of_functions.py` | Pure vs Impure, Recursion, Lambda | `filter()`, `lambda`, recursive functions |
| `12_built_in.py` | Built-in Functions | `map()`, `filter()`, `sorted()`, `zip()` |

**Highlight — 09_input_params.py:** Python ka ek famous gotcha — mutable default argument bug! Bahut log isme phaste hain:

```python
# Bug: mutable default argument persists across calls
def chai_order(order=[]):
    order.append("Masala")   # same list baar baar reuse hoti hai!

# Fix: None use karo aur andar fresh list banao
def chai_order(order=None):
    if order is None:
        order = []  # har call pe nayi list
```

`*args` aur `**kwargs` bhi dikhaye gaye hain:

```python
def special_chai(*ingredients, **extras):
    print("Ingredients:", ingredients)  # tuple
    print("Extras:", extras)            # dict
```

**Highlight — 11_types_of_functions.py:** Recursion + lambda + filter — teen important concepts ek file mein:

```python
def pour_chai(n):
    print(n)
    if n == 0: return "All cups poured"
    return pour_chai(n - 1)   # function apne aap ko call karta hai!

strong_chai = list(filter(lambda c: c != "kadak", chai_types))  # kadak hata do
```

---

### 06 - Chai Business Project

**Location:** `06_chai_buisnes/`

Ek **chhota sa modular project** hai jo Python ka module/package architecture demonstrate karta hai — bilkul waise jaise real-world Python projects hote hain.

```
06_chai_buisnes/
├── _main.py          # Entry point — yahan se program shuru hota hai
├── recipes/
│   ├── ___init__.py  # Package initializer
│   └── _flavors.py   # Chai flavor definitions
└── utils/
    └── _discounts.py # Discount utility functions
```

Ye project ek important concept sikhata hai — **separation of concerns** — matlab business logic (recipes) aur utilities (discounts) alag-alag rakhna. Real projects mein yahi hota hai!

---

### 07 - Generators & Decorators

**7 files** — Python ke do bahut powerful aur thoda advanced features. Ek baar samajh gaye toh alag hi level pe code likhne lagte ho!

#### Generators (Files 01-04)

Generator kya hota hai? Ek aisa function jo ek time mein ek value deta hai, saari ek saath nahi — isliye memory efficient hota hai:

```python
def serve_chai():
    yield "Cup 1: Masala Chai"   # ruk jao, pehle ye do
    yield "Cup 2: Ginger Chai"   # phir ye do
    yield "Cup 3: Elaichi Chai"  # phir ye do

stall = serve_chai()
next(stall)  # "Cup 1: Masala Chai" — lazy evaluation!
```

Generators **memory-efficient** hote hain — ye values ek-ek karke produce karte hain, poori list memory mein nahi rakhte.

#### Decorators (Files 05-07)

Decorator kya hota hai? Ek aisa function jo doosre function ko wrap karta hai aur bina original code change kiye extra functionality add karta hai!

| File | Topic |
|------|-------|
| `05_decorators_basics.py` | Basic decorator with `@wraps` |
| `06_logger_deco.py` | Logging decorator for function calls |
| `07_auth_deco.py` | Authorization/role-check decorator |

**Basic decorator pattern — kaise kaam karta hai:**

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)          # preserves original function metadata
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello from decorators class from ChaiCode")
```

**Authorization decorator — real-world use case** — jaise admin panel mein sirf admin access kar sake:

```python
def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied: Admins only")
            return None
        return func(user_role)
    return wrapper

@require_admin
def access_tea_inventory(role):
    print("Access granted to tea inventory")
```

---

### 08 - Object-Oriented Programming (OOP)

**8 files** — OOP ka poora curriculum! Class banane se lekar inheritance, composition, static methods, aur property decorator tak — sab systematically cover kiya gaya hai.

| File | Topic | Concepts |
|------|-------|---------|
| `01_classes_objects.py` | Classes & Objects | Blueprint vs instance, `type()` |
| `02_class_object_namespace.py` | Namespaces | Class vs instance namespace |
| `03_self_and_init.py` | `__init__` & `self` | Constructor, instance variables |
| `04_inheritance_composition.py` | Inheritance & Composition | IS-A vs HAS-A relationship |
| `05_super_and_base_class.py` | `super()` | Calling parent class methods |
| `06_multiple_inheritance.py` | Multiple Inheritance | MRO (Method Resolution Order) |
| `07_static_and_class_methods.py` | Static & Class Methods | `@staticmethod`, `@classmethod`, alternative constructors |
| `08_property_getter_setter.py` | Properties | `@property`, getter/setter pattern |

**Highlight — 04_inheritance_composition.py:** IS-A vs HAS-A relationship — OOP ka ek important concept:

```python
class BaseChai:
    def __init__(self, type_): self.type = type_
    def prepare(self): print(f"Preparing {self.type} chai...")

class MasalaChai(BaseChai):          # IS-A — MasalaChai EK BaseChai hai (Inheritance)
    def add_spices(self): print("Adding cardamom, ginger and cloves.")

class ChaiShop:
    def __init__(self):
        self.chai = BaseChai("Regular")   # HAS-A — ChaiShop KE PAAS chai hai (Composition)
```

**Highlight — 07_static_and_class_methods.py:**

```python
class ChaiOrder:
    @classmethod
    def from_dict(cls, data):    # Alternative constructor from dictionary
        return cls(data["tea_type"], data["sweetness"], data["size"])

    @classmethod
    def from_string(cls, s):     # Alternative constructor from string
        return cls(*s.split("-"))

# Instance Method  → receives self   (instance-specific)
# Class Method     → receives cls    (class-specific, alternative constructors)
# Static Method    → receives nothing (utility function)
```

---

### 09 - File Handling & Exceptions

**6 files** — errors handle karna aur files ke saath kaam karna. Real applications mein ye bahut zaroori hota hai!

| File | Topic | Concepts |
|------|-------|---------|
| `01_common_errors.py` | Common Python errors | `NameError`, `TypeError`, `ValueError`, `IndexError` |
| `02_try_except.py` | try/except blocks | Exception catching and handling |
| `03_raise_exception.py` | Raising exceptions | `raise`, custom messages |
| `04_custom_exceptions.py` | Custom exception classes | Inheriting from `Exception` |
| `05_mini_project.py` | Chai billing with errors | Complete exception handling mini-project |
| `06_file_handling_with.py` | File I/O with context manager | `open()`, `with` statement, read/write |

**Highlight — 05_mini_project.py:** Chai billing system jo properly errors handle karta hai — custom exception bhi banaya gaya:

```python
class InvalidChaiError(Exception):
    pass

def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("Bhai menu me likha hai, ye chai nahi milti")  # apna error raise karo
        if not isinstance(cups, int):
            raise TypeError("Cups number me bata bhai!")
        total = menu[flavor] * cups
        print(f"{cups} cups of {flavor} chai = Rs.{total}")
    except InvalidChaiError as e: print("Chai Error:", e)
    except TypeError as e:        print("Type Error:", e)
    except Exception as e:        print("Unexpected Error:", e)
    finally:                      print("Thank you for visiting ChaiCode!")  # ye hamesha chalega
```

**Highlight — 06_file_handling_with.py:** `with` statement kyun use karte hain — manual vs smart tarika:

```python
# Purana tarika (manually file band karni padti thi — agar error aaya toh file open reh jaati!)
file = open("order.txt", "w")
try:
    file.write("Masala chai - 2 cups")
finally:
    file.close()

# Naya aur better tarika — with statement automatically file band kar deta hai
with open("order.txt", "w") as file:
    file.write("Ginger tea - 7 cups")
```

---

## 🗄️ SQL Learning

**10 structured SQL lecture files** — MySQL ke basics se shuru hokar ek complete real-world mini-project tak sab cover hota hai. Seedha CSE database banane se IPL analytics tak!

| File | Lecture | Topics Covered |
|------|---------|---------------|
| `01_SQL_Basics.sql` | SQL Fundamentals | DDL/DML/DQL/DCL/TCL overview, `CREATE DATABASE`, `CREATE TABLE`, `INSERT`, `SELECT` |
| `02_DDL_DataTypes_Alter.sql` | DDL & Data Types | `ALTER TABLE`, `ADD COLUMN`, `MODIFY`, `DROP COLUMN`, MySQL data types |
| `03_DataTypes_Constraints_DML.sql` | Constraints & DML | `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `DEFAULT`, `CHECK`, `INSERT`, `UPDATE`, `DELETE` |
| `04_SELECT_WHERE_Operators.sql` | Querying Data | `WHERE`, `BETWEEN`, `IN`, `LIKE`, `IS NULL`, `AND`, `OR`, `NOT` |
| `05_Aggregate_Functions_Subqueries.sql` | Aggregates & Subqueries | `AVG`, `MAX`, `MIN`, `COUNT`, `SUM`, nested `SELECT`, `INSERT INTO SELECT` |
| `06_OrderBy_Limit_GroupBy_Having.sql` | Sorting & Grouping | `ORDER BY`, `LIMIT`, `GROUP BY`, `HAVING` |
| `07_Joins.sql` | SQL JOINs | `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL OUTER JOIN` (UNION), `CROSS JOIN`, `SELF JOIN` |
| `08_DCL_TCL_Keys.sql` | Permissions & Transactions | `GRANT`, `REVOKE`, `COMMIT`, `ROLLBACK`, `SAVEPOINT`, `FOREIGN KEY` |
| `09_Views_Stored_Procedures.sql` | Views & Procedures | `CREATE VIEW`, `CREATE PROCEDURE`, `DELIMITER`, `CALL` |
| `10_IPL_Mini_Project.sql` | **IPL Mini Project** | Complete relational database design & analytics |

---

### 🏑 IPL Mini Project (`10_IPL_Mini_Project.sql`)

SQL ka **capstone project** — IPL (Indian Premier League) ka ek fully normalized relational database design kiya gaya hai. 4 tables, real players, aur analytics queries!

#### Database Schema

```
TEAMS              → TEAM_ID (PK), TEAM_NAME, CITY, OWNER
PLAYERS            → PLAYER_ID (PK), NAME, ROLE, AGE, COUNTRY, TEAM_ID (FK)
MATCHES            → MATCH_ID (PK), TEAM1_ID (FK), TEAM2_ID (FK), DATE, VENUE, WINNER_TEAM_ID (FK)
PLAYER_PERFORMANCE → PERF_ID (PK), MATCH_ID (FK), PLAYER_ID (FK), RUNS, BALLS, WICKETS, CATCHES
```

#### Teams Included
`MI (Mumbai)` · `CSK (Chennai)` · `RCB (Bengaluru)` · `KKR (Kolkata)` · `RR (Jaipur)`

#### Sample Players
Rohit Sharma, Jasprit Bumrah, MS Dhoni, Ravindra Jadeja, Virat Kohli, Glenn Maxwell, Andre Russell, Jos Buttler, Sunil Narine, Ravichandran Ashwin

#### Analytics Queries

```sql
-- Orange Cap (sabse zyada runs)
SELECT P.PLAYER_NAME, SUM(PP.RUNS) AS TOTAL_RUNS
FROM PLAYER_PERFORMANCE PP JOIN PLAYERS P ON PP.PLAYER_ID = P.PLAYER_ID
GROUP BY P.PLAYER_ID ORDER BY TOTAL_RUNS DESC LIMIT 1;

-- Purple Cap (sabse zyada wickets)
SELECT P.PLAYER_NAME, SUM(PP.WICKETS) AS TOTAL_WICKETS
FROM PLAYER_PERFORMANCE PP JOIN PLAYERS P ON PP.PLAYER_ID = P.PLAYER_ID
GROUP BY P.PLAYER_ID ORDER BY TOTAL_WICKETS DESC LIMIT 1;

-- Points Table (wins per team)
SELECT T.TEAM_NAME, COUNT(M.MATCH_ID) AS WINS
FROM MATCHES M JOIN TEAMS T ON M.WINNER_TEAM_ID = T.TEAM_ID
GROUP BY T.TEAM_ID ORDER BY WINS DESC;

-- Match details aur saare team ke naam (multi-join)
SELECT M.MATCH_ID, T1.TEAM_NAME AS TEAM1, T2.TEAM_NAME AS TEAM2, TW.TEAM_NAME AS WINNER
FROM MATCHES M
JOIN TEAMS T1 ON M.TEAM1_ID  = T1.TEAM_ID
JOIN TEAMS T2 ON M.TEAM2_ID  = T2.TEAM_ID
JOIN TEAMS TW ON M.WINNER_TEAM_ID = TW.TEAM_ID;
```

---

### SQL Joins ka Summary — Yaad rakho:

```
INNER JOIN  → Sirf matching rows milti hain dono tables se
LEFT JOIN   → Left table ki saari rows + right se matching
RIGHT JOIN  → Right table ki saari rows + left se matching
FULL OUTER  → MySQL me directly nahi hota, LEFT + RIGHT UNION karo
CROSS JOIN  → Har row ka har row se combination (Cartesian product)
SELF JOIN   → Table apne aap se join (e.g., Employee → Manager)
```

---

## 🔢 NumPy Learning

**4 Jupyter Notebooks** — NumPy kya hota hai? Ye Python ka ek powerful library hai numbers ke saath fast kaam karne ke liye. Lists se kaafi better performance milti hai!

| Notebook | Topics |
|----------|--------|
| `01_NumPy_Fundamentals.ipynb` | Arrays, `dtype`, `shape`, `ndim`, `arange`, `zeros`, `ones`, `linspace` |
| `02_Indexing_Slicing_Reshaping.ipynb` | Integer indexing, boolean indexing, slicing, `reshape`, `flatten`, `ravel` |
| `03_Operations_Broadcasting_Statistics.ipynb` | Element-wise ops, broadcasting rules, `mean`, `std`, `min`, `max`, `sum` |
| `04_Joining_Random_LinearAlgebra_Practice.ipynb` | `concatenate`, `stack`, `random`, `seed`, dot product, matrix operations |

### NumPy ke Important Concepts:

- **Array create karna:** `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()`
- **Indexing & Slicing:** Multi-dimensional slicing `arr[1:3, 0:2]`, fancy indexing, boolean masks
- **Broadcasting:** Alag-alag shape ke arrays pe loop chalaye bina operations karna
- **Statistics:** `np.mean()`, `np.std()`, `np.median()`, `np.percentile()`
- **Linear Algebra:** Dot products, matrix multiplication
- **Random Module:** `np.random.rand()`, `np.random.seed()`, `np.random.choice()`

---

## 🐼 Pandas Learning

**5 Jupyter Notebooks** — Data Science ka dil! Pandas ke bina data analysis possible hi nahi. DataFrame aur Series ke through sab kuch milta hai.

| Notebook | Topics |
|----------|--------|
| `01_Pandas_Fundamentals.ipynb` | `Series`, `DataFrame`, creation, basic attributes (`shape`, `dtypes`, `info()`, `describe()`) |
| `02_Selection_Filtering_Cleaning.ipynb` | `loc`, `iloc`, boolean filtering, `isnull()`, `fillna()`, `dropna()`, `drop_duplicates()` |
| `03_Data_Manipulation_GroupBy.ipynb` | `apply()`, `map()`, `groupby()`, aggregation, custom functions |
| `04_Merge_Reshape_TimeSeries.ipynb` | `merge()`, `concat()`, `pivot_table()`, `melt()`, datetime indexing |
| `05_File_IO_Advanced_Practice.ipynb` | `read_csv()`, `to_csv()`, `read_excel()`, `read_json()`, advanced practice |

### Pandas ke Important Operations:

```python
# Data select karna
df.loc[rows, cols]                       # label-based selection — naam se
df.iloc[rows, cols]                      # position-based selection — number se

# Data clean karna
df.isnull().sum()                        # kitni missing values hain column mein?
df.fillna(value)                         # missing values fill karo
df.dropna()                              # NaN wali rows hata do
df.drop_duplicates()                     # duplicate rows hata do

# Grouping & Aggregation
df.groupby("City")["Sales"].mean()

# Merging
pd.merge(df1, df2, on="key", how="left")

# Reshaping
df.pivot_table(values="Sales", index="City", columns="Category", aggfunc="sum")
```

---

## 📊 Matplotlib Learning

**4 Jupyter Notebooks** — from simple line plots to advanced multi-panel visualizations.

| Notebook | Topics |
|----------|--------|
| `01_Matplotlib_Basics_Line_Plots.ipynb` | `plt.plot()`, `xlabel`, `ylabel`, `title`, `legend`, `figsize`, styles |
| `02_Bar_Scatter_Histogram_Pie.ipynb` | `plt.bar()`, `plt.scatter()`, `plt.hist()`, `plt.pie()` |
| `03_Customization_Subplots.ipynb` | `plt.subplot()`, `fig, ax = plt.subplots()`, colors, markers, linestyles |
| `04_Advanced_Visualization_Practice.ipynb` | Heatmaps, complex multi-plot layouts, real-data visualization |

### Chart Types Covered

| Chart Type | Use Case |
|------------|----------|
| Line Plot | Trends over time |
| Bar Chart | Categorical comparison |
| Scatter Plot | Correlation/relationship |
| Histogram | Distribution of values |
| Pie Chart | Proportional breakdown |
| Heatmap | Matrix / correlation visualization |
| Subplots | Multiple charts in one figure |

---

## 🎨 Seaborn Learning

**2 Jupyter Notebooks** — statistical visualization with beautiful defaults.

| Notebook | Topics |
|----------|--------|
| `01_Seaborn_Basics_Core_Plots.ipynb` | `sns.histplot()`, `sns.boxplot()`, `sns.scatterplot()`, `sns.heatmap()`, `sns.pairplot()` |
| `02_Seaborn_Advanced_Practice.ipynb` | `sns.violinplot()`, `sns.barplot()`, `sns.countplot()`, `FacetGrid`, themes, palettes |

### Seaborn vs Matplotlib

| Feature | Matplotlib | Seaborn |
|---------|-----------|---------|
| Complexity | Lower-level, more control | Higher-level, less code |
| Aesthetics | Manual styling needed | Beautiful defaults |
| Statistical plots | Manual | Built-in (`boxplot`, `violinplot`) |
| Pandas integration | Manual | Native DataFrame support |

---

## 🔍 EDA Learning

**8 Jupyter Notebooks** + ek real-world dataset — ye poore repo ka sabse complete section hai! Yahan pe sab kuch combine hota hai.

### Dataset: `chai_sales.csv`

Ek fictional but realistic **Chai Shop sales dataset** hai jisme **650+ records** hain. Aur sabse mast baat — isme intentionally kuch missing values, duplicates, aur inconsistent data hai taaki data cleaning ka real practice mile!

| Feature Category | Columns |
|-----------------|---------|
| Time | `date`, `day`, `order_hour` |
| Location | `city` (8 Indian cities) |
| Product | `chai_variety` (8 types), `size` |
| Sales | `quantity`, `price`, `discount`, `total_amount` |
| Customer | `payment_method`, `customer_type`, `repeat_customer` |
| Order Type | `dine_in`, `takeaway`, `delivery` |
| Environment | `weather`, `temperature` |
| Quality | `rating`, `preparation_time`, `sugar_pref`, `milk_pref` |

> Dataset mein **intentionally** missing values, duplicate rows, inconsistent text casing, aur outliers hain — yahi toh real data cleaning practice ke liye chahiye!

### EDA Notebooks

| Notebook | Topic | Key Techniques |
|----------|-------|---------------|
| `01_EDA_Intro.ipynb` | Introduction to EDA | What is EDA, why it matters, overview |
| `02_Data_Cleaning.ipynb` | Data Cleaning | Handling nulls, duplicates, inconsistent categories, outliers |
| `03_Univariate_Analysis.ipynb` | Univariate Analysis | Histograms, box plots, value counts, describe() for each variable |
| `04_Bivariate_Analysis.ipynb` | Bivariate Analysis | Scatter plots, correlation, grouped bar charts, cross-tabulations |
| `05_Multivariate_Analysis.ipynb` | Multivariate Analysis | Pair plots, heatmaps, correlation matrix, multi-variable groupby |
| `06_Feature_Engineering.ipynb` | Feature Engineering | Creating new features from existing ones (hour buckets, weekday flags) |
| `07_Preprocessing.ipynb` | Preprocessing | Encoding, scaling, train-test split preparation |
| `08_Complete_EDA_Project.ipynb` | **Full EDA Project** | End-to-end analysis combining all steps above |

### EDA Workflow

```
Raw Data (chai_sales.csv)
        |
Step 1: Data Understanding  →  shape, dtypes, head(), describe()
        |
Step 2: Data Cleaning       →  missing values, duplicates, outliers
        |
Step 3: Univariate Analysis →  distribution of each individual variable
        |
Step 4: Bivariate Analysis  →  relationships between two variables
        |
Step 5: Multivariate        →  interactions among multiple variables
        |
Step 6: Feature Engineering →  create better features from raw data
        |
Step 7: Preprocessing       →  prepare data for ML models
        |
Step 8: Full Project        →  complete documented end-to-end analysis
```

---

## 🎯 Key Themes & Teaching Style

### 🎓 Course Source

| Module | Source |
|--------|--------|
| Python Learning (all 9 sub-topics) | [Full Stack AI with Python — Udemy](https://www.udemy.com/course/full-stack-ai-with-python/) by Hitesh Choudhary & Piyush Garg |
| SQL Learning | Supplementary practice (Hitesh Sir style) |
| NumPy Learning | Official [NumPy Docs](https://numpy.org/doc/) + YouTube — [NumPy Full Course](https://www.youtube.com/watch?v=x7ULDYs4X84) |
| Pandas Learning | Official [Pandas Docs](https://pandas.pydata.org/docs/) + YouTube tutorials |
| Matplotlib Learning | Official [Matplotlib Docs](https://matplotlib.org/stable/index.html) + YouTube tutorials |
| Seaborn Learning | Official [Seaborn Docs](https://seaborn.pydata.org/) + YouTube tutorials |
| EDA Learning | Official documentation + YouTube videos + self practice |

### 🍵 The Chai Metaphor

Every concept — from Python variables to SQL queries — is explained through **Indian chai culture** — a signature teaching style of Hitesh Sir:

- Variables → `sugar_amount`, `chai_type`, `ginger`
- Classes → `class Chai`, `class ChaiShop`, `class MasalaChai`
- SQL data → IPL cricket teams and players
- Datasets → `chai_sales.csv`

This makes abstract programming concepts relatable and memorable for Indian learners.

### 🇮🇳 Hinglish Comments

All Python files are commented in **Hinglish** (Hindi + English) — a hallmark of Hitesh Sir's Udemy course:

```python
# Ye list ek mutable sequence hai, matlab aap iske andar changes kar sakte ho
# ingredients.append("sugar") — List me item add karna
# ingredients.remove("water") — Kisi item ko list se remove karna
```

### 📈 Progressive Complexity

The module ordering follows a deliberate progression:

```
[Udemy Course]
Basic Print → Data Types → Conditionals → Loops → Functions
    → Modules → Generators/Decorators → OOP → File Handling

[Supplementary Practice]
    → SQL → NumPy → Pandas → Matplotlib → Seaborn → Full EDA
```

---

## 🛠️ Tech Stack & Requirements

### Languages & Tools

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.10+ | Core programming (match/case requires 3.10+) |
| MySQL | 8.0+ | SQL exercises and mini projects |
| Jupyter Notebook | Latest | Interactive notebooks |
| VS Code | Latest | Code editor |

### Python Libraries

```bash
pip install numpy pandas matplotlib seaborn jupyter notebook
```

| Library | Used For |
|---------|---------|
| `numpy` | Array operations, linear algebra |
| `pandas` | DataFrame manipulation |
| `matplotlib` | Core plotting |
| `seaborn` | Statistical visualization |
| `jupyter` | Running `.ipynb` notebooks |

### Standard Library (no install needed)

- `functools` — `wraps` for decorators
- `collections` — `namedtuple`
- `datetime` — date/time operations

---

## 🚀 How to Use This Repo

### 1. Clone the Repository

```bash
git clone https://github.com/GovindJangid75/Exploring-Data-Science.git
cd "Exploring Data Science With Hitesh Sir"
```

### 2. Install Python Dependencies

```bash
pip install numpy pandas matplotlib seaborn jupyter notebook
```

### 3. Run Python Files

```bash
# Navigate to any Python Learning subfolder
cd "Python Learning/05_functions"
python 11_types_of_functions.py
```

### 4. Open Jupyter Notebooks

```bash
# From repo root
jupyter notebook
# OR
jupyter lab
```

Navigate to any module folder (e.g., `EDA Learning/`) and open notebooks in order.

### 5. Run SQL Files

Open your MySQL client (MySQL Workbench / DBeaver / MySQL CLI) and run files in order:

```bash
mysql -u root -p < "SQL Learning/01_SQL_Basics.sql"
```

> **Important:** Run SQL files in order (01 to 10), as later files depend on databases created in earlier ones.

---

## 🗺️ Learning Path

If you are starting fresh, follow this recommended 8-week order:

```
Week 1-2: Python Fundamentals
  ✅ 01_basic introduction
  ✅ 02_datatypes (chapters 1-11)
  ✅ 03_conditional (mini projects)
  ✅ 04_loops

Week 3-4: Python Advanced
  ✅ 05_functions (all 12 files)
  ✅ 06_chai_buisnes (module project)
  ✅ 07_Generators_and_Decorators
  ✅ 08_Object_Programming (OOP)
  ✅ 09_File_Handling

Week 5: SQL
  ✅ SQL Learning (01 to 10 in order)
  ✅ Complete IPL Mini Project

Week 6: Data Science Libraries
  ✅ NumPy Learning (01 to 04)
  ✅ Pandas Learning (01 to 05)

Week 7: Visualization
  ✅ Matplotlib Learning (01 to 04)
  ✅ Seaborn Learning (01 to 02)

Week 8: EDA Capstone
  ✅ EDA Learning (01 to 08)
  ✅ Complete EDA Project with chai_sales.csv

──────────────────────────── UPCOMING ────────────────────────────

Week 9-10: More EDA Projects
  🕓 Real-world EDA projects on different domains
  🕓 Feature engineering deep-dive

Week 11-12: Machine Learning
  🕓 Scikit-learn basics
  🕓 Supervised Learning (Linear/Logistic Regression, Decision Trees, Random Forest, SVM)
  🕓 Unsupervised Learning (K-Means, PCA)
  🕓 Model Evaluation & Cross-Validation
  🕓 ML Projects

Week 13-14: Deep Learning
  🕓 Neural Networks fundamentals
  🕓 TensorFlow / PyTorch basics
  🕓 CNNs (Computer Vision)
  🕓 RNNs / LSTMs (Sequence data)
  🕓 DL Projects

Week 15+: Generative AI & LLMs (Udemy Course Extension)
  🕓 LLM fundamentals (from Full Stack AI with Python course)
  🕓 OpenAI & Gemini API integration
  🕓 Prompt Engineering patterns
  🕓 RAG pipelines with LangChain
  🕓 Agentic AI with LangGraph
  🕓 MCP (Model Context Protocol)
```

---

## 🚀 Roadmap — Coming Soon

This repo is **actively growing**. Here's what's planned for future additions:

### 📊 More EDA Projects
- [ ] Real-world EDA on diverse datasets (e-commerce, health, finance)
- [ ] Advanced feature engineering notebooks
- [ ] EDA report automation

### 🤖 Machine Learning
- [ ] **Supervised Learning** — Linear Regression, Logistic Regression, Decision Trees, Random Forest, SVM, KNN
- [ ] **Unsupervised Learning** — K-Means Clustering, PCA, DBSCAN
- [ ] **Model Evaluation** — Confusion Matrix, ROC-AUC, Cross-Validation, Hyperparameter Tuning
- [ ] **ML Projects** — end-to-end projects with real datasets

### 🧠 Deep Learning
- [ ] **Neural Network fundamentals** — perceptrons, backpropagation, activation functions
- [ ] **TensorFlow / Keras** — model building, training, evaluation
- [ ] **PyTorch basics** — tensors, autograd, custom models
- [ ] **CNNs** — image classification projects
- [ ] **RNNs / LSTMs** — sequence prediction, time-series
- [ ] **DL Projects** — real-world applications

### 🌟 Generative AI & LLMs *(from the Udemy course)*
- [ ] LLM architecture — tokenization, embeddings, attention, transformers
- [ ] OpenAI API & Gemini API integration
- [ ] Prompt Engineering — zero-shot, few-shot, chain-of-thought
- [ ] **RAG** — Retrieval-Augmented Generation with LangChain + vector databases
- [ ] **Agentic AI** — stateful agents with LangGraph
- [ ] **MCP** — Model Context Protocol
- [ ] Local deployment with Ollama & Hugging Face

### ⚙️ MLOps & Deployment
- [ ] Docker for ML model deployment
- [ ] API creation with FastAPI / Flask
- [ ] Model versioning and experiment tracking

> 💡 *Star this repo to stay updated when new modules are added!*

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
| EDA Learning | ✅ Complete | 8 notebooks + 1 dataset | `.ipynb` + `.csv` |
| More EDA Projects | 🔜 Coming Soon | — | — |
| Machine Learning | 🔜 Coming Soon | — | — |
| Deep Learning | 🔜 Coming Soon | — | — |
| Generative AI / LLMs | 🔜 Coming Soon | — | — |
| **Current Total** | — | **74+ files** | — |

---

## 👨‍💻 Author

**Govind Jangid**
Student — Python via [Full Stack AI with Python (Udemy)](https://www.udemy.com/course/full-stack-ai-with-python/) | Data Science self-practice

> *"This repository is my living Data Science journey — from writing my first `print()` to building full EDA projects, and soon ML, DL, and Generative AI. Every commit is a step forward."*

---

## 🙏 Acknowledgements

- **Hitesh Choudhary** & **Piyush Garg** — for the structured, practical, Hinglish-friendly Python teaching on [Full Stack AI with Python (Udemy)](https://www.udemy.com/course/full-stack-ai-with-python/)
- **ChaiCode Community** — for the supplementary resources and peer learning environment

---

<div align="center">

Made with ☕ chai, 🐍 Python, and a lot of ❤️ by Govind Jangid

*"Acha code likhne ke liye chai zaroori hai"* — Good code needs chai!

</div>

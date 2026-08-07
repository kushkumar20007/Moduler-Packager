# 🚀 Multi-Utility Toolkit (Moduler & Packager)

## Objective

* **Explore Built-in Modules:** Utilize `datetime`, `time`, `math`, `random`, and `uuid` modules for practical tasks.
* **Custom Modules and Packages:**

  * Create modular Python scripts for specific functionalities.
  * Organize them into packages with an `__init__.py` file to demonstrate package usage.
* **Script Organization:** Implement `__name__` and `__main__` to separate reusable components and main execution logic.
* **Dynamic Exploration:** Use the `dir()` function to explore module attributes dynamically.

---

## 🌟 Key Highlights

* 📅 **Date & Time utilities**
* ⏱️ **Stopwatch and countdown timer**
* ➕ **Advanced mathematical calculations**
* 🎲 **Random number, OTP, and password generator**
* 🆔 **UUID-based unique identifier generator**
* 📂 **Custom file handling module**
* 🔍 **Dynamic module exploration using `dir()`**
* 🧩 **Package-based project organization**
* 🖥️ **Menu-driven command line interface**

---

# 🏗️ Project Layout

```text
multi_utility_toolkit/
│
├── main.py
├── README.md
│
├── utilities/
│   ├── __init__.py
│   ├── datetime_tools.py
│   ├── math_tools.py
│   ├── random_tools.py
│   ├── uuid_tools.py
│   └── explorer.py
│
├── custom_modules/
│   ├── __init__.py
│   ├── file_manager.py
│   └── converter.py
│
└── outputs/
    ├── logs.txt
    └── generated_ids.txt
```

---

# ⚙️ Features

## 📅 Datetime Utilities

| Operation       | Description                      |
| --------------- | -------------------------------- |
| Current Date    | Display today's date             |
| Current Time    | Show live system time            |
| Date Difference | Calculate days between two dates |
| Custom Format   | Format using `strftime()`        |

### Example

```python
from utilities.datetime_tools import show_current_datetime

show_current_datetime()
```

---

## ⏱️ Stopwatch & Countdown

### Stopwatch

```python
start_stopwatch()
```

### Countdown

```python
countdown(10)
```

---

## ➗ Mathematical Toolkit

Supported operations:

* Arithmetic operations
* Square root
* Power calculations
* Factorial
* Trigonometric functions
* Logarithmic calculations
* Compound Interest
* Area of geometric shapes

### Example

```python
from utilities.math_tools import compound_interest

result = compound_interest(10000, 5, 2)
print(result)
```

---

## 🎲 Random Utilities

### Generate Random Number

```python
generate_random_number(1, 100)
```

### Generate OTP

```python
generate_otp(6)
```

### Generate Password

```python
generate_password(12)
```

---

## 🆔 UUID Generator

Generate unique identifiers for:

* User sessions
* Invoice numbers
* File references
* Record IDs

### Example

```python
from utilities.uuid_tools import create_uuid

print(create_uuid())
```

---

# 📂 Custom Modules

## File Manager

Functions included:

* Create file
* Read file
* Append data
* Update file
* Save logs automatically

### Example

```python
from custom_modules.file_manager import write_log

write_log("Toolkit started successfully")
```

---

## Unit Converter

Supports conversions such as:

* Kilometer ↔ Meter
* Celsius ↔ Fahrenheit
* Gram ↔ Kilogram
* Inch ↔ Centimeter

---

# 🔍 Dynamic Module Explorer

The toolkit can inspect available attributes of any module.

### Example

```python
import math
print(dir(math))
```

Custom module exploration:

```python
from utilities import math_tools
print(dir(math_tools))
```

---

# 🖥️ Running the Project

## Step 1: Open Terminal

Navigate to the project folder.

```bash
cd multi_utility_toolkit
```

## Step 2: Run Main Program

```bash
python main.py
```

---

# 📋 Sample Menu

```text
========== MULTI-UTILITY TOOLKIT ==========

1. Date & Time Utilities
2. Stopwatch / Countdown
3. Mathematical Operations
4. Random Generator
5. UUID Generator
6. File Operations
7. Unit Converter
8. Explore Module Attributes
9. Exit

==========================================
```

---

# 🧠 Use of `__name__ == "__main__"`

Each module can work independently.

```python
def demo():
    print("Math module demo")

if __name__ == "__main__":
    demo()
```

This ensures that **demo code runs only when the file is executed directly**, not when it is imported.

---
## 🎥🎞️ Video Demonstration

[![Watch Video](https://img.shields.io/badge/🎥-Watch_Video-red?style=for-the-badge)](video)


# 📊 Output

<img width="932" height="901" alt="image" src="https://github.com/user-attachments/assets/218414ca-e1d4-43bf-bc77-1b86e30f9ac7" />
<img width="954" height="884" alt="image" src="https://github.com/user-attachments/assets/3d8df1b5-012d-4ea2-911c-b07e482002e8" />
<img width="982" height="918" alt="image" src="https://github.com/user-attachments/assets/a86e4358-e11f-41ff-b4b1-a2d2b38d1573" />
<img width="1268" height="868" alt="image" src="https://github.com/user-attachments/assets/d6c4a5f3-9615-457a-92fb-df3787b01e47" />





---

# 🎯 Learning Objectives Achieved

| Concept                     | Implemented |
| --------------------------- | ----------- |
| Built-in Modules            | ✅           |
| Custom Modules              | ✅           |
| Packages                    | ✅           |
| `__init__.py`               | ✅           |
| `__name__` & `__main__`     | ✅           |
| Dynamic Exploration (`dir`) | ✅           |
| Menu-driven UI              | ✅           |
| File Handling               | ✅           |

---

# 🧪 Suggested Test Cases

* Generate 100 random passwords
* Create multiple UUIDs and verify uniqueness
* Compare two dates from different years
* Save generated reports into `outputs/logs.txt`
* Explore attributes of both built-in and custom modules

---

# 💡 Real-World Scenario

A **small business owner** can use this toolkit to:

* Track working hours
* Generate secure passwords for employees
* Create invoice IDs
* Save activity logs
* Perform financial calculations
* Explore available module capabilities dynamically

---

# 🔮 Future Improvements

* GUI using **Tkinter**
* Database support (**SQLite**)
* Export reports to **CSV / PDF**
* User authentication system
* Configuration file support
* REST API integration

---

# 🛠️ Technologies Used

| Technology | Purpose                       |
| ---------- | ----------------------------- |
| Python 3   | Core programming              |
| datetime   | Date & time handling          |
| time       | Stopwatch and delays          |
| math       | Mathematical functions        |
| random     | Random generation             |
| uuid       | Unique identifier creation    |
| os         | File and directory management |

---

# 👨‍💻 Author

**Kush Kumar**
Python Mini Project — **Moduler & Packager 

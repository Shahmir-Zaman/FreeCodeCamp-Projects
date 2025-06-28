# FreeCodeCamp Projects

A collection of Python projects completed as part of the FreeCodeCamp Scientific Computing with Python certification. These projects demonstrate fundamental programming concepts including object-oriented programming, string manipulation, mathematical calculations, and data formatting.

## Table of Contents

- [Projects Overview](#projects-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Project Details](#project-details)
  - [Arithmetic Formatter](#arithmetic-formatter)
  - [Time Calculator](#time-calculator)
  - [Budget App](#budget-app)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Projects Overview

This repository contains four Python projects that showcase different programming skills:

- **Arithmetic Formatter**: Formats arithmetic problems vertically for easy reading
- **Time Calculator**: Adds duration to a given time and handles day calculations
- **Budget App**: Object-oriented budget management system with spending charts

## Installation

### Prerequisites
- Python 3.6 or higher

### Setup
1. Clone this repository:
```bash
git clone https://github.com/yourusername/FreeCodeCamp-Projects.git
cd FreeCodeCamp-Projects
```

2. No additional dependencies required - all projects use Python standard library only.

## Usage

Each project can be run independently:

```bash
# Run Arithmetic Formatter
python "Arithmetic Formatter.py"

# Run Time Calculator  
python "Time Calculator.py"

# Run Budget App
python "Budget App.py"
```

## Project Details

### Arithmetic Formatter

**File**: `Arithmetic Formatter.py`, `Arithmetic-Formatter-Custom-Just-Logic.py`

Arranges arithmetic problems vertically for better visualization.

**Features**:
- Formats addition and subtraction problems
- Right-aligns numbers properly
- Optional answer display
- Error handling for invalid inputs

**Example**:
```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

**Output**:
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

**Error Handling**:
- Maximum 5 problems per call
- Only addition (+) and subtraction (-) operators
- Numbers must be digits only
- Numbers cannot exceed 4 digits

### Time Calculator

**File**: `Time Calculator.py`

Adds a duration to a start time and calculates the resulting time with day tracking.

**Features**:
- 12-hour format support (AM/PM)
- Day of week calculations
- Multi-day duration handling
- Automatic day counting

**Example**:
```python
add_time('11:43 PM', '24:20', 'Tuesday')
# Returns: "12:03 AM, Thursday (2 days later)"
```

**Capabilities**:
- Handles time overflow (24+ hours)
- Optional starting day parameter
- Displays days passed for multi-day durations
- Case-insensitive day input

### Budget App

**File**: `Budget App.py`

Object-oriented budget management system with category tracking and spending visualization.

**Features**:
- Category-based budget tracking
- Transaction ledger management
- Fund transfers between categories
- Spending chart generation

**Example**:
```python
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
```

**Output**:
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
Transfer to Clothing    -50.00
Total: 939.85
```

**Category Methods**:
- `deposit(amount, description)`: Add funds to category
- `withdraw(amount, description)`: Remove funds (if available)
- `transfer(amount, category)`: Move funds between categories
- `get_balance()`: Get current balance
- `check_funds(amount)`: Verify sufficient funds

**Spending Chart**:
The `create_spend_chart()` function generates a visual bar chart showing percentage spent by category:

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

## Features

### Code Quality
- Clean, readable Python code
- Comprehensive error handling
- Object-oriented design principles
- Detailed inline documentation

### Testing Ready
- All projects include test cases
- Edge case handling
- Input validation
- Expected output formatting

### Educational Value
- Demonstrates string manipulation
- Shows mathematical calculations
- Illustrates object-oriented programming
- Teaches data structure usage

## Contributing

This is a personal learning project, but feedback and suggestions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add some improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

---

**Note**: These projects were completed as part of the FreeCodeCamp Scientific Computing with Python certification. They demonstrate fundamental programming concepts and problem-solving skills in Python.

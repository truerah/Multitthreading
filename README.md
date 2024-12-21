# Random Number Dashboard with Multithreading

## Overview

This project showcases a **Random Number Dashboard** that dynamically updates six boxes with random numbers. Each box generates numbers within a specific range and refreshes at unique intervals, ensuring an engaging and responsive user experience. The application leverages **multithreading** to maintain smooth performance.

---

## Features

- **Dynamic Number Generation**: Six boxes, each displaying random numbers from distinct ranges.
- **Independent Refresh Rates**: Each box updates its number at a unique interval.
- **Multithreading**: Ensures the GUI remains responsive by running updates concurrently.

---

## Input Parameters

### Number Ranges:

1. [10, 20]
2. [-10, 10]
3. [-100, 0]
4. [0, 20]
5. [-40, 40]
6. [100, 200]

### Refresh Intervals (in seconds):

1. 10 seconds
2. 20 seconds
3. 8 seconds
4. 12 seconds
5. 16 seconds
6. 14 seconds

---

## Output

The dashboard displays six boxes, each showing a random number updated at its respective interval. Below is a sample representation of the dashboard:
![image](https://github.com/user-attachments/assets/68f54719-ac81-4f49-a908-05cee7f38317)

---

## Technology Stack

- **Programming Language**: Python
- **Libraries**:
  - `tkinter` for GUI development
  - `threading` for multithreading support
  - `random` for number generation

---

## Implementation Details

### Multithreading

Each box runs on a separate thread to ensure independent and concurrent updates. This approach prevents the GUI from freezing or lagging while numbers are being refreshed.

### Random Number Generation

The `random.randint()` function is used to generate random numbers within the specified ranges.

---

## How to Run

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd random-number-dashboard
   ```

3. **Run the Application**:

   ```bash
   python main.py
   ```

---

##

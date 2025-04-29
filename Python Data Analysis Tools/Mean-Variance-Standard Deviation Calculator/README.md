# Mean-Variance-Standard Deviation Calculator

This project calculates key statistical measures — mean, variance, and standard deviation — for rows, columns, and flattened arrays of a 3x3 matrix, using NumPy for efficient computation.

It was developed as part of the freeCodeCamp Data Analysis with Python Certification.

---

## 🔹 Key Features
- Accepts a list of 9 numerical inputs.
- Converts the list into a 3x3 NumPy matrix.
- Calculates:
  - Mean
  - Variance
  - Standard deviation
  - Minimum
  - Maximum
  - Sum
for each row, column, and the flattened matrix.

---

## 🛠️ Technologies Used
- Python 3
- NumPy

---

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install numpy
2. Run the calculator
   ```bash
   python mean_var_std.py

## 📋 Sample Output
```
{'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
 'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
 'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
 'max': [[6, 7, 8], [2, 5, 8], 8.0],
 'min': [[0, 1, 2], [0, 3, 6], 0.0],
 'sum': [[9, 12, 15], [3, 12, 21], 36.0]}
```

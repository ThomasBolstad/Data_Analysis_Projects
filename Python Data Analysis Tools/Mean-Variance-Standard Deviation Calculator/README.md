# Mean-Variance-Standard Deviation Calculator

This project calculates statistical metrics — mean, variance, standard deviation, min, max, and sum — for rows, columns, and the entire matrix of a 3x3 numeric input. Built using NumPy, this tool demonstrates efficient numerical computation and data reshaping.

This was completed as part of freeCodeCamp’s Data Analysis with Python Certification.

---

## 🔹 Key Features

- Converts a 9-number list into a 3x3 NumPy array
- Computes:
  - Mean
  - Variance
  - Standard deviation
  - Min / Max
  - Sum
- Outputs stats by:
  - Column
  - Row
  - Flattened matrix

---

## 🛠️ Technologies Used

- Python 3
- NumPy

---

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install numpy
   ```

2. Run the script:
   ```bash
   python mean_var_std.py
   ```

---

## 📋 Sample Output

```
{'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
 'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
 'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
 'max': [[6, 7, 8], [2, 5, 8], 8.0],
 'min': [[0, 1, 2], [0, 3, 6], 0.0],
 'sum': [[9, 12, 15], [3, 12, 21], 36.0]}
```

---

## 📎 Project Files

- `mean_var_std.py` – Main logic for computing statistical outputs
- `test_module.py` – Unit tests provided by freeCodeCamp
- `requirements.txt` – Lists dependencies (`numpy`)

---

## 📄 License

This project is licensed under the MIT License.

---

> *"Mathematics is the language of the universe — here, it's just 9 numbers and a matrix."*

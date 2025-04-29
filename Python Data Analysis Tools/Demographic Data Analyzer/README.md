# Demographic Data Analyzer

This project analyzes demographic data from a census-style dataset to uncover trends across income levels, education, race, and other variables.

## 🔹 Key Features
- Computes categorical distributions (e.g., race breakdown, education levels)
- Calculates conditional statistics (e.g., percentage earning >50K based on education)
- Identifies correlations between income and education/work class

## 🛠️ Technologies
- Python (Pandas, NumPy)

## 📊 Data Source
- [adult.data.csv](https://archive.ics.uci.edu/ml/datasets/adult) (UCI Machine Learning Repository)

## 🚀 How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the analyzer: `python demographic_data_analyzer.py`
3. View outputs in console and/or charts.

## 📎 Project Files
- `demographic_data_analyzer.py` – Core analysis code
- `requirements.txt` – Python dependencies
- `adult.data.csv` – Dataset
- `test_module.py` – Test for certification purposes

## 📋 Sample Output

```
Number of each race:
 race
Amer-Indian-Eskimo      311
Asian-Pac-Islander     1039
Black                  3124
Other                   271
White                 27816
dtype: int64
Average age of men: 39.4
Percentage with Bachelors degrees: 16.4%
Percentage with higher education that earn >50K: 46.5%
Percentage without higher education that earn >50K: 17.4%
Min work time: 1 hours/week
Percentage of rich among those who work fewest hours: 10.0%
Country with highest percentage of rich: Iran
Highest percentage of rich people in country: 41.9%
Top occupations in India: Prof-specialty
```
## 📄 License

This project is licensed under the MIT License.

---

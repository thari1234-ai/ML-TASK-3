# 🚗 Auto MPG Prediction using Polynomial Regression

## 📌 Project Overview

This project predicts **fuel efficiency (MPG)** of cars using **Polynomial Regression**, which captures non-linear relationships between features.

---

## 🎯 Objective

To build a model that predicts MPG based on:

* Displacement
* Horsepower
* Weight
* Acceleration

---

## 📂 Project Structure

```
ML TASK-3/
│── auto_mpg.py
│── auto_mpg.csv
│── requirements.txt
│── README.md
```

---

## 📊 Dataset Description

| Feature      | Description              |
| ------------ | ------------------------ |
| Displacement | Engine size              |
| Horsepower   | Engine power             |
| Weight       | Vehicle weight           |
| Acceleration | Speed performance        |
| MPG          | Fuel efficiency (target) |

---

## ⚙️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Matplotlib

---

## 🚀 Steps Performed

1. Data Loading
2. Data Exploration
3. Feature Selection
4. Polynomial Feature Transformation (degree=2)
5. Model Training
6. Evaluation (MSE, R²)
7. Visualization

---

## 📈 Results

* Polynomial regression captures non-linear patterns better than linear models
* Improved prediction accuracy

---

## 🔍 Key Insights

* 📉 Higher **weight** reduces MPG
* 📉 Higher **horsepower** reduces fuel efficiency
* 📈 Lighter cars have better MPG
* Polynomial features improve model performance

---

## ▶️ How to Run

Install dependencies:

```
pip install pandas matplotlib scikit-learn
```

Run:

```
python auto_mpg.py
```

---

## ✅ Conclusion

Polynomial Regression is effective for modeling complex relationships in real-world datasets like vehicle fuel efficiency.

---

## 📌 Future Improvements

* Use full Auto MPG dataset
* Try higher-degree polynomials
* Compare with other models

---

## 👨‍💻 Author

THARINI P 
E24AI049


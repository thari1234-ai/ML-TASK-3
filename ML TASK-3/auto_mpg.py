import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load Data
df = pd.read_csv("auto_mpg.csv")

print("First 5 rows:\n", df.head())

# 2. Explore
print("\nMissing values:\n", df.isnull().sum())
print("\nStatistics:\n", df.describe())

# 3. Prepare Data
features = ["displacement", "horsepower", "weight", "acceleration"]
target = "mpg"

X = df[features]
y = df[target]

# Scatter plots (to see non-linear relation)
for col in features:
    plt.scatter(df[col], y)
    plt.xlabel(col)
    plt.ylabel("MPG")
    plt.title(f"{col} vs MPG")
    plt.show()

# 4. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Polynomial Transformation
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# 6. Model
model = LinearRegression()
model.fit(X_train_poly, y_train)

# 7. Prediction
y_pred = model.predict(X_test_poly)

# 8. Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MSE:", mse)
print("R2 Score:", r2)

# 9. Plot
plt.scatter(y_test, y_pred)
plt.xlabel("Actual MPG")
plt.ylabel("Predicted MPG")
plt.title("Polynomial Regression Results")
plt.show()
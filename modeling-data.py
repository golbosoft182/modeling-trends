#Data modeling and processing using python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Generate some random data
np.random.seed(42)
X = np.random.rand(100, 1) * 10
y = 2 * X + 3 + np.random.randn(100, 1)

# Create a pandas DataFrame from the generated data
df = pd.DataFrame(np.concatenate([X, y], axis=1), columns=['X', 'y'])

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df[['X']], df['y'], test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Plot the original data and the regression line
plt.scatter(X, y, color='b', label='Original Data')
plt.plot(X_test, y_pred, color='r', label='Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.show()

# Print the coefficients and intercept of the linear regression model
print('Coefficients:', model.coef_)
print('Intercept:', model.intercept_)
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Generate some random data
np.random.seed(42)
X = np.random.rand(100, 1) * 10
y = 2 * X + 3 + np.random.randn(100, 1)

# Create a pandas DataFrame from the generated data
df = pd.DataFrame(np.concatenate([X, y], axis=1), columns=['X', 'y'])

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df[['X']], df['y'], test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Plot the original data and the regression line
plt.scatter(X, y, color='b', label='Original Data')
plt.plot(X_test, y_pred, color='r', label='Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.show()

# Print the coefficients and intercept of the linear regression model
print('Coefficients:', model.coef_)
print('Intercept:', model.intercept_)

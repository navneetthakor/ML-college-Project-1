import numpy as np
from sklearn.linear_model import LinearRegression


X_train = np.array([182,178,150,130,160])
Y_train = np.array([75,72,62,40,67])

# Creating a linear regression model
model = LinearRegression()

# Training the model
model.fit(X_train.reshape(-1, 1), Y_train)

# Making predictions on the test set
# y_pred = model.predict(np.array([180]).reshape(1, -1))


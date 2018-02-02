import numpy as np

X_data = np.array([[0.3, 0.6], [0.7, 0.5]])

from sklearn.preprocessing import Binarizer
binarizer = Binarizer(threshold=0.5)
binarizer.fit(X_data)
Binarizer(copy=True, threshold=0.5)

X_data = binarizer.transform(X_data)
print(X_data)
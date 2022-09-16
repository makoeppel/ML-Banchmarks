from mlp import MLP
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import roc_auc_score


# set the seed
np.random.seed(42)

# get data
toy = False
if toy:
    # XOR
    x = np.array([[0, 0, 1, 1],
                  [0, 1, 0, 1]]).T
    y = np.array([[0, 1, 1, 0]]).T
else:
    x = np.genfromtxt('../../data/breast.csv', delimiter=",")
    y = np.genfromtxt('../../data/breast_y.csv', delimiter=",")
    x = MinMaxScaler().fit_transform(x)

# train the model
if toy:
    cls = MLP(input_size=len(x[0]), layers=[3, 1], learning_rate=0.1, epochs=5000)
else:
    cls = MLP(input_size=len(x[0]), layers=[10, 1], learning_rate=0.001, epochs=2000)
errors = cls.fit(x, y.reshape(-1,1))

# evaluation
y_pred = cls.predict(x)
auc = roc_auc_score(y, y_pred)
print('Multi-layer perceptron AUC: %.2f' % auc)

# plot training loss
plt.plot(errors, label="train")
plt.xlabel("epoch")
plt.ylabel("MSE")
plt.legend()
plt.savefig("python-train-mse.pdf")
plt.savefig("python-train-mse.png")

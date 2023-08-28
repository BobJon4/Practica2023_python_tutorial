import numpy as np


def g(s):
    return 1 / (1 + np.e ** (-s))


def normalize(s):
    return (s - np.mean(s))/(np.amax(s)-np.amin(s)), np.mean(s), (np.amax(s)-np.amin(s))


def rescale(s, mean, scale):
    return (s - mean)/scale


alfa = 0.1
x_train = np.loadtxt("data.txt", usecols=(0,))
y_train = np.loadtxt("data.txt", usecols=(1,))


x_train, mu, scaling_factor = normalize(x_train)

x_train = np.reshape(x_train, (len(x_train), 1))
n, m = x_train.shape
weights = np.zeros(m+1)
x_train = np.hstack((x_train, np.ones((n, 1))))
y_train = np.reshape(y_train, (len(y_train), 1))
weights = np.reshape(weights, (len(weights), 1))

for i in range(3000):

    weights = weights - alfa/n * np.dot(np.transpose(x_train), (g(np.dot(x_train, weights)) - y_train))

print(weights)

x_test = [14, 1, 6, 100]

x_test = rescale(x_test, mu, scaling_factor)
x_test = np.reshape(x_test, (len(x_test), 1))
n, m = x_test.shape
x_test = np.hstack((x_test, np.ones((n, 1))))

print(g(np.dot(x_test, weights)))



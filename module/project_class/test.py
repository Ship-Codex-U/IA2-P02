from perceptron import Perceptron

p = Perceptron()

inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
results = [0, 0, 0, 1]

p.train(inputs, results, 0.1, 1000)

print(p.predict(0, 0))
print(p.predict(0, 1))
print(p.predict(1, 0))
print(p.predict(1, 1))

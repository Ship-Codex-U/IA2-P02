import numpy as np

class Perceptron:
    def __init__(self):
        self.weights = [0, 0]
        self.bias = 0

    def activation(self, net: int) -> int:
        return 1 if net >= 0 else 0
    
    def train(self, inputs : list, results : list, alpha : float, iterations : int) -> tuple:

        self.weights = np.random.rand(2)
        self.bias = np.random.rand(1)
        totalError = 0

        for _ in range(iterations):
            totalError = 0

            for i in range(len(inputs)):
                net = inputs[i][0]*self.weights[0] + inputs[i][1]*self.weights[1] + self.bias

                y = self.activation(net)

                e = results[i] - y
                totalError += abs(e)

                if(e != 0):
                    self.weights[0] = self.weights[0] + e * alpha * inputs[i][0]
                    self.weights[1] = self.weights[1] + e * alpha * inputs[i][1]
                    self.bias = self.bias + e * alpha

            if totalError == 0:
                break

    def predict(self, x, y):
        net = x*self.weights[0] + y*self.weights[1] + self.bias

        return self.activation(net)
    
    def get_MB_equation_line(self):
        if self.weights[1]:
            m = -(self.weights[0] / self.weights[1])
            c = -(self.bias / self.weights[1])

            return (m,c)
        else:
            return None
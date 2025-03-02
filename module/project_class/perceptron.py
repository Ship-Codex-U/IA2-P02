import numpy as np

class Perceptron:
    def __init__(self):
        self.__weights = [0, 0]
        self.__bias = 0

    def activation(self, net: int) -> int:
        return 1 if net >= 0 else 0
    
    def train(self, inputs : list, results : list, alpha : float, iterations : int) -> tuple:

        self.__weights = np.random.rand(2)
        self.__bias = np.random.rand(1)
        totalError = 0

        for _ in range(iterations):
            totalError = 0

            for i in range(len(inputs)):
                net = inputs[i][0]*self.__weights[0] + inputs[i][1]*self.__weights[1] + self.__bias

                y = self.activation(net)

                e = results[i] - y
                totalError += abs(e)

                if(e != 0):
                    self.__weights[0] = self.__weights[0] + e * alpha * inputs[i][0]
                    self.__weights[1] = self.__weights[1] + e * alpha * inputs[i][1]
                    self.__bias = self.__bias + e * alpha

            if totalError == 0:
                break

    def predict(self, x, y):
        net = x*self.__weights[0] + y*self.__weights[1] + self.__bias

        return self.activation(net)
    
    def get_MB_equation_line(self):
        if self.__weights[1]:
            m = -(self.__weights[0] / self.__weights[1])
            c = -(self.__bias / self.__weights[1])

            return (m,c)
        else:
            return None
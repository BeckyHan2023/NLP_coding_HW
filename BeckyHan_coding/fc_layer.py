from layer import Layer
import numpy as np

# inherit from base class Layer
class FCLayer(Layer):
    # input_size = number of input neurons
    # output_size = number of output neurons
    def __init__(self, input_size, output_size):
        self.weights = np.random.rand(input_size, output_size) - 0.5
        self.bias = np.random.rand(1, output_size) - 0.5

    # returns output for a given input
    def forward_propagation(self, input_data):
        self.input = input_data
        # TODO: feedforward to return output
        self.output = np.dot(input_data, self.weights) + self.bias
        return self.output

    # computes dE/dW, dE/dB for a given output_error=dE/dY. Returns input_error=dE/dX.
    def backward_propagation(self, output_error, learning_rate):
        # TODO: computes dE/dW as weights_error, input_error=dE/dX for a given output_error=dE/dY
        weights_error = np.dot(self.input.T, output_error)
        bias_error = np.sum(output_error, axis=0, keepdims=True)
        input_error = np.dot(output_error, self.weights.T)

        # TODO: update parameters: self.weights, self.bias
        self.weights -= learning_rate * weights_error
        self.bias -= learning_rate * bias_error
        return input_error
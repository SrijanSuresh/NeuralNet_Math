class SimpleNeuron():
    weight = 0
    bias = 0
    def __init__(self, weight, bias):
        self.weight = weight
        self.bias = bias

def main():
    neuron = SimpleNeuron(0.5, 0.1)
    print(neuron.weight)
    print(neuron.bias)

if __name__ == '__main__':
    main()
# Topic: Comparison and Visualization of Activation Functions in Neural Networks

# Header: Activation Function Visualization: Sigmoid, Tanh, ReLU, Leaky ReLU, and Softmax

# This topic and header can set the context for demonstrating and comparing the behavior of various activation functions in neural networks, using graphical visualization to highlight the differences.


import numpy as np
import matplotlib.pyplot as plt

# Define activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

def softmax(x):
    exp_x = np.exp(x - np.max(x))  # Subtract max(x) for numerical stability
    return exp_x / np.sum(exp_x, axis=0)

# Generate input values
x = np.linspace(-10, 10, 500)

# Compute function values
sigmoid_values = sigmoid(x)
tanh_values = tanh(x)
relu_values = relu(x)
leaky_relu_values = leaky_relu(x)

# Prepare a multi-plot for visualization
plt.figure(figsize=(12, 10))

# Plot Sigmoid
plt.subplot(2, 2, 1)
plt.plot(x, sigmoid_values, label='Sigmoid', color='blue')
plt.title("Sigmoid Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)
plt.legend()

# Plot Tanh
plt.subplot(2, 2, 2)
plt.plot(x, tanh_values, label='Tanh', color='red')
plt.title("Tanh Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)
plt.legend()

# Plot ReLU
plt.subplot(2, 2, 3)
plt.plot(x, relu_values, label='ReLU', color='green')
plt.title("ReLU Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)
plt.legend()

# Show the activation function plots
plt.tight_layout()
plt.show()

# Now for Softmax
# Define input vector for softmax
input_vector = np.array([2.0, 1.0, 0.1])

# Compute softmax values
softmax_values = softmax(input_vector)

# Print and visualize Softmax
print("Input Vector: ", input_vector)
print("Softmax Output: ", softmax_values)

plt.figure(figsize=(6, 4))
plt.bar(range(len(input_vector)), softmax_values, 
        tick_label=[f"v({i})" for i in range(len(input_vector))], color='purple')
plt.title("Softmax Activation Function")
plt.xlabel("Input Index")
plt.ylabel("Softmax Output")
plt.grid(True)
plt.show()

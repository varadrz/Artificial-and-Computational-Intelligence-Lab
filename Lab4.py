# To implement local search algorithm such as Simulated Annealing

import math
import random

# Simulated Annealing parameters
def simulated_annealing(objective_function, initial_solution, max_iterations, initial_temp, cooling_rate):
    # Initial solution and objective value
    current_solution = initial_solution
    current_value = objective_function(current_solution)

    # Best solution
    best_solution = current_solution
    best_value = current_value

    # Temperature
    temperature = initial_temp

    for iteration in range(max_iterations):
        # Generate a new candidate solution (neighbor)
        new_solution = get_neighbor(current_solution)
        new_value = objective_function(new_solution)

        # Calculate the difference in objective function
        delta_value = new_value - current_value

        # Determine whether to accept the new solution
        if delta_value < 0 or math.exp(-delta_value / temperature) > random.random():
            current_solution = new_solution
            current_value = new_value

        # Update the best solution found so far
        if current_value < best_value:
            best_solution = current_solution
            best_value = current_value

        # Cool down the temperature
        temperature *= cooling_rate

    return best_solution, best_value

# Objective function (to be minimized)
def objective_function(solution):
    # Example: a quadratic function as the objective
    return sum(x**2 for x in solution)

# Function to generate a neighbor solution
def get_neighbor(solution):
    # Slightly modify a random element in the solution (example with continuous variables)
    neighbor = solution[:]
    index = random.randint(0, len(solution) - 1)
    neighbor[index] += random.uniform(-1, 1)  # Change this according to your problem
    return neighbor

# Example usage
initial_solution = [random.uniform(-10, 10) for _ in range(5)]  # Initial random solution
max_iterations = 1000
initial_temp = 100
cooling_rate = 0.99

best_solution, best_value = simulated_annealing(objective_function, initial_solution, max_iterations, initial_temp, cooling_rate)

print("Best solution:", best_solution)
print("Best objective value:", best_value)
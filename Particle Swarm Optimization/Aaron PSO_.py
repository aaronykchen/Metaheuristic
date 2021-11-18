"""
寫到 ---
Problem 6
@Aaron YuKu Chen
"""
import pandas as pd
import numpy as np
from numpy.random import randn
import random
import math as m
from matplotlib import pyplot as plt

pi = m.pi  # set π , objective function will use it
swarm_size = 30
acceleration_constants = 2
random_num = random.uniform(0, 1)
max_iterations = 100
x_domain = [2, 4]
y_domain = [-1, 2]
initial_velocity_constraint = [-1, 1]
w = 1
r1, r2 = random.uniform(0, 1), random.uniform(0, 1)
c1, c2 = 2, 2
v_max = 2


def initialization():
    particles = []
    velocity = []
    for i in range(swarm_size):
        s = random.uniform(0, 1)
        i_location = [
            s * (x_domain[1] - x_domain[0]) + x_domain[0], s * (y_domain[1] - y_domain[0]) + y_domain[0]]
        particles.append(i_location)
        initialization_locations = np.array(particles)
        i_velocity = [
            s * (initial_velocity_constraint[1] - initial_velocity_constraint[0]) + initial_velocity_constraint[0],
            s * (initial_velocity_constraint[1] - initial_velocity_constraint[0]) + initial_velocity_constraint[0]]
        velocity.append(i_velocity)
        initialization_velocities = np.array(velocity)
    return initialization_locations, initialization_velocities


def updateCurrentLoc(new_locations):
    current_locations = new_locations
    return current_locations


def computeFitness(current_locations, pBest_fitness, pBest_locations, gBest_fitness,
                   gBest_location):  # compute the fitness then update pBest and determine gBest
    temp_fitnessValue = []
    for particle in range(swarm_size):
        x_value = current_locations[particle][0]
        y_value = current_locations[particle][1]
        if x_value + y_value <= 5:
            fitness_value = m.sin(5 * pi * (x_value ** (3 / 4) - 0.1)) ** 2 - (y_value - 1) ** 4
        else:
            fitness_value = m.sin(5 * pi * (x_value ** (3 / 4) - 0.1)) ** 2 - (y_value - 1) ** 4 - 999

        temp_fitnessValue.append(fitness_value)
        current_fitness = temp_fitnessValue
    for order in range(swarm_size):  # update pBest
        if current_fitness[order] > pBest_fitness[order]:
            pBest_fitness[order] = current_fitness[order]
            pBest_locations[order] = current_locations[order]
        else:
            pass
    for order_gBest in range(swarm_size):  # determine gBest
        if current_fitness[order_gBest] > gBest_fitness:
            gBest_fitness = current_fitness[order_gBest]
            gBest_location = current_locations[order_gBest]
        else:
            pass
    return pBest_fitness, pBest_locations, gBest_fitness, gBest_location


def computeVelociteis(current_locations):
    for order_vel in range(swarm_size):
        current_velocities[order_vel][0] = w * current_velocities[order_vel][0] + r1 * c1 * (
                pBest_locations[order_vel][0] - current_locations[order_vel][0]) + r2 * c2 * (
                                                   gBest_location[0] - current_locations[order_vel][0])
        current_velocities[order_vel][1] = w * current_velocities[order_vel][1] + r1 * c1 * (
            pBest_locations[order_vel][1]) - \
                                           current_locations[order_vel][1] + r2 * c2 * (
                                                   gBest_location[1] - current_locations[order_vel][1])
        if current_velocities[order_vel][0] > v_max:  # Velocity damping for v_max as 2
            current_velocities[order_vel][0] = v_max
        if current_velocities[order_vel][0] < -v_max:
            current_velocities[order_vel][0] = -v_max
        elif current_velocities[order_vel][1] > v_max:
            current_velocities[order_vel][1] = v_max
        elif current_velocities[order_vel][1] < -v_max:
            current_velocities[order_vel][1] = -v_max
        else:
            pass
    new_velocities = current_velocities
    print(new_velocities)
    return new_velocities


def computeNewLocation(current_locations, new_velocities):
    new_locations = current_locations + new_velocities
    return new_locations


# Run the procedure

current_locations, current_velocities = initialization()

pBest_locations = current_locations  # set current locations as pBest location

initialization_fitnessValue = []
for particle in range(swarm_size):
    x_value = pBest_locations[particle][0]
    y_value = pBest_locations[particle][1]
    if x_value + y_value <= 5:
        fitness_value = m.sin(5 * pi * (x_value ** (3 / 4) - 0.1)) ** 2 - (y_value - 1) ** 4
    else:
        fitness_value = m.sin(5 * pi * (x_value ** (3 / 4) - 0.1)) ** 2 - (y_value - 1) ** 4 - 999  # give penalty
    initialization_fitnessValue.append(fitness_value)
pBest_fitness = initialization_fitnessValue


gBest_fitness = max(pBest_fitness)
gBest_location = pBest_locations[pBest_fitness.index(gBest_fitness)]  # determine gBest location

new_locations = pBest_locations
history_gBest_fitness = []
for iteration in range(max_iterations):
    current_locations = updateCurrentLoc(new_locations)
    pBest_fitness, pBest_locations, gBest_fitness, gBest_location = \
        computeFitness(current_locations, pBest_fitness, pBest_locations, gBest_fitness, gBest_location)
    history_gBest_fitness.append(gBest_fitness)
    new_velocities = computeVelociteis(current_locations)
    new_locations = computeNewLocation(current_locations, new_velocities)
    for i in range(swarm_size):  # repair the locations if they are outlier
        if new_locations[i][0] < 2:
            new_locations[i][0] = 2
        elif new_locations[i][0] > 4:
            new_locations[i][0] = 4
        elif new_locations[i][1] < -1:
            new_locations[i][1] = -1
        elif new_locations[i][1] > 2:
            new_locations[i][1] = 2
        else:
            pass


print("Final gBest Value is:  ", gBest_fitness)  # print the final optimal value



####

history_gBest_fitness = pd.DataFrame(history_gBest_fitness)
plt.style.use('fivethirtyeight')
plt.plot(range(max_iterations), pd.DataFrame.rolling(history_gBest_fitness, window=30, min_periods=1).max())
plt.xlim(0, 100)
plt.ylim(0.99, 1.0)

plt.xlabel("Iterations")
plt.ylabel("Optimal gBest Value")
plt.title("Particle Swarm Optimization for Problem 6")

plt.show()



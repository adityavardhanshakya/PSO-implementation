import random
import numpy as np
import matplotlib.pyplot as plt

random.seed(12)

class Particle():
    def __init__(self):
        x = (-1) ** bool(random.getrandbits(1)) * random.random() * 1000
        y = (-1) ** bool(random.getrandbits(1)) * random.random() * 1000
        self.position = np.array([x, y])
        self.pBest_position = self.position
        self.pBest_value = float('inf')
        self.velocity = np.array([0, 0])

    def update(self):
        self.position = self.position + self.velocity

class Space():
    def __init__(self, target, target_error, n_particles, W, c1, c2):
        self.target = target
        self.target_error = target_error
        self.n_particles = n_particles
        self.particles = []
        self.gBest_value = float('inf')
        self.gBest_position = np.array([random.random() * 50, random.random() * 50])
        self.W = W
        self.c1 = c1
        self.c2 = c2

    def fitness(self, particle):
        x = particle.position[0]
        y = particle.position[1]
        f = x**2 + y**2 + 1
        return f

    def set_pBest(self):
        for particle in self.particles:
            fitness_candidate = self.fitness(particle)
            if particle.pBest_value > fitness_candidate:
                particle.pBest_value = fitness_candidate
                particle.pBest_position = particle.position

    def set_gBest(self):
        for particle in self.particles:
            best_fitness_candidate = self.fitness(particle)
            if self.gBest_value > best_fitness_candidate:
                self.gBest_value = best_fitness_candidate
                self.gBest_position = particle.position

    def update_particles(self):
        for particle in self.particles:
            inertial = self.W * particle.velocity
            self_confidence = self.c1 * random.random() * (particle.pBest_position - particle.position)
            swarm_confidence = self.c2 * random.random() * (self.gBest_position - particle.position)
            new_velocity = inertial + self_confidence + swarm_confidence
            particle.velocity = new_velocity
            particle.update()

    def show_particles(self, iteration):
        print(iteration, 'iterations')
        print('BestPosition in this time:', self.gBest_position)
        print('BestValue in this time:', self.gBest_value)

        for particle in self.particles:
            plt.plot(particle.position[0], particle.position[1], 'ro')
        plt.plot(self.gBest_position[0], self.gBest_position[1], 'bo')
        plt.show()

# User Input
target_function = input("Enter the target function (e.g., 'x**2 + y**2 + 1'): ")
target_error = float(input("Enter the target error: "))
n_particles = int(input("Enter the number of particles: "))
W = float(input("Enter the inertial weight (W): "))
c1 = float(input("Enter the self-confidence coefficient (c1): "))
c2 = float(input("Enter the swarm-confidence coefficient (c2): "))
n_iterations = int(input("Enter the number of iterations: "))

# Define the target function dynamically
def target(x, y):
    return eval(target_function)

search_space = Space(target, target_error, n_particles, W, c1, c2)
particle_vector = [Particle() for _ in range(search_space.n_particles)]
search_space.particles = particle_vector

iteration = 0
while iteration < n_iterations:
    # set particle best & global best
    search_space.set_pBest()
    search_space.set_gBest()

    # visualization
    search_space.show_particles(iteration)

    # check conditional
    if abs(search_space.gBest_value - search_space.target(0, 0)) <= search_space.target_error:
        break

    search_space.update_particles()
    iteration += 1

print("The best solution is:", search_space.gBest_position, "in", iteration, "iterations")

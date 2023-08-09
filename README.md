# Particle Swarm Optimization (PSO) for Function Optimization

This repository contains a Python implementation of the Particle Swarm Optimization (PSO) algorithm for function optimization. PSO is a heuristic optimization technique inspired by the social behavior of birds and fish. It is used to find the optimal solution to a given problem by iteratively adjusting a population of particles.

## Requirements

- Python (>= 3.6)
- NumPy (>= 1.19)
- Matplotlib (>= 3.3)

## Usage

1. Clone the repository or download the `pso_optimization.py` file.

2. Ensure you have the required libraries installed by running:
   ```
   pip install numpy matplotlib
   ```

3. Open the `pso_optimization.py` file in your favorite Python environment.

4. Customize the parameters at the beginning of the script according to your optimization problem:
   - `W`, `c1`, `c2`: Control parameters for the PSO algorithm.
   - `n_iterations`: Number of iterations for the optimization process.
   - `n_particles`: Number of particles in the swarm.
   - `target_error`: Desired precision of the solution.

5. Modify the `fitness` function in the `Space` class to define your target function that needs optimization.

6. Run the script.


## Same will follow for the User Input Program

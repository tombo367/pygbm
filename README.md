[![Documentation Status](https://readthedocs.org/projects/tb711-pygbm/badge/?version=latest)](https://ljf441-pygbm.readthedocs.io/en/latest/)

# pygbm
The **pygbm** package is a Python package to simulate geometric Brownian motion.

## Features
- **GBM**: core attribute and implements the analytic solution
- **EMGBM**: implements the Euler-Maruyama method
- **MGBM**: implements the Milstein method

## Usage

Here's a quick example of how to use this package:
```python
  import pygbm
  import matplotlib.pyplot as plt

  y0 = 1.0
  mu = 0.05
  sigma = 0.2 
  T = 1.0
  N = 100

  simulator = pygbm.GBM(y0, mu, sigma) 
  t, y = simulator.get_solution(T, N)
  
  plt.plot(t, y, label="GBM Path")  
  plt.xlabel("Time")
  plt.ylabel("Y")
  plt.title("Simulated Geometric Brownian Motion Path")
  plt.legend()
  plt.show()
```

To run a simulation directly in CLI, see the following example:
```bash
pygbm euler --y0 1.0 --mu 0.05 --sigma 0.2 --method milstein --T 1.0 --N 100 --output gbm_plot.png
```

## Documentation

Visit our [documentation page](https://tb711-pygbm.readthedocs.io/en/latest/)

## License

This project is licensed under the MIT License - see the ``LICENSE`` file for details.
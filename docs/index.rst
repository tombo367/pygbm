pygbm
==============================================================================

  *Author* Tom Borrett

The **pygbm** package is a Python package designed to simulate geometric Brownian motion.

Features 
------------

- **GBM**: core attribute and implements the analytic solution
- **EMGBM**: implements the Euler-Maruyama method
- **MGBM**: implements the Milstein method

Installation
------------
Ensure you have Python 3.6 or higher. Install the package and its dependencies with:
```bash
pip install -e .
```

Usage
------------
Here's a quick example of how to use the package:
```python
import pygbm
import matplotlib.pyplot as plt
  
y0 = 1.0
mu = 0.05
sigma = 0.2 
T = 1.0
N = 100

simulator =  GBM(y0, mu, sigma)
  
t, y = simulator.get_solution(T, N)

plt.plot(t_values, y_values, label="GBM Path")
plt.xlabel("Time")
plt.ylabel("Y")
plt.title("Simulated Geometric Brownian Motion Path")
plt.legend()
plt.show()
```

Contributing
------------

Contributions are welcome! Fork our repository and submit a pull request.

License
-------

This project is licensed under the MIT License - see the `LICENSE` file for details.




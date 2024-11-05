[![Documentation Status](https://readthedocs.org/projects/tb711-pygbm/badge/?version=latest)](https://ljf441-pygbm.readthedocs.io/en/latest/)

# pygbm
The **pygbm** package is a Python package to simulate geometric Brownian motion.

## Features
- **GBM**: core attribute and implements the analytic solution
- **EMGBM**: implements the Euler-Maruyama method
- **MGBM**: implements the Milstein method

## Run a simulation in CLI
To run a simulation in CLI, use the following:
```bash
pygbm euler --y0 1.0 --mu 0.05 --sigma 0.2 --method milstein --T 1.0 --N 100 --output gbm_plot.png
```
`--y0`, `--mu`, and `--sigma` arguments are required, while defaults are, Milstein method for `--method`, 10 for `--T`, 100 for `--N`, and gbm_plot.png for `--output`.
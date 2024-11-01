import gbm_simulator
import matplotlib.pyplot as plt
import numpy as np

y0 = 1.0
mu = 0.05
sigma = 0.2

simulator = gbm_simulator.GBM(y0, mu, sigma)
t, Y = simulator.get_solution(10, 100)

plt.plot(t, Y, label="Analytic Method")

simulator = gbm_simulator.EMGBM(y0, mu, sigma)
t, Y = simulator.get_solution(10, 100)

plt.plot(t, Y, label="Euler-Maruyama Method")

simulator = gbm_simulator.MGBM(y0, mu, sigma)
t, Y = simulator.get_solution(10, 100)

plt.plot(t, Y, label="Milstein Method")

plt.legend()

plt.show()



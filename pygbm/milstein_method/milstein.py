import numpy as np

from numpy import exp, sqrt

class MGBM:
    def __init__(self, y0, mu, sigma):
        self.y0 = y0
        self.mu = mu
        self.sigma = sigma

    def get_solution(self, time=10, N=100):
        
        np.random.seed(42)

        t = np.linspace(0, time, N)
        dt = t[1] - t[0]

        # Initialize the Weiner Process
        dB = np.random.normal(scale=sqrt(dt), size=N-1)
        dB = np.concatenate(([0], dB))

        Y = np.zeros(N)
        Y[0] = self.y0

        for i in range(1, len(t)):
            Y[i] = Y[i - 1] + self.mu * Y[i - 1] * dt + self.sigma * Y[i - 1] * dB[i - 1] + 1 / 2 * self.sigma * Y[i - 1] * dB[i - 1] \
                   * self.sigma * (dB[i - 1] ** 2 - dt)

        return t, Y

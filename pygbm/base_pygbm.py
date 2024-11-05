import numpy as np

from numpy import exp, sqrt

class GBM:
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
        B_t = np.concatenate(([0], np.cumsum(dB)))
        
        Y = self.y0 * exp((self.mu - self.sigma ** 2 / 2) * t + self.sigma * B_t)

        return t, Y


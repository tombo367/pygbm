import argparse
import matplotlib.pyplot as plt
import numpy as np
from gbm_simulator import GBM, EMGBM, MGBM

def get_solution(y0, mu, sigma, T=10, N=100):
    """Run the GBM simulation and return the results."""
    simulator = GBM(y0, mu, sigma)
    time, simulation = simulator.get_solution(T, N)
    return time, simulation

def plot_simulation(simulation, T, N):
    """Plot the simulation results."""
    plt.figure(figsize=(12, 6))
    time = np.linspace(0, T, N)
    plt.plot(time, simulation)
    plt.title(f"Geometric Brownian Motion Simulation\nTime: {T}")
    plt.xlabel("Time Steps")
    plt.ylabel("Value")
    plt.grid()
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Pygbm CLI tool")
    subparsers = parser.add_subparsers(dest="command")

    # Create subparser for "simulate" command
    simulate_parser = subparsers.add_parser("simulate", help="Run a GBM simulation")
    simulate_parser.add_argument("--y0", type=float, help="Initial value of the process (y0)")
    simulate_parser.add_argument("--mu", type=float, help="Expected return (mu)")
    simulate_parser.add_argument("--sigma", type=float, help="Volatility of the process (sigma)")
    simulate_parser.add_argument('--method', type=str, choices=['analytic', 'milstein', 'euler-maruyama'], default='milstein', help='Simulation method')
    simulate_parser.add_argument("--T", type=float, default=10, help="Total time for the simulation (default: 10)")
    simulate_parser.add_argument("--N", type=int, default=100, help="Number of iterations (default: 100)")
    simulate_parser.add_argument("--output", type=str, default="gbm_plot.png", help="Output file name for the plot (default: gbm_plot.png)")

    # Parse the arguments
    args = parser.parse_args()

    if args.command == 'simulate':
        if args.method == "milstein":
            simulator = MGBM(args.y0, args.mu, args.sigma)
        elif args.method == "euler-maruyama":
            simulator = EMGBM(args.y0, args.mu, args.sigma)
        else:
            simulator = GBM(args.y0, args.mu, args.sigma)
        # Extract the parameters
        t, Y = simulator.get_solution(args.T, args.N)
        if args.output is not None:
            plt.plot(t, Y)
            plt.title("Geometric Brownian Motion Simulation")
            plt.xlabel("Time")
            plt.ylabel("Value")
            plt.savefig(args.output)
            print(f"Plot saved to: {args.output}")
            plt.close()

if __name__ == "main":
    main()

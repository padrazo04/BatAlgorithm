from BatAlgorithm import *
from time import time


def RosenbrockFunction(dimensions, sol):
    val = 0.0
    for i in range(dimensions-1):
        val += (1 - sol[i])**2 + 100*(sol[i+1]-sol[i]**2)**2
    return val


def main():
    for i in range(10):
        Algorithm = BatAlgorithm (
            dimensions=2, populationSize=40, generations=2000, 
            A=1, r=0, fMin=-1.0, fMax=10.0, lower=-10.0, upper=10.0,
            alpha=0.001, gamma=0.001, function=RosenbrockFunction
        )

        start = time()

        Algorithm.moveBats()

        end = time()

        print("Elapsed time: ", end - start)
        print("===")


if __name__ == "__main__":
    main()

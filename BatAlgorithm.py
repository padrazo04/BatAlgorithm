import numpy as np
from random import gauss
from math import exp

class BatAlgorithm():
    def __init__(self, dimensions, populationSize, generations, A, r, 
                 fMin, fMax, lower, upper, alpha, gamma, function):
        self.dimensions = dimensions 
        self.populationSize = populationSize
        self.generations = generations

        self.lower = lower  # Lower bound
        self.upper = upper  # Upper bound

        self.sol = [[0 for i in range(self.dimensions)] for j in range(self.populationSize)]  # Population of solutions
        self.v = [[0 for i in range(self.dimensions)] for j in range(self.populationSize)]  # Velocity
        
        self.frequency = [0] * self.populationSize
        self.fMin = fMin
        self.fMax = fMax
        
        self.A = [A] * self.populationSize  # Loudness
        self.r = [r] * self.populationSize  # Pulse rate
        self.r0 = [0] * self.populationSize # Pulse rate at generation 0

        self.fitness = [0] * self.populationSize 
        
        self.bestSol = [0] * self.dimensions
        self.bestFitness = 0.0

        self.alpha = alpha # Constant to update loudness
        self.gamma = gamma # Constant to update pulse rate

        self.function = function # Objective Function


    def initBats(self):
        for i in range(self.populationSize):
            for j in range(self.dimensions):
                self.v[i][j] = 0.0
                self.sol[i][j] = self.lower + (self.upper - self.lower) * np.random.uniform(0, 1)

            self.frequency[i] = self.fMin + (self.fMax - self.fMin) * np.random.uniform(0,1)

            self.A[i] = np.random.uniform(0, 1) + self.A[i]
            self.r[i] = np.random.uniform(0, 1) + self.r[i]
            self.r0[i] = self.r[i]

            self.fitness[i] = self.function(self.dimensions, self.sol[i])


    def findBestBat(self):
        bestSolPosition = 0

        for i in range(self.populationSize):
            if self.fitness[i] < self.fitness[bestSolPosition]:
                bestSolPosition = i

        for i in range(self.dimensions):
            self.bestSol[i] = self.sol[bestSolPosition][i]

        self.bestFitness = self.fitness[bestSolPosition]


    def simpleBounds(self, val, lower, upper):
        if val < lower:
            val = lower

        if val > upper:
            val = upper

        return val


    def calculateAvgLoudness(self):
        add = 0.0

        for i in range(self.populationSize):
            add += self.A[i]

        return add / self.populationSize


    def moveBats(self):
        newPos = [[0.0 for i in range(self.dimensions)] for j in range(self.populationSize)]

        self.initBats()
        self.findBestBat()

        for t in range(self.generations):
            averageLoudness = self.calculateAvgLoudness()

            for i in range(self.populationSize):
                rnd = np.random.uniform(0, 1)
                self.frequency[i] = self.fMin + (self.fMax - self.fMin) * rnd

                for j in range(self.dimensions):
                    self.v[i][j] = self.v[i][j] + (self.sol[i][j] - self.bestSol[j]) * self.frequency[i]
                    newPos[i][j] = self.sol[i][j] + self.v[i][j]
                    newPos[i][j] = self.simpleBounds(newPos[i][j], self.lower, self.upper)

                rnd = np.random.random_sample()

                if rnd > self.r[i]:
                    for j in range(self.dimensions):
                        epsilon = gauss(0, 1)
                        newPos[i][j] = self.bestSol[j] + epsilon * averageLoudness
                        newPos[i][j] = self.simpleBounds(newPos[i][j], self.lower, self.upper)
                        
                newFitness = self.function(self.dimensions, newPos[i])

                rnd = np.random.random_sample()

                if (rnd < self.A[i]) and (newFitness <= self.fitness[i]):
                    for j in range(self.dimensions):
                        self.sol[i][j] = newPos[i][j]

                    self.fitness[i] = newFitness

                    self.A[i] = self.alpha * self.A[i]
                    self.r[i] = self.r0[i] * (1 - exp(-self.gamma * t))

                if newFitness <= self.bestFitness:
                    for j in range(self.dimensions):
                        self.bestSol[j] = newPos[i][j]
                    self.bestFitness = newFitness

        print(self.bestFitness)

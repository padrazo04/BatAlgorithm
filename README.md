# Bat Algorithm in Python

## Objective
The main objective is to solve the well-known problem Rosenbrock function optimization using implementation of Bat Algorithm in Python programming language.

## Bat Algorithm
Bat Algorithm is a metaheuristic bat-inspired algorithm introduced by Xin-She Yang in 2010. The algorithm is based on bats skill to locate preys and insects using echolocation. With this sonar, bats can fly dodging all kind of obstacles until they finally reach their prey. Going back to programming world we will define a bat in our program by the following features:

1. **Position x<sub>i</sub>** : Location of the bat among the whole solutions space. This feature is also called location or simply solution.
2. **Velocity v<sub>i</sub>** : Speed at which the bat flies. We will use the velocity to calculate subsequent positions of the bat.
3. **Frequency f<sub>i</sub>** : Value that determines the wavelength of the pulses emitted by the bat. As higher is the frequency, then quickly is the response from where is the prey. Moreover, bats can adjust the frequency of their pulses in a range \[f<sub>min</sub>,f<sub>max</sub>] depending on the proximity of their target.
4. **Loudness A<sub>i</sub>** : Value that reflects bats pulse loudness. Loudness varies from the loudest when a bat is searching for his prey to a quieter base when he is closer to his prey.
5. **Pulse rate r<sub>i</sub>** : Value that refers to the rate that a bat emits his ultrasonic pulse, when bats are flying and searching for a prey, they have lower values pulse rate. When they get closer to his prey, then they need higher values of pulse rate in order to get a great accuracy about the prey position.

Here is the pseudocode of the algorithm, implemented in BatAlgorithm.py with some minor changes whose only aim are the improvement of the algorithm performance

![Pseudocode of Bat Algorithm](https://i.imgur.com/AfsBlG6.png)

The following images shows the equations that Bat Algorithm uses and the pseudocode step in which they are required:

* Adjust frecuency

![Adjust frecuency equation](https://i.imgur.com/ozwHjin.png)

Where beta is in range \[0,1]

* Update velocity

![Update velocity equation](https://i.imgur.com/YF3NZUu.png)

Where x<sub>*</sub> is the current global best position

* Update position

![Update position](https://i.imgur.com/LBCA2Ae.png)

* Generate local solution arond the selected best solution

![Generate local solution arond the selected best solution](https://i.imgur.com/qGIFuu1.png)

Where epsilon is in range \[-1,1] and A<sup>t</sup> is the average loudness of all the bats at this time step

* Increase r<sub>i</sub>

![Increase ri](https://i.imgur.com/QiPBMMq.png)

Where gamma is a constant

* Reduce A<sub>i</sub>

![Reduce Ai](https://i.imgur.com/UhRbfr7.png)

Where alpha is a constant


### Rosenbrock Function
![Rosenbrock function of two variables](https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Rosenbrock_function.svg/450px-Rosenbrock_function.svg.png)

The Rosenbrock function is a typical test for optimize algorithms. It was introduced by Howard H. Rosenbrock in 1960.
The global minimum is inside a long, narrow, parabolic shaped flat valley. To find the valley is trivial. To converge to the global minimum, however, is difficult.

The function is defined by

![Equation of Rosenbrock function](https://i.imgur.com/kdOHvv9.png)

Usually ***a** = 1* and ***b** = 100*. This function has a global minimum at *(x,y) = (1, 1) --> f(x,y) = (0, 0)* which can be generalized for N-dimensions, in this case the minimum for N-dimensions will be *(x\*) = (1,...,1)*

### Example
The following example presents a simple use of bat algorithm. `function()` denotes the objective function that may be changed by the user. Control parameters should be defined within `BatAlgorithm()` constructor. Order of parameters is as 
follows: `BatAlgorithm(dimensions, populationSize, generations, A, r, fMin, fMax, lower, upper, function)` where:

- `dimensions`  denotes dimension of the problem,
- `populationSize` denotes population size,
- `generations`  denotes number of generations (iterations),
- `A` parameter denotes loudness,
- `r` parameter denotes pulse rate,
- `fMin` parameter denotes frequency minimum,
- `fMax` parameter denotes frequency maximum,
- `lower` denotes lower bound,
- `upper` denotes upper bound and
- `function` passes objective function.

## Code Example

```python
from BatAlgorithm import *
from time import time

def RosenbrockFunction(dimensions, sol):
    val = 0.0
    for i in range(dimensions-1):
        val += (1 - sol[i]**2)**2 + 100*(sol[i+1]-sol[i]**2)**2
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
```

## Bugs
Bugs and extension should be send via Github.

## Authors
Carlos Freire Caballero

## References

Yang, X.-S. "A new metaheuristic bat-inspired algorithm." Nature inspired cooperative strategies for optimization (NICSO 2010). Springer
Berlin Heidelberg, 2010. 65-74.

Fister, I. Jr., Fister, I., Yang, X.-S., Fong, S., Zhuang, Y. "Bat algorithm: Recent advances." IEEE 15th International Symposium on Computational Intelligence and Informatics (CINTI), IEEE, 2014. 163-167.

https://www.researchgate.net/publication/300297266_The_bat_algorithm_and_its_parameters

https://www.researchgate.net/publication/318929033_New_binary_bat_algorithm_for_solving_0-1_knapsack_problem

https://www.researchgate.net/publication/318239029_Study_of_Parameter_Sensitivity_on_Bat_Algorithm

import numpy as np
import random
import operator
import pandas as pd
import matplotlib.pyplot as plt

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Find the Eucledian distance between the two cities
    def distance(self, city):
        x_dis = abs(self.x - city.x)
        y_dis = abs(self.y - city.y)
        distance = np.sqrt((x_dis ** 2) + (y_dis ** 2))
        return distance
    
    def __repr__(self):
        return f"({self.x},{self.y})"

class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0.0
    
    def route_distance(self):
        if self.distance == 0:
            path_distance = 0 # Get the total distance of the route
            for i in range(len(self.route)):
                from_city = self.route[i]
                to_city = self.route[(i + 1) % len(self.route)]
                path_distance += from_city.distance(to_city)
            self.distance = path_distance
        return self.distance
    
    def route_fitness(self):
        if self.fitness == 0: # Get the fitness score based on the reciprocal of the distance
            self.fitness = 1 / float(self.route_distance())
        return self.fitness

# Create a random route by going through the list of the given cities
def create_route(city_list):
    route = random.sample(city_list, len(city_list))
    return route

class GeneticAlgo:
    def __init__(self, city_list, population_size, generations):
        self.city_list = city_list
        self.population_size = population_size
        self.generations = generations

    def initial_population(self):
        population = [] # Initializa a population with random routes
        for _ in range(self.population_size):
            route = create_route(self.city_list)
            population.append(route)
        return population

    def rank_routes(self, population): # Add ranking for routes based on the fitness score
        fitness_results = {}
        for i, route in enumerate(population):
            fitness = Fitness(route).route_fitness()
            fitness_results[i] = fitness
        return sorted(fitness_results.items(), key=operator.itemgetter(1), reverse=True)

    def selection(self, ranked_population): # Do the roulette wheel selection to pick the parents
      selection_results = []
      df = pd.DataFrame(ranked_population, columns=['Index', 'Fitness'])
      df['cum_sum'] = df['Fitness'].cumsum()
      df['cum_perc'] = 100 * df['cum_sum'] / df['Fitness'].sum()

      for _ in range(self.population_size):
        rand_num = random.random() * 100
        selected_route = df[df['cum_perc'] >= rand_num].iloc[0]
        selection_results.append(int(selected_route['Index']))  
      return selection_results

    def mating_pool(self, population, selection_results): # Create the mating pool for the selected routes
        mating_pool = []
        for i in range(len(selection_results)):
            index = selection_results[i]
            mating_pool.append(population[index])
        return mating_pool

# PMX Algorithm to create the child route based on the parents
    def breed(self, parent1, parent2):
        child = []
        child_parent1 = []
        child_parent2 = []

        gene_a = int(random.random() * len(parent1))
        gene_b = int(random.random() * len(parent1))

        start_gene = min(gene_a, gene_b)
        end_gene = max(gene_a, gene_b)

        for i in range(start_gene, end_gene):
            child_parent1.append(parent1[i])

        child_parent2 = [item for item in parent2 if item not in child_parent1]

        child = child_parent1 + child_parent2
        return child
# Create new population through the crossover of mating_pool
    def breed_population(self, mating_pool):
        children = []
        length = len(mating_pool) - self.population_size
        pool = random.sample(mating_pool, len(mating_pool))

        for i in range(self.population_size):
            child = self.breed(pool[i], pool[len(mating_pool) - i - 1])
            children.append(child)
        return children
# Swap mutation to create diversity
    def mutate(self, individual, mutation_rate):
        for swapped in range(len(individual)):
            if random.random() < mutation_rate:
                swap_with = int(random.random() * len(individual))
                city1 = individual[swapped]
                city2 = individual[swap_with]
                individual[swapped] = city2
                individual[swap_with] = city1
        return individual
# Apply the mutation 
    def mutate_population(self, population, mutation_rate):
        mutated_population = []

        for ind in range(len(population)):
            mutated_individual = self.mutate(population[ind], mutation_rate)
            mutated_population.append(mutated_individual)
        return mutated_population

    def run(self):
        population = self.initial_population() # Initializa progress and population list
        progress = []
        progress.append(1 / self.rank_routes(population)[0][1])
        # Base genetic algorithm loop
        for i in range(self.generations): 
            ranked_population = self.rank_routes(population) # Rank curent population based on fitness
            selection_results = self.selection(ranked_population) # Select the parents for mating_pool
            mating_pool = self.mating_pool(population, selection_results) # Create the mating pool
            children = self.breed_population(mating_pool) # Crossover for the children
            population = self.mutate_population(children, mutation_rate=0.01) # Mutation for the children

            progress.append(1 / ranked_population[0][1]) # Append new progress from inverse
        # Get the best route of the final population
        best_route_index = self.rank_routes(population)[0][0]
        best_route = population[best_route_index]

        return best_route, progress

# Create N cities within a 200-by-200 plane
def main(N=25, population_size=20, generations=500):
    # Set a fixed random seed for reproducibility
    random.seed(42)

    # Create a list of N cities within a 200-by-200 plane
    city_list = [City(x=int(random.random() * 200), y=int(random.random() * 200)) for _ in range(N)]

    # Create a GA instance and run
    ga = GeneticAlgo(city_list, population_size, generations)
    best_route, progress = ga.run()

    print("Best Route:", best_route)
    print("Total Distance:", Fitness(best_route).route_distance())

    # Plot 
    plt.plot(progress)
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.show()

if __name__ == "__main__":
    main()

from BinaryGene import BinaryGene;
import random;
population_size = 10
gene_len = 10
epoch = 50
mutation = 1
population_obj = []
offspring_obj = []
val = 2
temp_holder = BinaryGene()


def crossover():
    global population_obj
    global gene_len
    #loop population
    for i in range(len(population_obj)):
        #declare variables
        fitness = fitness_two = 0
        rand = random.random()
        #modulo to gather two parents
        if i % 2 is 1 and rand > 0:
            #calculate point of crossover for gene
            crossover_val = random.randrange(0, gene_len);
            #place both parents in temp arrays and update population genes values with temp genes after crossover
            for j in range(gene_len):
                if j >= crossover_val:
                    temp_1 = population_obj[i].get_gene_value()[j]
                    temp_2 = population_obj[i - 1].get_gene_value()[j]
                    population_obj[i].update_gene(j, temp_2)
                    population_obj[i - 1].update_gene(j, temp_1)
            #calculate fitness
            for j in range(gene_len):
                fitness =  fitness_func(population_obj[i].get_gene_value())
                fitness_two = fitness_func(population_obj[i - 1].get_gene_value())
            #set fitness for both population genes after crossover
            population_obj[i].set_fitness(fitness)
            population_obj[i - 1].set_fitness(fitness_two)


def mutation():
    global population_obj
    for i in range(len(population_obj)):
        #set variables
        #if random below threshold loop gene at population index and create tempory gene
        for k in range(len(population_obj[i].get_gene_value())):
            rand = random.random()
        #get random point in gene to mutate and flip bit
            if rand < 0.01:
                if population_obj[i].get_gene_value()[k] is 1:
                    population_obj[i].update_gene(k, 0)
                else:
                    population_obj[i].update_gene(k, 1)
        #update population gene with temp gene values and calculate new fitness
        fitness = fitness_func(population_obj[i].get_gene_value())
        population_obj[i].set_fitness(fitness)


def tournament_selection(pop_size):
    global offspring_obj
    global population_obj
    for i in range(pop_size):
        offspring_obj.pop()
    #select to random parents from population
    for i in range(pop_size):
        parent_one = random.randrange(0, pop_size)
        parent_two = random.randrange(0, pop_size)
        #find parent with highest fitness value and add to offspring pool
        if population_obj[parent_one].get_fitness() > population_obj[parent_two].get_fitness():
            offspring_obj.append(population_obj[parent_one])
        else:
            offspring_obj.append(population_obj[parent_two])
    #after population size iterations replace population pool with the new offspring
    for i in range(pop_size):
        population_obj[i] = offspring_obj[i]


#def sqr(n):
#    n = n * n
#    return n


def fitness_func(val):
    fitness = 0
    for i in range(len(val)):
        if val[i] is 1:
            fitness = fitness + 1
    return fitness


def overall_fitness():
    global population_obj
    global population_size
    summ = 0
    maxx = 0
    for i in range(len(population_obj)):
        summ = summ + population_obj[i].get_fitness()
        if population_obj[i].get_fitness() > maxx:
            maxx = population_obj[i].get_fitness()
    meann = summ / population_size
    return summ, meann, maxx

#initilize population
for i in range(population_size):
    p = BinaryGene();
    for j in range(gene_len):
        val = random.randrange(0, 2)
        p.set_gene_value(val)
    fitness = fitness_func(p.get_gene_value())
    p.set_fitness(fitness)
    population_obj.append(p)
    offspring_obj.append(p)


best = 0
for i in range(epoch):
    #initilize variables
    sum = mean = max = 0
    sum, mean, max = overall_fitness()

    #print mean, sum and max for population
    #print("Sum: " + str(sum))
    print("Mean: " + str(mean))
    print("Max: " + str(max))
    print("------------")
    print("Generation " + str(i + 1))

    for j in range(population_size):
        print(str(j) + ": Population " + str(population_obj[j].get_gene_value()) + str(population_obj[j].get_fitness()))
    #select random mating pool
    tournament_selection(population_size)
    #shuffle mating pool
    random.shuffle(population_obj)
    #crossover all parents in mating pool to gather offspring for new population
    crossover()
    #muta selected genes
    mutation()


    #find best and worst chromosomes and replace worst with best to maintain best solution found in all mating pools
    #for j in range(population_size):
    #    if population_obj[j].get_fitness() >= best:
    #        best_gene = population_obj[j].get_gene_value().copy()
    #        temp = j
    #        best = population_obj[j].get_fitness()
    #worst = best
    #for j in range(population_size):
    #    if population_obj[j].get_fitness() < worst:
    #        worst = population_obj[j].get_fitness()

    #for j in range(population_size):
     #   if population_obj[j].get_fitness() is worst:
      #      for k in range(gene_len):
       #         population_obj[j].update_gene(k, best_gene[k])
        #        population_obj[j].set_fitness(best)
















    #print(population_obj[temp_two].get_gene_value())
    #for j in range(population_size):
     #   print(str(j) + ": population " + str(population_obj[j].get_gene_value()) + str(population_obj[j].get_fitness()))

 #fitness = fitness + (fitness_var * val);
    #fitness_var = fitness_var * 2;
    #return fitness, fitness_var




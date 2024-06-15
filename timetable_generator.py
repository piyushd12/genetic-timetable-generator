import random
from tabulate import tabulate

# Constants
NUM_SUBJECTS = 5
NUM_LABS = 5
NUM_DAYS = 5
SLOTS_PER_DAY = 6  
SUBJECTS = ["EM", "OS", "CNND", "COA", "AT"]
LABS = ["Maths Tutorial", "Unix Lab", "Python Lab", "Networking Lab", "Microprocessor Lab"]

# Constraint parameters
SUBJECT_SLOTS_PER_WEEK = 3
LAB_SLOTS_PER_WEEK = {"Maths Tutorial": 1, "Unix Lab": 1, "Python Lab": 4, "Networking Lab": 1, "Microprocessor Lab": 1}

# Generate initial population
def generate_population(pop_size):
    population = []
    for _ in range(pop_size):
        chromosome = []
        for day in range(NUM_DAYS):
            day_labs = random.sample(LABS, min(1, len(LABS)))  # Select one lab randomly for the day
            if len(day_labs) < 1:
                continue  # Ensures at least one lab is selected for the day
            chosen_lab = day_labs[0]
            for slot in range(SLOTS_PER_DAY):
                if slot < 2:
                    chromosome.append(chosen_lab)
                else:
                    chromosome.append(random.choice(SUBJECTS))
        population.append(chromosome)
    return population

# Fitness function
def calculate_fitness(chromosome):
    fitness = 0
    subject_counts = {subject: 0 for subject in SUBJECTS}
    lab_counts = {lab: 0 for lab in LABS}
    python_lab_count = 0

    for slot in chromosome:
        if slot in SUBJECTS:
            subject_counts[slot] += 1
            if subject_counts[slot] <= SUBJECT_SLOTS_PER_WEEK:
                fitness += 1
        elif slot == "Python Lab":
            python_lab_count += 1
            if python_lab_count <= LAB_SLOTS_PER_WEEK["Python Lab"]:
                fitness += 1
        else:
            lab_counts[slot] += 1
            if lab_counts[slot] * 2 <= LAB_SLOTS_PER_WEEK[slot]:  # Adjust for lab slots
                fitness += 1

    # Penalties for not meeting compulsory lecture counts
    subject_penalty = sum(max(0, count - SUBJECT_SLOTS_PER_WEEK) for count in subject_counts.values())
    lab_penalty = sum(max(0, count - (LAB_SLOTS_PER_WEEK[lab] * 2)) for lab, count in lab_counts.items())
    python_lab_penalty = max(0, python_lab_count - LAB_SLOTS_PER_WEEK["Python Lab"])

    # Penalty for not meeting lecture frequency
    lecture_frequency_penalty = sum(abs(count - 3) if count < 3 else abs(count - 4) for count in subject_counts.values())
    fitness -= subject_penalty + lab_penalty + python_lab_penalty + lecture_frequency_penalty
    return fitness

# Crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation
def mutate(chromosome, mutation_rate):
    for day in range(NUM_DAYS):
        day_start_index = day * SLOTS_PER_DAY
        if random.random() < mutation_rate:
            chosen_lab = random.choice(LABS)
            chromosome[day_start_index] = chosen_lab
            chromosome[day_start_index + 1] = chosen_lab
    return chromosome

# Genetic algorithm
def genetic_algorithm(population_size, generations, mutation_rate):
    population = generate_population(population_size)

    for generation in range(generations):
        population = sorted(population, key=lambda x: calculate_fitness(x), reverse=True)

        # Crossover
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = random.choices(population[:population_size // 2], k=2)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([child1, child2])

        # Mutation
        new_population = [mutate(chromosome, mutation_rate) for chromosome in new_population]

        population = new_population

    # Return the fittest timetable
    return max(population, key=lambda x: calculate_fitness(x))

def print_timetable(timetable):
    table_data = []
    for day in range(NUM_DAYS):
        day_schedule = []
        for slot in range(SLOTS_PER_DAY):
            day_schedule.append(timetable[day * SLOTS_PER_DAY + slot])
        table_data.append(day_schedule)
    
    headers = [f"Slot {i+1}" for i in range(SLOTS_PER_DAY)]
    days = [f"Day {i+1}" for i in range(NUM_DAYS)]
    print(tabulate(table_data, headers=headers, showindex=days, tablefmt="grid"))

if __name__ == "__main__":
    population_size = 100
    generations = 100
    mutation_rate = 0.01

    timetable = genetic_algorithm(population_size, generations, mutation_rate)
    print("Generated Timetable:")
    print_timetable(timetable)

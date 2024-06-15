# Timetable Generation using Genetic Algorithm

## Overview

This project generates an optimized classroom timetable using a genetic algorithm. It takes into account various constraints such as the number of subjects, labs, days, and slots per day to produce a timetable that maximizes the efficient allocation of classes and labs.

### Key Features

- **Genetic Algorithm:** EUtilizes crossover and mutation to evolve the population of timetables over generations.
- **Constraint Handling:**  Ensures subjects and labs are scheduled according to predefined constraints.
- **Fitness Function:** Measures the suitability of each timetable based on the allocation of subjects and labs.
- **User-Friendly Output:** Prints the generated timetable in a tabulated format.

## Genetic Algorithms (GAs)

In the pursuit of solving complex optimization problems across various domains, researchers and practitioners have turned to nature-inspired computational methods. Among these, genetic algorithms (GAs) stand out as powerful tools that draw inspiration from the principles of natural selection and genetics.

These algorithms mimic the process of natural evolution, where solutions to problems are iteratively improved over generations. By selecting the fittest individuals, combining their traits through crossover, and introducing variations via mutation, genetic algorithms navigate solution spaces to find optimal or near-optimal solutions.

Researchers and practitioners alike have embraced genetic algorithms for their ability to tackle complex problems characterized by large search spaces, non-linearity, and multi-modality. In engineering, genetic algorithms are employed for design optimization, scheduling, and control systems. In finance, they aid in portfolio optimization and trading strategies. In bioinformatics, genetic algorithms assist in sequence alignment, protein folding, and drug discovery.

## Requirements

- Python 3.x
- Tabulate library

## Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/piyushd12/genetic-timetable-generator.git
   cd genetic-timetable-generator

2. **Install the required Python packages:**
   ```sh
   pip install tabulate

## Usage

1. **Run the script:**
   ```sh
   python timetable_generator.py

2. **Generated Timeteable:**
   The script will output the generated timetable in a tabulated format.

## Code Explanation

**Constants**

- **NUM_SUBJECTS:** Number of subjects.
- **NUM_LABS:** Number of labs.
- **NUM_DAYS:** Number of days in a week.
- **SLOTS_PER_DAY:** Number of slots per day.
- **SUBJECTS:** List of subject names.
- **LABS:** List of lab names.
- **SUBJECT_SLOTS_PER_WEEK:** Slots per week for each subject.
- **LAB_SLOTS_PER_WEEK:** Slots per week for each lab.

**Functions**

- **generate_population(pop_size):** Generates an initial population of timetables.
- **calculate_fitness(chromosome):** Calculates the fitness of a timetable based on constraints.
- **crossover(parent1, parent2):** Performs crossover between two parent timetables to produce offspring.
- **mutate(chromosome, mutation_rate):** Mutates a timetable with a given mutation rate.
- **genetic_algorithm(population_size, generations, mutation_rate):** Runs the genetic algorithm to generate an optimized timetable.
- **print_timetable(timetable):** Prints the timetable in a tabulated format.

**License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


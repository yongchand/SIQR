# Original code by Steve Adolph, with mods by Eliot Bush.
# Overall code rewritten and modifided by Chan Hong.
import random
import matplotlib.pyplot as plt


def create_initial_population(pop_size, initial_infected=100):
    """
    Create a starting population with a specified number of infected individuals.
    """
    population = ['I'] * initial_infected + ['S'] * (pop_size - initial_infected)
    random.shuffle(population)
    return population


def update_quarantine_status(quarantine_status, num_quarantine_days):
    """
    Update the quarantine status of individuals in the population.
    """
    for person in list(quarantine_status):
        quarantine_status[person] += 1
        if quarantine_status[person] >= num_quarantine_days:
            del quarantine_status[person]


def simulate_day(population, pop_size, prob_infected_recovery, prob_quarantine_recovery,
                num_contacts, prob_infection, quarantine_status, num_quarantine_days, prob_quarantine):
    """
    Simulate the events of a day in the SIQR model.
    """
    for person in range(pop_size):
        update_quarantine_status(quarantine_status, num_quarantine_days)
        status = population[person]
        if status == 'I':
            if random.random() < prob_quarantine:
                quarantine_status[person] = 0
                population[person] = 'Q'
            elif random.random() < prob_infected_recovery:
                population[person] = 'R'

        elif status == 'Q':
            if random.random() < prob_quarantine_recovery:
                population[person] = 'R'

        elif status == 'S':
            rest_of_poplation = population[:person] + population[person+1:]
            rest_of_poplation = [p for p in rest_of_poplation if p != "Q"]
            contacts = random.sample(rest_of_poplation, num_contacts)
            for other_person in contacts:
                if other_person == 'I':
                    if random.random() < prob_infection:
                        population[person] = 'E'

    # Update Exposed to Infected
    population = ['I' if status == 'E' else status for status in population]

    return population


def outbreak(pop_size, num_days, prob_infected_recovery, prob_quarantine_recovery,
            num_contacts, prob_infection, num_quarantine_days, prob_quarantine):
    """
    Simulate an outbreak over a period of days.
    """
    population = create_initial_population(pop_size)
    infected_count = [population.count('I') + population.count('Q')]
    quarantine_status = {}

    for day in range(1, num_days + 1):
        population = simulate_day(population, pop_size, prob_infected_recovery,
                                  prob_quarantine_recovery, num_contacts, prob_infection,
                                  quarantine_status, num_quarantine_days, prob_quarantine)
        infected_count.append(population.count('I') + population.count('Q'))
        print("Day: ", day)

    return infected_count, population

def main():
    # Parameters
    pop_size = 10000
    num_contacts = 20
    prob_infection = 0.01
    prob_quarantine = 0.1
    prob_infected_recovery = 0.133333
    prob_quarantine_recovery = 0.133333
    num_days = 300
    num_quarantine_days = 14

    # Running the simulation
    infected_count, final_population = outbreak(pop_size, num_days, prob_infected_recovery,
                                                prob_quarantine_recovery, num_contacts,
                                                prob_infection, num_quarantine_days, prob_quarantine)

    # Results
    max_infected = max(infected_count)
    print("Maximum number infected: ", max_infected)
    print("Day of max. number infected: ", infected_count.index(max_infected))
    print("Final number infected then recovered: ",
        final_population.count('R')+final_population.count('Q'))
    print("R0 = ", num_contacts * prob_infection / prob_infected_recovery)

    # Plotting
    plt.plot(range(num_days+1), infected_count)
    plt.xlabel('Days')
    plt.ylabel('Number of infections')
    plt.ylim(0, max(infected_count) + 100)
    plt.title('SIR Model Simulation of Infection Spread')
    plt.show()

if __name__ == "__main__":
    main()

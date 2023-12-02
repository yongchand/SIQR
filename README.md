# SIQR

The SIQR repository is a computational simulation for the SIQR model, which expands upon the SIR model by incorporating quarantine considerations.

The simulation represents a closed model that does not account for birth or death. Each susceptible individual will have contact with `num_contacts` others per day and may become infected with a certain probability. However, quarantined individuals, who have already been diagnosed as infected, cannot come into contact with susceptibles.

Each simulation will have the following parameters:

```python
pop_size = 10000 # Total population size.
num_contacts = 20 # Number of susceptible individuals contacted per day.
prob_infection = 0.01 # Probability that a susceptible individual gets infected.
prob_quarantine = 0.1 # Probability for an infected individual to be quarantined.
prob_infected_recovery = 0.133333 # Probability for an infected individual to recover.
prob_quarantine_recovery = 0.133333 # Probability for a quarantined individual to recover.
num_days = 300 # Number of simulation days.
num_quarantine_days = 14 # Number of days a quarantined individual persists. They will be freed to the infected category after completion.
initial_infected = 100 # Embedded as the default.
```

To run the simulation, simply execute the Python file. After completion, a pyplot visualization will be displayed.

```bash
python siqr.py
```

Feel free to use this version or make further adjustments according to your preferences.
import random
import time
import matplotlib.pyplot as plt

def generate_random_program(max_length=10):
    """Generates a random program with operations from a simple set."""
    operations = ['inc', 'dec', 'jmp', 'halt']
    return [random.choice(operations) for _ in range(random.randint(1, max_length))]

def simulate_program(program, time_limit=0.00003125):  # time_limit set to approximately 31.25 microseconds
    pc = 0  # Program counter
    acc = 0  # Accumulator for operations
    start_time = time.time()  # Record the start time of the simulation

    while True:
        if time.time() - start_time > time_limit:
            return False  # Terminate as non-halting if time limit exceeded

        if pc >= len(program):
            return False  # End of program reached without halting

        op = program[pc]
        if op == 'inc':
            acc += 1
        elif op == 'dec':
            acc -= 1
        elif op == 'jmp':
            if acc != 0:  # Jump only if accumulator is not zero
                pc = (pc + acc) % len(program)  # Simple jump logic, wraps around
                continue
        elif op == 'halt':
            if acc == 0:  # Only halt if accumulator is zero
                return True

        pc += 1

def run_monte_carlo(num_simulations=100, num_programs=1000):
    omega_values = []
    for _ in range(num_simulations):
        halt_count = 0
        for _ in range(num_programs):
            program = generate_random_program()
            if simulate_program(program):
                halt_count += 1
        omega = halt_count / num_programs
        omega_values.append(omega)
    return omega_values

def main():
    num_simulations = 100  # Number of Monte Carlo simulations
    omega_values = run_monte_carlo(num_simulations)
    
    # Plotting the histogram of omega values
    plt.hist(omega_values, bins=10, color='blue', edgecolor='black')
    plt.title('Histogram of Ω Values')
    plt.xlabel('Ω Value')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == "__main__":
    main()
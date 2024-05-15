import random
import time

def generate_random_program(max_length=10):
    """Generates a random program with operations from a simple set."""
    operations = ['inc', 'dec', 'jmp', 'halt']
    return [random.choice(operations) for _ in range(random.randint(1, max_length))]

def simulate_program(program, time_limit=0.00003125):  # time_limit set to 500 milliseconds
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

def main(num_programs=1000):
    halt_count = 0
    milestones = [10, 50, 100, 500, 1000]  # Define milestones
    for i in range(1, num_programs + 1):
        program = generate_random_program()
        if simulate_program(program):
            halt_count += 1
        if i in milestones:  # Check if the current program count is a milestone
            print(f"Milestone reached: {i} programs processed. Halting count: {halt_count}")
    
    omega_approx = halt_count / num_programs
    print(f"Approximation of Ω for this model: {omega_approx}")

if __name__ == "__main__":
    main()
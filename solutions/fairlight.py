
import angr
import sys
import claripy


def main(argv):
    path_to_binary = argv[1]
    project = angr.Project(path_to_binary)

    password0_size_in_bits = 14*8
    password0 = claripy.BVS('password0', password0_size_in_bits)

    initial_state = project.factory.entry_state(args=["./fairlight", password0],
                                                add_options={angr.options.SYMBOL_FILL_UNCONSTRAINED_MEMORY,
                                                             angr.options.SYMBOL_FILL_UNCONSTRAINED_REGISTERS}
                                                )

    simulation = project.factory.simgr(initial_state)

    # Define a function that checks if you have found the state you are looking
    # for.
    def is_successful(state):
        # Dump whatever has been printed out by the binary so far into a string.
        stdout_output = state.posix.dumps(sys.stdout.fileno())

        # Return whether 'Good Job.' has been printed yet.
        # (!)
        return "OK - ACCESS GRANTED: CODE".encode() in stdout_output  # :boolean

    # Same as above, but this time check if the state should abort. If you return
    # False, Angr will continue to step the state. In this specific challenge, the
    # only time at which you will know you should abort is when the program prints
    # "Try again."
    def should_abort(state):
        stdout_output = state.posix.dumps(sys.stdout.fileno())
        return "NOPE - ACCESS DENIED!".encode() in stdout_output  # :boolean

    # Tell Angr to explore the binary and find any state that is_successful identfies
    # as a successful state by returning True.
    simulation.explore(find=is_successful, avoid=should_abort)

    if simulation.found:
        solution_state = simulation.found[0]
        solution = solution_state.solver.eval(password0, cast_to=bytes).decode()
        print(solution)
    else:
        raise Exception('Could not find the solution')


if __name__ == '__main__':
    main(sys.argv)

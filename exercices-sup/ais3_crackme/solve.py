#!/usr/bin/env python


'''
ais3_crackme has been developed by Tyler Nighswander (tylerni7) for ais3.

It is an easy crackme challenge. It checks the command line argument.
'''

import angr
import claripy


def main():
    exec_path = ???
    project = angr.Project(exec_path, auto_load_libs=False)

    # create an initial state with necessary setup
    ...
    initial_state = project.factory.entry_state(???)

    # create a path group using the created initial state
    sm = project.factory.simulation_manager(initial_state)

    # symbolically execute the program until we reach the wanted value of the instruction pointer
    valid_path_address = ???  # at this instruction the binary will print(the "correct" message)
    sm.explore(find=valid_path_address)

    found = sm.found[0]
    # ask to the symbolic solver to get the value of the secret key in the reached state as a string
    solution = found.solver.eval(argv1, cast_to=bytes)

    solution = solution[:solution.find(b"\x00")]
    return solution


if __name__ == '__main__':
    print(repr(main()))

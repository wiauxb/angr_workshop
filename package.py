#!/usr/bin/env python3
import datetime
import os
import sys
import shutil


def level_generate_module(level_path):
    module_name = level_path.replace("/", ".")
    level_name = module_name.split(".")[-1]
    return getattr(__import__(module_name + ".generate"), level_name)


def package_level(level_name, output_base_directory, num_binaries, user, salt, extra_files):
    seed = level_name + user + salt
    generate_module = level_generate_module(level_name)
    output_directory = output_base_directory
    binary_file_output_prefix = os.path.join(output_directory, level_name)
    suffix_format_str = '{:0' + str(len(str(num_binaries - 1))) + '}' if (num_binaries - 1 > 0) else ''

    directory = os.path.dirname(level_name)

    if not os.path.exists(os.path.join(output_directory, directory)):
        os.makedirs(os.path.join(output_directory, directory))

    for i in range(num_binaries):
        suffix = suffix_format_str.format(i)
        binary_file_output = binary_file_output_prefix + suffix
        generate_module.generate.generate([None, seed, binary_file_output])

    for extra_file in extra_files:
        extra_file_abs = os.path.join('.', level_name, extra_file)
        extra_file_target = os.path.join(output_base_directory, directory, extra_file)
        shutil.copyfile(extra_file_abs, extra_file_target)
    name_candidates = user.split('/')
    if len(name_candidates) >= 2:
        name = name_candidates[-2]
    else:
        name = name_candidates[-1]
    print('Compiled %s for user %s.' % (level_name, name))


def get_path(package_name: str):
    prepend = "exercices"
    return os.path.join(prepend, package_name)


def package_exercices(root_folder):
    num_binaries = 1
    year = str(datetime.datetime.now().year)
    package_level(get_path('02_angr_find_condition'), root_folder,
                  num_binaries, root_folder, year, ['scaffold02.py'])
    package_level(get_path('03_angr_symbolic_registers'), root_folder,
                  num_binaries, root_folder, year, ['scaffold03.py'])
    package_level(get_path('08_angr_constraints'), root_folder,
                  num_binaries, root_folder, year, ['scaffold08.py'])
    package_level(get_path('09_angr_hooks'), root_folder, num_binaries, root_folder, year, ['scaffold09.py'])
    package_level(get_path('10_angr_simprocedures'), root_folder,
                  num_binaries, root_folder, year, ['scaffold10.py'])


def package_exercices_sup(root_folder):
    num_binaries = 1
    year = str(datetime.datetime.now().year)
    package_level(os.path.join("exercices-sup", '06_angr_symbolic_dynamic_memory'), root_folder,
                  num_binaries, root_folder, year, ['scaffold06.py'])


def package_all(root_folder):
    package_exercices(root_folder)
    package_exercices_sup(root_folder)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python package.py [base_directory]')
        sys.exit()

    if not os.path.exists(sys.argv[1]):
        os.makedirs(sys.argv[1])
    package_all(sys.argv[1])

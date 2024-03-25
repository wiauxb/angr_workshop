#!/usr/bin/env python3
import os
import sys
import shutil

exos = ["ais3_crackme", "fairlight"]


def copy_to(path):
    for exo in exos:
        dest_dir = os.path.join(path, exo)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Iterate over files in the source directory
        for filename in os.listdir(exo):
            src_file = os.path.join(exo, filename)
            dest_file = os.path.join(dest_dir, filename)

            # Check if the current item is a file
            if os.path.isfile(src_file):
                # Copy the file to the destination directory
                shutil.copy2(src_file, dest_file)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python extern.py [base_directory]')
        sys.exit()

    if not os.path.exists(sys.argv[1]):
        os.makedirs(sys.argv[1])
    copy_to(sys.argv[1])

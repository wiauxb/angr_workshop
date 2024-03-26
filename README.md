# Angr Workshop - CyberExcellence
This repository contains all necessery material for an Angr introduction workshop 

---

A Makefile is included that performs an automated build for installation.

A list of users is passed in via the `USERS` environment variable, which will then build the binaries for each user listed.

## Setup
### Install Ghidra
To install an official pre-built multi-platform Ghidra release:  
* Install [JDK 17 64-bit](https://adoptium.net/temurin/releases)
* Download a Ghidra [release file](https://github.com/NationalSecurityAgency/ghidra/releases)
  - **NOTE:** The official multi-platform release file is named 
    `ghidra_<version>_<release>_<date>.zip` which can be found under the "Assets" drop-down.
    Downloading either of the files named "Source Code" is not correct for this step.
* Extract the Ghidra release file
* Launch Ghidra: `./ghidraRun` (or `ghidraRun.bat` for Windows)
### Or for the nerdy nerds
Every thing we do with Ghidra is identifying adresses. So if you are confortable with assembly and that you like to live in your good old terminal then you can just use `objdump`.

I advise you
```console
objdump -D <binary_path> --disassembler-color=color | less
```
or to look for symbols (strings etc)
```console
objdump -s <binary_path> | less
```

### Building the exercices
The `make` command will build all the necessary binaries and put all the exercices template in `obj/<username>/angr`

  ```make USERS='<username>' local```

You can then go to the target directory (`obj/<username>/angr`), you'll find the built binaries as well as the python files to play the levels

## Troubleshooting
While compiling using "`make USERS=<user> local`" you might have the following error: <br>
`fatal error: bits/libc-header-start.h: No such file or directory`

One easy fix is to install the missing headers and libraries using: <br>
  ```sudo apt-get install gcc-multilib```

---

## Solutions
The solutions of the exercices can be found in `solutions.zip` with password: `4ngr2024`.

* NOTE: the addresses used in the solutions could differ from those compiled on your computer.

Eventually, this README will have complete and more detailed information about building, installing, and playing the levels.

Currently, if you want to play around with them, take a look at `package.py`, which builds the levels, and `dist/` which generally has an up-to-date build of each of the levels.

A Makefile is included that performs an automated build for both a local installation and for the MetaCTF web installation.
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

### Building the course
Build binaries in `obj/{foo,bar}/angr`: <br>
  ```make USERS='foo bar' local```

* You can go to the target directory (`obj/{foo,bar}/angr`), you'll find the built binaries as well as the python files to play the levels

## Troubleshooting
While compiling using "`make USERS=<user> local`" you might have the following error: <br>
`fatal error: bits/libc-header-start.h: No such file or directory`

One easy fix is to install the missing headers and libraries using: <br>
  ```sudo apt-get install gcc-multilib```


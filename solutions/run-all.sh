#!/bin/bash
# Binaries generated via python package.py obj/wuchang/angr
echo "Solving all of the levels... This could take a while."
ANGR_OUT_02="$(python3 02_angr_find_condition/solve02.py 02_angr_find_condition/02_angr_find_condition 2> /dev/null)"
echo -n "."
ANGR_OUT_03="$(python3 03_angr_symbolic_registers/solve03.py 03_angr_symbolic_registers/03_angr_symbolic_registers 2> /dev/null)"
echo -n "."
ANGR_OUT_06="$(python3 06_angr_symbolic_dynamic_memory/solve06.py 06_angr_symbolic_dynamic_memory/06_angr_symbolic_dynamic_memory 2> /dev/null)"
echo -n "."
ANGR_OUT_08="$(python3 08_angr_constraints/solve08.py 08_angr_constraints/08_angr_constraints 2> /dev/null)"
echo -n "."
ANGR_OUT_09="$(python3 09_angr_hooks/solve09.py 09_angr_hooks/09_angr_hooks 2> /dev/null)"
echo -n "."
ANGR_OUT_10="$(python3 10_angr_simprocedures/solve10.py 10_angr_simprocedures/10_angr_simprocedures 2> /dev/null)"
echo -n "."
echo ""
echo "-- Solutions --"
echo "02: $ANGR_OUT_02"
echo $ANGR_OUT_02 | 02_angr_find_condition/02_angr_find_condition
echo "03: $ANGR_OUT_03"
echo $ANGR_OUT_03 | 03_angr_symbolic_registers/03_angr_symbolic_registers
echo "06: $ANGR_OUT_06"
echo $ANGR_OUT_06 | 06_angr_symbolic_dynamic_memory/06_angr_symbolic_dynamic_memory
echo "08: $ANGR_OUT_08"
echo $ANGR_OUT_08 | 08_angr_constraints/08_angr_constraints
echo "09: $ANGR_OUT_09"
echo $ANGR_OUT_09 | 09_angr_hooks/09_angr_hooks
echo "10: $ANGR_OUT_10"
echo $ANGR_OUT_10 | 10_angr_simprocedures/10_angr_simprocedures

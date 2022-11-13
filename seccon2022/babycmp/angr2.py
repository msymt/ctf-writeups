"""
src: https://mopisec.hatenablog.com/entry/2022/11/13/213220#babycmp-176-solves
"""

import angr
import claripy

EXEC_NAME = './chall.baby'
FLAG_ADDR = 0x4012CC # puts("Correct!");

p = angr.Project(EXEC_NAME, load_options={"auto_load_libs": False})

argv1 = claripy.BVS("argv1", 100*8)
state = p.factory.entry_state(args=[EXEC_NAME, argv1])

simgr = p.factory.simulation_manager(state)
simgr.explore(find=FLAG_ADDR)

try:
    found = simgr.found[0]
    solution = found.solver.eval(argv1, cast_to=bytes)
    flag = solution[:solution.find(b"\x00")].decode()
    print(flag)
except IndexError:
    print("Something went wrong :(")
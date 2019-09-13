#!/usr/bin/python3

# import /Include/opcode.h

def magic_calculation(a, b):
    bytecode = dis.Bytecode(magic_calculation(a, b))
    for instr in bytecode:
        print(instr.opname)

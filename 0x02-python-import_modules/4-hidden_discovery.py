#!/usr/bin/python3
import dis
# import marshal
import hidden_4

# marshal.load(hidden_4)

# dis.dis(hidden_4)
# bytecode = dis.Bytecode(hidden_4)
# for instr in bytecode:
#     print(instr.opname)

dis.show_code(hidden_4)

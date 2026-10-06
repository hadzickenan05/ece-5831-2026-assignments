import logic_gate as lg

logic_gate = lg.LogicGate()

print("AND Gate Output:")
print(logic_gate.and_gate(0,0))
print(logic_gate.and_gate(0,1))
print(logic_gate.and_gate(1,0))
print(logic_gate.and_gate(1,1))

print(" ")

print("OR Gate Output:")
print(logic_gate.or_gate(0,0))
print(logic_gate.or_gate(0,1))
print(logic_gate.or_gate(1,0))
print(logic_gate.or_gate(1,1))

print(" ")

print("NAND Gate Output:")
print(logic_gate.nand_gate(0,0))
print(logic_gate.nand_gate(0,1))
print(logic_gate.nand_gate(1,0))
print(logic_gate.nand_gate(1,1))

print(" ")

print("NOR Gate Output:")
print(logic_gate.nor_gate(0,0))
print(logic_gate.nor_gate(0,1))
print(logic_gate.nor_gate(1,0))
print(logic_gate.nor_gate(1,1))

print(" ")

print("XOR Gate Output:")
print(logic_gate.xor_gate(0,0))
print(logic_gate.xor_gate(0,1))
print(logic_gate.xor_gate(1,0))
print(logic_gate.xor_gate(1,1))
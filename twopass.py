SYMBOL_TABLE = {}  # Symbol table to store labels and their addresses
MEMORY = []  # Memory to store machine code
PC = 0  # Program counter

def pass_one(assembly_code):
    global PC
    tokens = assembly_code.split()
    for token in tokens:
        if token.endswith(":"):  # Label definition
            label = token[:-1]
            SYMBOL_TABLE[label] = PC
        else:  # Instruction
            MEMORY.append(token)
            PC += 1

def resolve_symbols():
    global MEMORY
    for i, instruction in enumerate(MEMORY):
        if instruction in SYMBOL_TABLE:
            MEMORY[i] = str(SYMBOL_TABLE[instruction])

def assemble(assembly_code):
    pass_one(assembly_code)
    resolve_symbols()
    print("Opcode Table:")
    print(SYMBOL_TABLE)
    print("Machine Code:")
    print(MEMORY)

# Example assembly code
assembly_code = """
START: MOV A, B
ADD C
JMP END
LOOP: SUB D
JNZ LOOP
END: HLT
"""

assemble(assembly_code)

class MacroProcessor:
    def __init__(self):
        self.MNT = {}  # Macro Name Table
        self.MDT = []  # Macro Definition Table
        self.ALA = {}  # Argument List Array

    def pass1(self, source_code):
        macro_definition = []
        for line in source_code:
            if line.startswith("MACRO"):
                macro_name = line.split()[1]
                self.MNT[macro_name] = len(self.MDT)
                macro_definition = [line]
            elif macro_definition and not line.startswith("MEND"):
                macro_definition.append(line)
            elif macro_definition and line.startswith("MEND"):
                macro_definition.append(line)
                self.MDT.extend(macro_definition)
                macro_definition = []

    def pass2(self, source_code):
        for line in source_code:
            words = line.split()
            if words[0] in self.MNT:
                mdtp = self.MNT[words[0]]
                macro_definition = self.MDT[mdtp:]
                self.expand_macro(macro_definition)

    def expand_macro(self, macro_definition):
        mdtp = 0
        ala = {}
        while mdtp < len(macro_definition):
            line = macro_definition[mdtp]
            words = line.split()
            if words[0] == "MACRO":
                mdtp += 1
                continue
            elif words[0] == "MEND":
                break
            else:
                mdtp += 1
                expanded_line = self.substitute_arguments(line, ala)
                print(expanded_line)

    def substitute_arguments(self, line, ala):
        words = line.split()
        for i in range(len(words)):
            if words[i] in ala:
                words[i] = ala[words[i]]
        return ' '.join(words)

# Example usage
source_code = [
    "MACRO ADD A, B",
    "LOAD A",
    "ADD B",
    "STORE A",
    "MEND",
    "ADD X, Y",
    "MACRO CALL ADD X, Y",
    "END"
]
processor = MacroProcessor()
processor.pass1(source_code)
processor.pass2(source_code)

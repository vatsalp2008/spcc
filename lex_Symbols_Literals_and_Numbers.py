import re

def lexical_analyzer_symbols_literals_numbers(input_text):
    tokens = []  # List to store tokens

    # Regular expression patterns for symbols, literals, and numbers
    symbol_pattern = r'[^\w\s]'
    literal_pattern = r"'[^']*'|\"[^\"]*\""
    number_pattern = r'\b\d+\b'

    # Tokenize the input text
    for token in re.findall(symbol_pattern + '|' + literal_pattern + '|' + number_pattern, input_text):
        if re.match(symbol_pattern, token):
            tokens.append((token, "Symbol"))
        elif re.match(literal_pattern, token):
            tokens.append((token, "Literal"))
        elif re.match(number_pattern, token):
            tokens.append((token, "Number"))

    return tokens

# Example usage
input_text = "int x = 10; float y = 3.14; char c = 'a';"
tokens = lexical_analyzer_symbols_literals_numbers(input_text)
for token in tokens:
    print(token)

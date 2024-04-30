import re

def lexical_analyzer_keywords_identifiers(input_text):
    keywords = {'if', 'else', 'while', 'for', 'return'}  # Set of keywords
    tokens = []  # List to store tokens

    # Regular expression pattern for identifying identifiers
    identifier_pattern = r'[a-zA-Z_]\w*'

    # Tokenize the input text
    for token in re.findall(identifier_pattern, input_text):
        if token in keywords:
            tokens.append((token, "Keyword"))
        else:
            tokens.append((token, "Identifier"))

    return tokens

# Example usage
input_text = "if (x > 0) { return x; } else { return y; }"
tokens = lexical_analyzer_keywords_identifiers(input_text)
for token in tokens:
    print(token)

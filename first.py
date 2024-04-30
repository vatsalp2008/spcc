def find_first(grammar):
    first = {}
    
    # Function to find first set for a non-terminal symbol
    def find_first_for_symbol(symbol):
        if symbol in first:
            return first[symbol]
        
        first_set = set()
        
        for production in grammar[symbol]:
            first_symbol = production[0]
            
            # If first symbol is a terminal, add it to first set
            if first_symbol.islower() or first_symbol == 'ε':
                first_set.add(first_symbol)
            # If first symbol is a non-terminal, find its first set recursively
            else:
                first_of_first_symbol = find_first_for_symbol(first_symbol)
                first_set.update(first_of_first_symbol)
                
                # If ε is in the first set of first symbol, continue with next symbol in the production
                if 'ε' in first_of_first_symbol:
                    i = 1
                    while i < len(production) and 'ε' in first_of_first_symbol:
                        first_of_next_symbol = find_first_for_symbol(production[i])
                        first_set.update(first_of_next_symbol - {'ε'})
                        first_of_first_symbol = first_of_next_symbol
                        if 'ε' in first_of_first_symbol:
                            i += 1
                    if i == len(production) and 'ε' in first_of_first_symbol:
                        first_set.add('ε')
                
        return first_set
    
    # Iterate over each non-terminal symbol in the grammar
    for symbol in grammar:
        first[symbol] = find_first_for_symbol(symbol)
        
    return first

# Example usage
grammar = {
    'S': [['A', 'B'], ['C', 'a']],
    'A': [['B', 'b'], ['ε']],
    'B': [['d']],
    'C': [['e', 'f']]
}

first_set = find_first(grammar)
for symbol, first in first_set.items():
    print(f"First({symbol}) = {first}")

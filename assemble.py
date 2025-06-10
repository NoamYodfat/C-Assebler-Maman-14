ic = 0
dc = 0
source = open("result.asm")
result = open("binary.o", "w")
symbol_table[10][100] = 

"""
Question how to store a function
"""
def return_in_10_bits(source): 
	int i = 0;
	result = 0;
	for byte in data:
		result = result | (byte << (10 * i))
		i = i + 1;
	return result;
	
bool is_symbol_definition = False;
for line in source:
	first_word = line.split(':')[0]
	if (first_word.isupper()):  
		is_symbol_definition = True
		line = line.split(' ')[1]		
				
	if '.' in line:
		if (is_symbol_definition):
			if ".data" in line: 
				# store data in symbol table

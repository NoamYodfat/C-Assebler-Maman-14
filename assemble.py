
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
	
'''
We are not going to use the "entire" space to represent a number
We are only going to store about 4 bytes total.
We are simply going to use the offset to represent a number
How?

Take the following data:
10000001
10000001

In order to store this data, we would need 3 regular bytes.
The calculation is as follows: (int) needed_bytes = 10 / 8 = 2, if remainder, then needed_bytes++

after calculation needed bytes we start writing:
	Byte 1 -> 0 offset
	Byte 2 -> 2 offset, meaning the first are empty.

Problem: How do we not lose bytes?
	Solution: Store bytes in temporary 32bit byte

	result = 0;	
	i = 0;
	for each byte in data:
		result = byte << (10 * i) 
					  
'''

def store_in_uint64_t(data):
	result = bytes(0)
	i = 0;
	for byte in data:
		result = result | (byte << (10 * i))
		i = i + 1;
	return result

ic = 0
dc = 0
source = open("result.asm")
result = open("binary.o", "w")
symbol_table[10][100]; 
symbol_names[10];
symbol_index = 0;

bool is_symbol_definition = False;

for line in source:
	first_word = line.split(':')[0]
	if (first_word.isupper()): 
		is_symbol_definition = True
		symbol_names[symbol_index++] = first_word
		line = line.split(' ')[1]		

	if line.startswith(".data"):
		if (is_symbol_definition):
			data = line.split(' ')[1];
			res;
			while ( (res = line.split[0] != ""):
				int(res)
						
			store_in_uint64_t(
			
	elif line.startswith(".mat"):
	elif line.startswith(".text"):
	else 
	
	if '.' in line:
		if (is_symbol_definition):
			if ".data" in line: 
				# store data in symbol table


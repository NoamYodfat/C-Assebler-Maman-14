data = bytes([129,129]);

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
result = 0;	
i = 0;
for byte in data:
	result = result | (byte << (10 * i))
	i = i + 1;	
	print(f"result is ", byte);	

expected_result = 0b00100000010010000001
print(f"expected:", expected_result, "result:", result);
if (expected_result == result):
	print(f"Success!") 
else: 
	print("Failure!");


def thousands_with_commas(i):
	"""Receive an integer and returns a string with the number
	with commas each three digits"""

	list_i = list(str(i))
	tmp_list_i = list_i[:]
	for n in range(len(list_i)-3, 0, -3):
		tmp_list_i.insert(n, ',')
	
	i = ''.join(tmp_list_i)
	return str(i)	
	

if __name__ == '__main__':
	assert thousands_with_commas(1234) == '1,234'
	assert thousands_with_commas(123456789) == '123,456,789'
	assert thousands_with_commas(12) == '12'

A = [1,1,2,2,3,4,4]
freq_dict = {}
for i in A:
	try:
		freq_dict[i] += 1
	except KeyError:
		freq_dict[i] = 1
#print(freq_dict)
for keys, values in freq_dict.items():
	if values == 1:
			break
			return keys

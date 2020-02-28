def distance(strand_a, strand_b):
    try:
    	hamLength = 0
    	if len(strand_a) == len(strand_b):
    		for i in range(len(strand_a)):
    			if(strand_a[i] != strand_b[i]): hamLength += 1
    		return hamLength
    	else: raise ValueError("The input strings have different length!")
    except ValueError as e:
    	raise e

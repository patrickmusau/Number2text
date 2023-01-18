def numtoword(number):
		#number = '1'
		number = number
				
		values = {'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','2x':'twenty','3x':'thirty','4x':'forty','5x':'fifty','6x':'sixty','7x':'seventy','8x':'eighty','9x':'ninenty','xxx':'hundred','10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen'}
		pvalue = {'4':'thousand','7':'million','10':'billion','13':'trillion','16':'zillion'}
		
		print(number)
		long = len(number)
		words = str()
		count = 1
		count2 = 1
		pv = 0
		
		for num in range(long):
			n = number[long-num-1]
			
			#Check if the second number lies between 10 - 19 by checking the second number
			if count == 1 and number[long-num-2] == '1' and num != long - 1:
				count += 1
				count2 += 1
				continue
						
			#Setting the value to be crosschechecked to get the correct word for the number
			#Single chatacters between 1-9, 10-19, 20-99
			val = n
			if count == 2:
				val = n + 'x'
				if n == '1':
					val = '1'+number[long-num]
					
			#Checking tge correct word for the number as per its value
			for j in values:
				if j == val:
					word = values[val]
					
			#Setting the place value for a thousand, million, billion, trillion and zillion
			if pv == 1:
				for k in pvalue:
					if int(k) == count2 or int(k)+1 == count2:
						word = word + ' ' + pvalue[k]
					pv = 0
			
			#For the hundred place value, the word 'hundred' should be added
			#Resetting the counter to zero and setting place value(pv) to be true
			if count == 3:
				word = word + ' hundred and'
				count = 0
				pv = 1
							
			count += 1
			count2 += 1
			#print(count2,val,pv)
			words = word + ' ' + words
				
			#print(words)
		print(words)
		return words
		
#numtoword()
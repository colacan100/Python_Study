score = input("Enter Score: ")
try:
    fs = float(score)
except:
    print("number error")
if(0.0<=fs<=1.0):
	if(fs>=0.9):
		print('A')
	elif(fs>=0.8):
		print('B')
	elif(fs>=0.7):
		print('C')
	elif(fs>=0.6):
		print('D')
	else:
		print('F')
else:
    print("range error")

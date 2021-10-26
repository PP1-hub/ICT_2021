str = str(input())

words = str.split(' ')
print ("Input: description:", str)

print ("Output: description:")
for W in words:
	if(len(W)%2==0):
	  print(W)
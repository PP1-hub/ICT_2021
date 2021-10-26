sentence=input("Input: description: text:")

word_to_find=input("word:")

words=sentence.split()

if word_to_find in words:

 print("Output:description:",True)

else:

 print("Output:description:",False)
user1 = int(input("age of the first people:"))
user2 = int(input("age of the second people:"))
user3 = int(input("age of the third people:"))

if(user1 >= user2 and user1 >= user3):
    print("Oldest is:", user1)
elif (user2 >= user1 and user2 >= user3):
    print("Oldest is:", user2) 
elif( user3 >= user1 and user3 >= user2):
    print("Oldest is:",user3)
     
if(user1 <= user2 and user1 <= user3):
    print("Oldest is:", user1)
elif (user2 <= user1 and user2 <= user3):
    print("Oldest is:", user2) 
elif( user3 <= user1 and user3 <= user2):
    print("Oldest is:",user3)


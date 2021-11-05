held = int(input("number of classes held: "))
attend = int(input("number of classes attended:"))

percent = (held / attend) * 100

if percent < 75:
    print("You cannot sit in the exams as your attendance is too low!")
else:
    print("You can sit in the exams as your attendance is fine.")    
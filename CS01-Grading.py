A = int(input("คะแนนเก็บ : "))
B = int(input("คะแนนสอบกลางภาค : "))
C =  int(input("คะเเนนสอบปลายภาค : ")) 

while True :
    if (A < 0) or (A > 30) :
        print("Error!")
        A = int(input("ข้อมูลผิดพลาด กรอกคะแนนเก็บใหม่ : "))
    elif (B < 0) or (B > 30) :
        print("Error!")
        B = int(input("ข้อมูลผิดพลาด กรอกคะแนนสอบกลางภาคใหม่ : "))
    elif (C < 0) or (C > 40) :
        print("Error!")
        C = int(input("ข้อมูลผิดพลาด กรอกคะเเนนสอบปลายภาคใหม่ : "))
    else :
        break

result = A + B + C

if (80 <= result) :
    print("Grade : A")
elif (75 <= result) :
    print("Grade : B+")
elif (70 <= result) :
    print("Grade : B")
elif (65 <= result) :
    print("Grade : C+")
elif (60 <= result) :
    print("Grade : C")
elif (55 <= result) :
    print("Grade : D+")
elif (50 <= result) :
    print("Grade : D")
elif (50 > result) :
    print("Grade : F")
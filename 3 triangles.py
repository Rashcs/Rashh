def determinethe_type(a,b,c):
 if(a==b==c):
    print("this is equilateral triangle")
 elif(a==b or b==c or c==a):
    print("thi is isoscles triangle")
 else:
    print("this is scalene triangle")

side1=int(input("enter the length of side1"))
side2=int(input("enter the length of side2"))
side3=int(input("enter the length of side3"))

triangle_type=determinethe_type(side1,side2,side3)
print(f"the triangle is{triangle_type}.")               

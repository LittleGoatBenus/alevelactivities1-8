import math

choice = input("""

  _ __ ___   __ _| |_| |__    _ __ ___   __ _  ___| |__ (_)_ __   ___
 | '_ ` _ \ / _` | __| '_ \  | '_ ` _ \ / _` |/ __| '_ \| | '_ \ / _ .
 | | | | | | (_| | |_| | | | | | | | | | (_| | (__| | | | | | | |  __/
 |_| |_| |_|\__,_|\__|_| |_| |_| |_| |_|\__,_|\___|_| |_|_|_| |_|\___|



1: ADDITION MACHINE
2: MULTIPLY MACHINE
3: VOLUME OF WATER
4: CIRCLE CALCULATIONS
5: AREA OF TRIANGLE
6: TIME OF JOURNEY
7: AREA OF TRAPEZOID
8: AREA OF OCTAGON

""")




if choice == '1':
    num1 = int(input("input the first number: "))
    num2 = int(input("input the second number: "))
    sum = num1 + num2
    print("your additon sum is", sum)

if choice == '2':
    num1 = int(input("input the first number: "))
    num2 = int(input("input the second number: "))
    sum = num1 * num2
    print("your multiplication sum is", sum)

if choice == '3':
    num1 = int(input("input the height of the tank in cm: "))
    num2 = int(input("input the length of the tank in cm: "))
    num3 = int(input("input the width of the tank in cm: "))
    sum = (num1 * num2 * num3) / 1000
    print("your tank will hold", sum, " Litres")

if choice == '4':
    pi = math.pi
    radius = int(input("input the radius of the circle: "))
    circumference = 2 * pi * radius
    area = pi * radius**2
    print("the circumfernce of your circle is: ", circumference, " \nthe area of your circle is: ", area)

if choice == '5':
    print("""


       /|
      / |
     /  | side 1
    /   |
   /___a|
   side 2

    """)

    a = int(input("input the angle alpha inbetween the 2 corresponding sides: "))
    arad = a * (math.pi/180)
    side1 = int(input("input side 1 : "))
    side2 = int(input("input side 2 : "))
    area = 0.5 * (side1 * side2 * math.sin(arad))
    print("the area of your triangle is: " ,area)

if choice == '6':
    vel = int(input("input the average velocity of the journey in ms-1: "))
    dis = int(input("input the distance of the journey in m: "))
    time = (dis/vel)/60
    print(time, "minutes")

if choice == '7':
    a = int(input("the top legnth of the trapzoid: "))
    b = int(input("the base length : "))
    h = int(input("the height: "))
    area = ((a + b)/2) * h
    print("the area is: ", area)

if choice == '8':
    a = int(input("input the length of one side of a regular octagon: "))
    area = (2(1 + 2**0.5)) * a
    print(area)

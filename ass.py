country={"India":"Delhi","China":"Beijing","Japan":"Tokyo",
         "Qatar":"Doha","France":"Marseilles"}
print(country)

"""
1.
country["France"]="Paris"
print(country)
"""

"""
2.
country[4]="France"
print(country)

"""

"""tuple_1 = (1,5,6,7,8)
tuple_2 = (8,9,4)

print(sum(tuple_1))
print(len(tuple_2))
print(tuple_2 + tuple_1)
print(tuple_1[3] = 45)
 
"""

def pythagorean(n):

    for a in range(1, n+1):
        for b in range(a+1, n+1):
            for c in range(b+1, n+1):
                if a*a + b*b == c*c:
                    print(a, b, c)

pythagorean(20)



# single levell of conditions

a=5
b=6
l=[11,2,7,4]
if a == 5:
    print("Scenario A")
elif a==6:

    print("Scenario B")
else:
    print("Scenario C")

l2=[x for x in l if x%2==0 or x%3==1]
print(l2)

# Example of list comprehension ... is aove
# Dic Comprehension -> Ubove

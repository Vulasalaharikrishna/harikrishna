s1=input("Enter the string :")
s2=input("Enter the string 2:")
l1=list(s1)
l2=list(s2)
for i in l1:
    if i in l2:
        l2.remove(i)
if(len(l2)==0):
    print("True")
else:
    print("False")

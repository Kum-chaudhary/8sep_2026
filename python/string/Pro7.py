s1 = "PyTHOn"

s2 = ""

for ch in s1:
    if ch.isupper():
        s2+=ch.lower()
    else:
        s2+=ch.upper()
        
        print("s1 :",s1)
        print("s2 :",s2)
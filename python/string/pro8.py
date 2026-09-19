"""
endswith()
startwith()
"""
s1 = "https://www.gmail.com"
if s1.startswith("https://"):
    if s1.endswith(".com") or s1.endswith(".in") or s1.endswith(".co.in"):
        print("valid and secure url")
    else:
        print("invalid url")
else:
    print("Sorry url is not secure!!")
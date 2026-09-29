quiz = {
    1 : {
        "que": "which is most popular programming language ?",
        "ans" : "Python"
    },
    2: {
        "que" : "who is prime minister of india ?",
        "ans" : "Narendra modi"
    },
    3: {
        "que":  "most treding technologies (AI / Cyber / Backend)",
        "ans" : "AI"
    }
}
#print(quiz)
#print(quiz[1]["que"])

#answer = input("Enter answer :")

for i in range(1,(len(quiz)+1)):
    print(f"\n que : {i}.{quiz[i]["que"]} ")
    ans = input("enter your ans :")

    if ans == quiz[i]["ans"]:
        print("correct answer !")
    else:
        print("Wrong answer")



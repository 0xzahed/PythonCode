def ChatGPT(a,b,c):
    print("Now text with ChatGPT\n")
    while True:
        text=str(input())
        text.lower()
        if "hi" in text:
            print("Hi! What can i do now?\n")
        elif "know me?" in text:
            print(f"Yes.You are {a}.You are from {b}.You are currently studying {c} semester.\n")
        elif "thanks" in text:
            print("Thanks for your gratitude.\n")
        elif "bye" in text:
            print("Good Bye.\n")
        else:
            print("Sorry,I can't understand.Please repeat.\n")


a=str(input("Enter your name:"))
b=str(input("Enter your Univarsity name:"))
c=str(input("Enter your current semester:"))
ChatGPT(a,b,c)




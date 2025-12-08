password = input("enter password :" )

if len(password) < 8:
    print("weak")
elif len(password) == 8: 
    print("moderate")
elif len(password) > 8:
    print("STRONG!")
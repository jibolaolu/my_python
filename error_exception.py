def ask_for_int():
    while True:
        try:
            res = int(input("Please provide a number: "))
        except:
            print("This is not a number please enter a number: ")
            continue
        else:
            print("Thanks for entering a number!!! ")
            break
        finally:
            print("This will always run at the end of the code")
            print("Finally this is the end of the try block!! ")

ask = ask_for_int()
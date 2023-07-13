def main():
    calc1 = 0.0
    calc2 = 0.0
    operation = ""
    while calc1 != "q":
        print("\nWhat is the first operator? Or, enter q to quit: ")
        calc1 = raw_input()
        if calc1.lower() == "q":
            break
        calc1 = float(calc1)
        print("\nWhat is the second operator? Or, enter q to quit: ")
        calc2 = raw_input()
        if calc2.lower() == "q":
            break
        calc2 = float(calc2)
        print("Enter an operation to perform on the two operators (+ or -): ")
        operation = raw_input()
        if operation == "+":
            print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
        elif operation == '-':
            print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
        else:
            print("\n Not a valid entry. Restarting...")

if __name__ == "__main__":
    main()

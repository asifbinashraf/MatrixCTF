def encoder(instr):
    outstr = str().join([chr((ord(instr[i]) << 8) + ord(instr[i + 1])) for i in range(0, len(instr), 2)])
    print(outstr)

user_in = input("Enter a string: ")
encoder(user_in)

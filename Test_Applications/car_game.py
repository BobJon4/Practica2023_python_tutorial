while True:
    command = input('>').upper()

    if command == 'HELP':
        print("START - to start the car")
        print("STOP - to stop the car")
        print("QUIT - to quit the game")
    elif command == 'START':
        print("The car started...")
    elif command == 'STOP':
        print("The car stopped...")
    elif command == 'QUIT':
        print("Game stopped")
        break
    else:
        print("Command doesn't exist, try again")
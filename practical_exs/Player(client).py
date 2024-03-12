from Client0 import Client

ip = "127.0.0.1"
port = 8080
c = Client(ip, port)
print(f"Connection to SERVER at {ip}, PORT: {port}")

secret_number = input("enter a guess")
guessing = True
while guessing:
    attempt = int(input('Enter an integer : '))
    if attempt == secret_number:
        print('Congratulations, you guessed it.')
        guessing = False
    elif attempt < secret_number:
        print("No, I'm afraid it is a little higher than that.")
    else:
        print("No, I'm afraid it is a little lower than that.")





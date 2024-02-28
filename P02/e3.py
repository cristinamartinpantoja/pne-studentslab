from Client0 import Client

def test_client_talk():
    # Creating a Client object
    c = Client(IP="192.168.1.45", PORT=8080)  # Replace with your actual server address

    print("-----| Practice 2, Exercise 3 |------")

    print("Sending a message to the server...")
    response = c.talk("Testing!!!")
    print(f"Response: {response}")

test_client_talk()
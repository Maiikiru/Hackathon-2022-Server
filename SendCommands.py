import socket

IP = socket.gethostbyname(socket.gethostname()) #Todo change this later to connect to a non-same machine
PORT = 7522                                     #PORT 7522 for sending text files
ADDRESS = (IP, PORT)
FORMAT = "utf-8"

TEXT_PATH = "D:\\SampleJavaPath\\toTransfer.txt"


def send_command(text):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDRESS)

    print("Sending commands")
    file = open(TEXT_PATH,"w")
    file.write(text)
    file.close()
    file = open(TEXT_PATH,"rb")
    client.sendall(file.read())
    client.close()


if __name__ == "__main__":
    userInput = input("Please enter a command for the tello: ")
    send_command(userInput)
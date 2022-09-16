import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 7522
ADDRESS = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024


#Sending files over TCP.
def main():
    print("STARTING SERVER")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDRESS)
    server.listen(5)
    print("LISTENING...")

    while True:
        client_socket, addr = server.accept()
        print(f"NEW CONNECTION {addr} connected.")

        try:
            print("Starting to read bytes..")
            buffer = client_socket.recv(1024)


            with open('video_' + str(n) + '.mp4', "wb") as video:
                i = 0
                while buffer:
                    video.write(buffer)
                    buffer = client_socket.recv(1024)

            print("Done reading bytes..")
            client_socket.close()

        except KeyboardInterrupt:
            if client_socket:
                client_socket.close()
            break

        client_socket.close()
        print(f"Disconnected {addr} disconnected.")


if __name__ == "__main__":
    main()

import socket
import os
import threading

IP = socket.gethostbyname(
    socket.gethostname())   # Since we will be connected to the same IP address, this code will work
                            # Upon changing to a non-local WI-FI, this will need to be changed.
PORT = 7523                 #PORT 7523 for sending videos.
ADDRESS = (IP, PORT)
FORMAT = "utf-8"
BUFFER_SIZE = 1024
VIDEO_FILE_PATH = "D:\\SampleJavaPath\\Videos\\"



# Sending files over TCP.
def accept_video_server():
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
            buffer = client_socket.recv(BUFFER_SIZE)
            i = 0
            while os.path.exists(f"{VIDEO_FILE_PATH}video{i}.mp4"):
                i += 1

            with open(VIDEO_FILE_PATH + "video" + str(i) + ".mp4", "wb") as video:
                while buffer:
                    video.write(buffer)
                    buffer = client_socket.recv(BUFFER_SIZE)

            print("Done reading bytes..")
            client_socket.close()

        except KeyboardInterrupt:
            if client_socket:
                client_socket.close()
            break

        client_socket.close()
        print(f"Disconnected {addr} disconnected.")





if __name__ == "__main__":
    x = threading.Thread(target=accept_video_server())
    x.start()


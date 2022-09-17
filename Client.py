import socket

IP = socket.gethostbyname(socket.gethostname()) #Todo change this later to connect to a non-same machine
PORT = 7523                                     #PORT 7523 for sending videos.
ADDRESS = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDRESS)

    print("Sending video")

    with open("D:\\SampleJavaPath\\tuyuUnderKids.mp4","rb") as video:
        buffer = video.read()
        client.sendall(buffer)


    client.close()


if __name__ == "__main__":
    main()

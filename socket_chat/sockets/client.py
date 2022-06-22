import socket


class Client_IPV4:
    def __init__(
        self,
        ip="127.0.0.1",
        port=8000,
        header_size=64,
        format="utf-8",
        disconnect_message="!DISCONNECT",
        logger=None,
    ):
        self.ADDR = (ip, port)
        self.IP = ip
        self.PORT = port
        self.HEADER = header_size
        self.FORMAT = format
        self.DISCONNECT_MESSAGE = disconnect_message
        self.logger = logger
        self.current_message = None
        self.stopped = False

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

    def send(self, msg):
        if type(msg) == bytes:
            message = msg
        elif type(msg) == str:
            message = msg.encode("utf-8")
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b" " * (self.HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)

    def disconnect(self):
        self.send(self.DISCONNECT_MESSAGE)
        self.client.close()

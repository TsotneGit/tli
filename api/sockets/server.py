import socket
import threading


class Server_IPV4:
    def __init__(
        self,
        ip=socket.gethostbyname(socket.gethostname()),
        port=5050,
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

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)

        self.connection_acceptor = threading.Thread(target=self.start)
        self.connection_acceptor.start()

    def log(self, msg):
        if self.logger:
            self.logger.log(msg)

    def handle_client(self, conn, addr):
        self.log(f"[NEW CONNECTION] {addr} connected")

        connected = True
        while connected:
            msg_length = conn.recv(self.HEADER).decode(self.FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(self.FORMAT)
                if msg == self.DISCONNECT_MESSAGE:
                    connected = False
                    break
                self.current_message = msg
                self.log(f"[{addr}] {msg}")
        conn.close()

    def start(self):
        self.server.listen()
        self.log(f"[LISTENING] Server is listening {self.IP}")
        while True:
            try:
                conn, addr = self.server.accept()
            except OSError:
                if self.stopped:
                    break
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            self.log(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

    def wait(self):
        while True:
            if self.current_message:
                break

    def receive(self):
        self.wait()
        msg = self.current_message
        self.current_message = None
        if msg != self.DISCONNECT_MESSAGE:
            return msg

    def stop(self):
        self.server.close()
        self.stopped = True

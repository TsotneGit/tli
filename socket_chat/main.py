from image_serializer import loads
from sockets import Server_IPV4


server = Server_IPV4(ip="127.0.0.1", header_size=16384)
a = server.receive()
loads(a).save("a.png")
print("A")
server.stop()

import socket

class UDPReceiver:
    def __init__(self, port=5005):
        self.UDP_IP = ""
        self.UDP_PORT = 5005
        self.sock = socket.socket(socket.AF_INET,  # Internet
                             socket.SOCK_DGRAM)  # UDP
        self.sock.bind((self.UDP_IP, self.UDP_PORT))
    def receive(self):
        print('Waiting for UDP message...')
        data, addr = self.sock.recvfrom(1024)  # buffer size is 1024 bytes
        print('Message received!')
        return data, addr



if __name__ == "__main__":
    udp_r = UDPReceiver(5005)
    while True:
        data, addr = udp_r.receive()
        print(str(data))
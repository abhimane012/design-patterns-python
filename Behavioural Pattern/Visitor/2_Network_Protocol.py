from abc import ABC, abstractmethod


class Packet(ABC):
    def accept(self, visitor):
        pass


class DataPacket(Packet):
    def accept(self, visitor):
        visitor.visit_data_packet(self)


class ControlPacket(Packet):
    def accept(self, visitor):
        visitor.visit_control_packet(self)


class PacketVisitor:
    def visit_data_packet(self, data_packet):
        pass

    def visit_control_packet(self, data_packet):
        pass


class PacketDecoder(PacketVisitor):
    def visit_data_packet(self, data_packet):
        print("Decoding Data Packet")

    def visit_control_packet(self, data_packet):
        print("Decoding Control Packet")


class PacketEncryptor(PacketVisitor):
    def visit_data_packet(self, data_packet):
        print("Encrypting Data Packet")

    def visit_control_packet(self, data_packet):
        print("Encrypting Control Packet")


class PacketCompressor(PacketVisitor):
    def visit_data_packet(self, data_packet):
        print("Compressing Data Packet")

    def visit_control_packet(self, data_packet):
        print("Compressing Control Packet")


class Network:
    def __init__(self):
        self.packets = []

    def add_packets(self, packet):
        self.packets.append(packet)

    def process_packet(self, visitor):
        for packet in self.packets:
            packet.accept(visitor)


if __name__ == "__main__":
    network = Network()

    control_packet = ControlPacket()
    data_packet = DataPacket()

    network.add_packets(control_packet)
    network.add_packets(data_packet)

    decoder = PacketDecoder()
    network.process_packet(decoder)

    encrypter = PacketEncryptor()
    network.process_packet(encrypter)

    compressor = PacketCompressor()
    network.process_packet(compressor)

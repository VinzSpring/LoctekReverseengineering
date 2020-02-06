from loctek_structs import Packet
from abc import ABC, abstractmethod


class AbstractPacketProcessor:
    @abstractmethod
    def on_packet_recv(self, packet: Packet)-> None:
        pass

class PacketProcessorLogger(AbstractPacketProcessor):
    def on_packet_recv(self, packet: Packet)-> None:
        print("Received packet with contents: ", packet.raw_bytes)

class PacketProcessorPersister(AbstractPacketProcessor):
    def on_packet_recv(self, packet)-> None:
        pass


class CompositePacketProcessor(AbstractPacketProcessor):
    def __init__(self, *processors: AbstractPacketProcessor):
        super().__init__()
        self.processors = processors

    def on_packet_recv(self, packet: Packet)-> None:
        for processor in self.processors:
            processor.on_packet_recv(packet)


class TM1650PacketProcessor(AbstractPacketProcessor):
    def __init__(self, path="./log.txt"):
        self.x = 0
        self.path = path
    def on_packet_recv(self, packet: Packet)-> None:

        if len(packet.raw_bytes) < 9:
            return

        _SEG = ["3F", "06", "5B", "4F", "66", "6D", "7D", "07", "7F", "6F", "77", "7C", "39", "5E", "79", "71"]
        payload = packet.raw_bytes[3:-3]
        decrypt = ""
        for i , c in enumerate(payload):
            if c in _SEG:
                decrypt += str(_SEG.index(c))
            else:
                j = hex(int(c[0], 16) - 0x08)[2:]
                decrypt += str(_SEG.index(j + c[1])) 
                decrypt += "."
        print(decrypt)







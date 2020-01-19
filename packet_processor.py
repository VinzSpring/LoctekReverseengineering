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



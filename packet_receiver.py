import serial
import re
from loctek_structs import Packet
from packet_processor import AbstractPacketProcessor

from abc import ABC, abstractmethod


class AbstractPacketReceiver:
    @abstractmethod
    def start_receiving(self, packet_processor: AbstractPacketProcessor)-> None:
        pass
    @abstractmethod
    def end_receiving(self)-> None:
        pass

class SerialPacketReceiver(AbstractPacketReceiver):
    def __init__(self, port_name: str, baud_rate: int=9600):
        super().__init__()
        self.baud_rate = baud_rate
        self.port_name = port_name

        self.stop_listening = False

    def start_receiving(self,  packet_processor: AbstractPacketProcessor)-> None:
        with serial.Serial(self.port_name, self.baud_rate) as conn:
            print("listening on port ", conn.name)
            buff = []
            while not self.stop_listening:
                byte = conn.read()
                buff.append(byte)
                if buff and buff[0] != Packet.BYTE.START:
                        buff = []
                elif Packet.is_valid_packet(buff):
                    packet_processor.on_packet_recv(Packet(0, 0, buff))
                    buff.clear()

        self.stop_listening = False

    def stop_receiving(self)-> None:
        self.stop_listening = True

class PulseViewFilePacketReceiver(AbstractPacketReceiver):
    def __init__(self, file_path: str):
        super().__init__()
        self.file_path = file_path


    def start_receiving(self,  packet_processor: AbstractPacketProcessor)-> None:
        pattern = re.compile(r"(\d+)-(\d+).+RX:\s+(\w+)")
        buff = []
        t_pckg_start = -1
        t_pckg_end = -1

        with open(self.file_path, "r") as f:
            for line in f.readlines():
                for match in re.finditer(pattern, line):
                    t_start, t_end, byte = match.group(1), match.group(2), match.group(3)
                    if byte in "Start Stop".split():
                        continue

                    if byte == Packet.BYTE.START:
                        t_pckg_start = t_start
                    elif byte == Packet.BYTE.STOP:
                        t_pckg_end = t_end

                    buff.append(byte)

                    if buff and buff[0] != Packet.BYTE.START:
                        buff = []
                    elif Packet.is_valid_packet(buff):
                        packet_processor.on_packet_recv(Packet(t_pckg_start, t_pckg_end, buff))
                        buff = []


    def stop_receiving(self)-> None:
        pass

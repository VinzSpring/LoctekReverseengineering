from packet_receiver import PulseViewFilePacketReceiver, SerialPacketReceiver
from packet_processor import CompositePacketProcessor, PacketProcessorLogger, PacketProcessorPersister


if __name__ == "__main__":

    receiver = PulseViewFilePacketReceiver("./samples/71.5_no_btns.txt")
    # receiver = SerialPacketReceiver("COM3", 9600)
    processor = CompositePacketProcessor(PacketProcessorLogger(), PacketProcessorPersister())

    receiver.start_receiving(processor)
    

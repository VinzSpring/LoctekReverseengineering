from packet_receiver import PulseViewFilePacketReceiver, SerialPacketReceiver
from packet_processor import CompositePacketProcessor, PacketProcessorLogger, PacketProcessorPersister, TM1650PacketProcessor


if __name__ == "__main__":

    receiver = PulseViewFilePacketReceiver("./samples/71.3_no_btns.txt")
    # receiver = SerialPacketReceiver("COM3", 9600)
    tm_processor = TM1650PacketProcessor()
    processor = CompositePacketProcessor(PacketProcessorLogger(), PacketProcessorPersister(), tm_processor)

    receiver.start_receiving(processor)
    


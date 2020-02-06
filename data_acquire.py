from packet_receiver import PulseViewFilePacketReceiver, SerialPacketReceiver
from packet_processor import CompositePacketProcessor, PacketProcessorLogger, PacketProcessorPersister, TM1650PacketProcessor


if __name__ == "__main__":

    #receiver = PulseViewFilePacketReceiver("./samples/TX_btn_down.txt")
    receiver = SerialPacketReceiver("COM4", 9600)
    tm_processor = TM1650PacketProcessor()
    processor = CompositePacketProcessor(PacketProcessorPersister(), tm_processor)

    receiver.start_receiving(processor)
    



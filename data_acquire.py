from packet_receiver import PulseViewFilePacketReceiver, SerialPacketReceiver
from packet_processor import CompositePacketProcessor, PacketProcessorLogger, PacketProcessorPersister


if __name__ == "__main__":

    receiver = PulseViewFilePacketReceiver("./going_down_75_71_no_btn_R.txt")
    processor = CompositePacketProcessor(PacketProcessorLogger(), PacketProcessorPersister())

    receiver.start_receiving(processor)
    
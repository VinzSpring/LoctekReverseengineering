
class Packet:
    class BYTE:
        START = "9B"
        STOP = "9D"


    def __init__(self, t_start, t_end, raw_bytes):
        super().__init__()
        self.t_start = t_start
        self.t_end = t_end
        self.raw_bytes = raw_bytes

    @staticmethod
    def is_valid_packet(raw_bytes):
        return raw_bytes[0] == Packet.BYTE.START and raw_bytes[-1] == Packet.BYTE.STOP and int(raw_bytes[1], 16) == (len(raw_bytes) - 2)


    
import re
from pprint import pprint as p

"""
DEPRECATED, TEST-SCRIPT
"""

class BYTE:
    START = "9B"
    STOP = "9D"

pattern = re.compile(r"(\d+)-(\d+).+RX:\s+(\w+)")


def get_frames(pulseview_uart_lines, t_pause=1000):
    packets = []
    t_last = -1
    packet = []
    for line in pulseview_uart_lines:
        for match in re.finditer(pattern, line):
            t_start, t_end, val = match.group(1), match.group(2), match.group(3)
            if val in "Start Stop".split():
                continue
            t_start, t_end = int(t_start), int(t_end)
            if t_last == -1:
                t_last = t_end

            delta_t = t_start - t_last
            t_last = t_end
            if delta_t <= t_pause:
                packet.append(val)
            else:
                packets.append(packet)
                packet = [val]
    return packets

def get_packets(frames):
    packets = []

    for frame in frames:
        packet = []
        for byte in frame:
            if byte == BYTE.START:
                packet = []
            packet.append(byte)
            if byte == BYTE.STOP:
                if is_valid_packet(packet):
                    packets.append(packet)
                else:
                    print("encountered invalid packet: ", packet)
                packet = []
    return packets

def is_valid_packet(packet):
    return packet[0] == BYTE.START and packet[-1] == BYTE.STOP and int(packet[1], 16) == (len(packet) - 2)
 
def uniqueness(packets):
    return list(set(tuple(p) for p in packets))

if __name__ == "__main__":
    with open("./going_down_75_71_no_btn_R.txt") as f:
        frames = get_frames(f.readlines())

    packets = get_packets(frames)

    unique_packets = uniqueness(packets)

    with open("unique_packets.csv", "w+") as f:
        lines = [",".join(packet) for packet in unique_packets]
        f.write("\n".join(lines))
    
    with open("export.csv", "w+") as f:
        lines = [",".join(packet) for packet in packets]
        f.write("\n".join(lines))
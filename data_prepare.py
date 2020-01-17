import re
from pprint import pprint as p

pattern = re.compile(r"(\d+)-(\d+).+RX:\s+(\w+)")


def get_packets(pulseview_uart_lines, t_pause=1000):
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
                continue
            delta_t = t_start - t_last
            t_last = t_end
            if delta_t <= t_pause:
                packet.append(val)
            else:
                packets.append(packet)
                packet = [val]
    return packets



if __name__ == "__main__":
    with open("./going_down_75_71_no_btn_R.txt") as f:
        get_packets(f.readlines())
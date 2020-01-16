import re

patterbn


def get_packets(pulseview_uart_lines):
    packets = []
    t_last = 0
    for line in pulseview_uart_lines:

        
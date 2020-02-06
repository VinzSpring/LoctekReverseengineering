import serial

seventy_one = b"\x9B\x07\x12\x07\x86\x3F\x09\x07\x9D"
if __name__ == "__main__":
    with serial.Serial("COM6", 9600) as conn:
        while True:
            while conn.in_waiting:
                print(conn.read())

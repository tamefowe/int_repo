from pathlib import Path



def run() :
    path = "C:\cygwin64\home\Trader\C++\iTest\input.dat"
    data = Path(path).read_bytes()
    i = int.from_bytes(data[:2], byteorder='big', signed=False)
    j = int.from_bytes(data[2:4], byteorder='big', signed=False)
    length = int.from_bytes(data[4:6], byteorder='big', signed=False)
    type = data[6:7].decode( encoding='utf-8')
    sym = data[7:12].decode(encoding='utf-8')
    size = int.from_bytes(data[12:14], byteorder='big', signed=False)
    price = int.from_bytes(data[14:22], byteorder='big', signed=False)
    print("{} {}".format(i, j))


if __name__ == "__main__":
    run()
import math


class Conversor:
    def convert(self, conv_val):
        size = len(conv_val)
        i, addr = 0, 0

        if size == 4:
            conv_val = conv_val.replace("0", "2").replace("1", "0")
            while i < size:
                addr += int(conv_val[i]) * pow(3, i)
                i += 1
            return addr

        elif size == 8:
            while i+1 < size:
                delta = int(conv_val[i])
                dib = int(conv_val[i+1])
                if delta == 1 and dib == 1:
                    raise Exception("Invalid DIP switches configuration")
                else:
                    base = 0
                    if delta == 0 and dib == 0:
                        base = 2
                    elif delta == 0 and dib == 1:
                        base = 1
                    addr += base * pow(3, math.trunc(i/2))
                    i += 2
            return addr

        elif size <=2 and size > 0:
            conv_val = int(conv_val)
            addr = ""
            addr_d4 = "Invalid adrress"
            addr_d8 = "Invalid address"

            if conv_val == 80 or conv_val == 0:
                addr = "0000"
            else:
                while conv_val > 0:
                    addr = addr + str(conv_val % 3)
                    conv_val = conv_val // 3

                while len(addr) < 4:
                    addr = addr + "0"

            if "1" not in addr and len(addr) == 4:
                addr_d4 = addr.replace("0", "1").replace("2", "0")
            if len(addr) == 4:
                addr_d8 = ""
                for b in addr:
                    if b == "0":
                        addr_d8 = addr_d8 + "10"
                    elif b == "1":
                        addr_d8 = addr_d8 + "01"
                    elif b == "2":
                        addr_d8 = addr_d8 + "00"

            return {"D4": addr_d4, "D8": addr_d8}
        else:
            raise Exception("Invalid value")

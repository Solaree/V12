from NaCl import NaCl

class ByteStream:
    def __init__(self, client, endian: str = 'big'):
        self.client = client
        self.endian = endian
        self.buffer = b''

    def writeInt(self, data, length=4):
        self.buffer += data.to_bytes(length, 'big')
    
    def size(self):
        return len(self.buffer)
    
    def getRaw(self):
        return self.buffer
    
    def writeIntEndian(self, data, length=4):
        self.buffer += data.to_bytes(length, 'little')
    
    def writeShortEndian(self, data, length=2):
        self.buffer += data.to_bytes(length, 'little')

    def writeUInteger(self, integer: int, length: int = 1):
        self.buffer += integer.to_bytes(length, self.endian, signed=False)
    
    def writeArrayVInt(self, data):
        self.writeVInt(len(data));
        for x in data:
            self.writeVInt(x)

    def writeUInt8(self, integer: int):
        self.writeUInteger(integer)
    
    def writeBytes(self, data):
        self.buffer += data

    def writeHexa(self, data):
        if data:
            if data.startswith('0x'):
                data = data[2:]

            self.buffer += bytes.fromhex(''.join(data.split()).replace('-', ''))

    def send(self, crypto):
        self.encode()
        packet_data = crypto.encrypt(self.id, self.buffer)
        self.buffer = self.id.to_bytes(2, 'big', signed=True)
        self.writeInt(len(packet_data), 3)
        if hasattr(self, 'version'):
            self.writeInt16(self.version)
        else:
            self.writeInt16(0)
        self.buffer += packet_data
        self.client.send(self.buffer)

    def writeVInt(self, data, rotate: bool = True):
        final = b''
        if data == 0:
            self.writeByte(0)
        else:
            data = (data << 1) ^ (data >> 31)
            while data:
                b = data & 0x7f

                if data >= 0x80:
                    b |= 0x80
                if rotate:
                    rotate = False
                    lsb = b & 0x1
                    msb = (b & 0x80) >> 7
                    b >>= 1
                    b = b & ~0xC0
                    b = b | (msb << 7) | (lsb << 6)

                final += b.to_bytes(1, 'big')
                data >>= 7
        self.buffer += final

    def writeString(self, string: str = None):
        if string is None:
            self.writeInt((2**32)-1)
        else:
            encoded = string.encode('utf-8')
            self.writeInt(len(encoded))
            self.buffer += encoded

    def writeByte(self, data):
        self.writeInt(data, 1)

    def writeInt16(self, data):
        self.writeInt(data, 2)

    def writeDataReference(self, ClassID, InstanceID):
        self.writeVInt(ClassID)
        self.writeVInt(InstanceID)
from Crypto.Util.Padding import unpad
from Crypto.Util.number import bytes_to_long as b2l, long_to_bytes as l2b
from enum import Enum

class Mode(Enum):
    ECB = 0x01
    CBC = 0x02
    CFB = 0x03

class Cipher:
    def __init__(self, key, iv=None):
        self.BLOCK_SIZE = 64
        self.KEY = [b2l(key[i:i+self.BLOCK_SIZE//16]) for i in range(0, len(key), self.BLOCK_SIZE//16)]
        self.DELTA = 0x9e3779b9
        self.IV = iv
        self.ROUNDS = 64
        if self.IV:
            self.mode = Mode.CBC if iv else Mode.ECB
            if len(self.IV) * 8 != self.BLOCK_SIZE:
                self.mode = Mode.CFB

    def _xor(self, a, b):
        return b''.join(bytes([_a ^ _b]) for _a, _b in zip(a, b))

    def encrypt_block(self, msg):
        m0 = b2l(msg[:4])
        m1 = b2l(msg[4:])
        msk = (1 << (self.BLOCK_SIZE//2)) - 1
        s = self.DELTA << 5
        for i in range(self.ROUNDS):
            m1 -= ((m0 << 4) + self.KEY[(i+2) % len(self.KEY)]) ^ (m0 + s) ^ ((m0 >> 5) + self.KEY[(i+3) % len(self.KEY)])
            m1 &= msk
            m0 -= ((m1 << 4) + self.KEY[i % len(self.KEY)]) ^ (m1 + s) ^ ((m1 >> 5) + self.KEY[(i+1) % len(self.KEY)])
            m0 &= msk
            s -= self.DELTA
        return l2b((m0 << (self.BLOCK_SIZE//2)) | m1)

    def decrypt(self, ct):
        blocks = [ct[i:i + self.BLOCK_SIZE // 8] for i in range(0, len(ct), self.BLOCK_SIZE // 8)]
        pt = b''
        if self.mode == Mode.ECB:
            for block in blocks:
                pt += self.decrypt_block(block)
        elif self.mode == Mode.CBC:
            X = self.IV
            for block in blocks:
                dec_block = self.decrypt_block(block)
                pt += self._xor(X, dec_block)
                X = block
        elif self.mode == Mode.CFB:
            X = self.IV
            for block in blocks:
                output = self.encrypt_block(X)
                dec_block = self._xor(output, block)
                pt += dec_block
                X = block
        try:
            return unpad(pt, self.BLOCK_SIZE // 8)
        except ValueError:
            return pt

    def decrypt_block(self, ct):
        m0 = b2l(ct[:4])
        m1 = b2l(ct[4:])
        msk = (1 << (self.BLOCK_SIZE//2)) - 1
        s = self.DELTA << 5
        for i in range(self.ROUNDS - 1, -1, -1):
            m0 -= ((m1 << 4) + self.KEY[(i+2) % len(self.KEY)]) ^ (m1 + s) ^ ((m1 >> 5) + self.KEY[(i+3) % len(self.KEY)])
            m0 &= msk
            m1 -= ((m0 << 4) + self.KEY[i % len(self.KEY)]) ^ (m0 + s) ^ ((m0 >> 5) + self.KEY[(i+1) % len(self.KEY)])
            m1 &= msk
            s -= self.DELTA
        return l2b((m0 << (self.BLOCK_SIZE//2)) | m1)

if __name__ == '__main__':
    KEY = bytes.fromhex("3362623866656338306539313238353733373566366338383563666264386133")
    IV = bytes.fromhex("64343537373337663034346462393931")
    cipher = Cipher(KEY, IV)
    ct = bytes.fromhex("1cb8db8cabe8edbbddb236d5eb6f0cdeb610e9af855b52d3")
    pt = cipher.decrypt(ct)
    print("Decrypted plaintext:", pt.decode())
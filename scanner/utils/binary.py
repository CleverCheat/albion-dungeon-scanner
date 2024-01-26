import gzip
import io

from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

from scanner.utils.singleton import Singleton


class BinaryDecrypter:
    def __init__(self):
        self.key = bytes([48, 239, 114, 71, 66, 242, 4, 50])
        self.iv = bytes([14, 166, 220, 137, 219, 237, 220, 79])

    def decrypt_binary_file(self, input_path):
        with open(input_path, "rb") as input_file:
            file_buffer = input_file.read()

            t_des = DES.new(self.key, DES.MODE_CBC, self.iv)
            out_buffer = unpad(t_des.decrypt(file_buffer), DES.block_size)

            buffer_size = 4096
            buffer = bytearray(buffer_size)
            output_buffer = io.BytesIO()

            with gzip.GzipFile(
                fileobj=io.BytesIO(out_buffer), mode="rb"
            ) as decompression:
                while True:
                    bytes_read = decompression.readinto(buffer)
                    if bytes_read == 0:
                        break
                    output_buffer.write(buffer[:bytes_read])

            return output_buffer.getvalue()


class Binary(metaclass=Singleton):
    def __init__(self) -> None:
        self.decrypter = BinaryDecrypter()

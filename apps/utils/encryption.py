# -*- coding:utf-8 -*-
# @FileName  :encryption.py
# @Time      :2023/1/30 14:57
# @Author    : yuhaiping
import base64

from Crypto.Cipher import AES

from django.conf import settings as django_settings


class EncryptionHelper(object):

    def __init__(self, ):
        self.key = django_settings.SECRET_KEY[0:6]
        # init aes
        self.aes = AES.new(self.add_to_16(self.key), AES.MODE_ECB)

    def encrypt(self, text):
        encrypted_text = str(base64.encodebytes(self.aes.encrypt(self.add_to_16(text))), encoding='utf8').replace('\n',
                                                                                                                  '')
        return encrypted_text

    def decrypt(self, encrypted_text):
        text_decrypted = str(
            self.aes.decrypt(base64.decodebytes(bytes(encrypted_text, encoding='utf8'))).rstrip(b'\0').decode(
                "utf8"))
        # return bytes
        return text_decrypted

    @staticmethod
    def add_to_16(text):
        while len(text) % 16 != 0:
            text += '\0'
        # return bytes
        return str.encode(text)


class AESOperator(object):

    def __init__(self):
        self.key = django_settings.AES_KEY
        # 16-bit character, used to fill in missing content,
        # can be fixed value or random string, specific selection depends on requirements.
        self.iv = django_settings.AES_IV
        self.key = self.key.encode('utf-8')
        self.iv = self.iv.encode('utf-8')

    @staticmethod
    def __pad(text):
        """
        Fill method:
            the encrypted content must be a multiple of 16 bytes.
            If it is insufficient, use self.iv to fill
        """
        text_length = len(text)
        amount_to_pad = AES.block_size - (text_length % AES.block_size)
        if amount_to_pad == 0:
            amount_to_pad = AES.block_size
        pad = chr(amount_to_pad)
        return text + pad * amount_to_pad

    @staticmethod
    def __un_pad(text):
        pad = ord(text[-1])
        return text[:-pad]

    def encrypt(self, raw):

        raw = self.__pad(raw)
        raw = raw.encode('utf-8')
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return base64.urlsafe_b64encode(cipher.encrypt(raw)).decode("utf-8")

    def decrypt(self, enc):

        try:
            enc = base64.urlsafe_b64decode(enc)
            cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
            return self.__un_pad(cipher.decrypt(enc).decode("utf-8"))
        except Exception as e:
            print(e)
            return None


if __name__ == '__main__':
    value = EncryptionHelper().encrypt("11112")
    print(value)

    value = EncryptionHelper().encrypt("31111")
    print(value)

    value = EncryptionHelper().decrypt("FpQUPGlWd5QS2oUc1Yv8mQ==")
    print(value)

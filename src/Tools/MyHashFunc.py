from hashlib import sha256


class HashFunction:
    @staticmethod
    def sha256_str(item):
        return sha256(str(item).encode()).hexdigest()

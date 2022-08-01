from typing import Literal
from hashlib import md5, sha1, sha224, sha256, sha384, sha512


class Hash:
    __hashing_methods = {"md5": md5, "sha1": sha1, "sha224": sha224, "sha256": sha256, "sha384": sha384,
                         "sha512": sha512}
    __encoding_methods = ("utf-8", "utf-16", "ascii")

    @classmethod
    def get_hash_of_string(cls, string: str,
                           hashing_method: Literal["md5", "sha1", "sha224", "sha256", "sha384", "sha512"] = "sha256",
                           encoding: Literal["utf-8", "utf-16", "ascii"] = "utf-8") -> int:

        if not isinstance(string, str):
            raise ValueError("String argument should be an instance of the str type.")
        if hashing_method not in cls.__hashing_methods.keys():
            raise ValueError("Please, use available hashing methods.")
        if encoding not in cls.__encoding_methods:
            raise ValueError("Please, use available encoding methods.")

        byte_string = bytes(string, encoding)
        hash_object = cls.__hashing_methods[hashing_method](byte_string)
        return hash_object.hexdigest()


if __name__ == '__main__':
    print(Hash.get_hash_of_string("Python Bootcamp"))
    print(Hash.get_hash_of_string("Python Bootcamp", "md5"))
    print(Hash.get_hash_of_string("Python Bootcamp", "sha1", "ascii"))
    print(Hash.get_hash_of_string("Python Bootcamp", "sha224", "utf-16"))
    print(Hash.get_hash_of_string("Python Bootcamp", "sha256", "utf-8"))
    print(Hash.get_hash_of_string("Python Bootcamp", "sha384"))
    print(Hash.get_hash_of_string("Python Bootcamp", "sha512"))

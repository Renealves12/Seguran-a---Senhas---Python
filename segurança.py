import hashlib

senha = "1234"
hash_md5 = hashlib.md5(senha.encode()).hexdigest()
print("hash MD5:",hash_md5)


import bcrypt

senha = b"1234"

hash_seguro = bcrypt.hashpw(senha, bcrypt.gensalt())
print("Hash seguro",hash_seguro)

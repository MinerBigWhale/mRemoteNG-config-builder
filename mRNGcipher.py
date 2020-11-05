
    
import hashlib
import base64
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

def encryptAES(plaintext, password):
    if password == "":
        password = "mR3m"
    plaintext = plaintext.encode("utf-8")
    
    salt = get_random_bytes(16)
    associated_data = salt
    key = hashlib.pbkdf2_hmac("sha1", password.encode(), salt, 1000, dklen=32)
    
    cipher = AES.new(key, AES.MODE_GCM)
    cipher.update(associated_data)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    nonce = cipher.nonce
    
    #print("salt: {}, nonce: {}, ciphertext: {}, tag: {}".format(salt, nonce, ciphertext, tag))
    encrypted_data  = bytearray()
    encrypted_data.extend(salt)
    encrypted_data.extend(nonce)
    encrypted_data.extend(ciphertext)
    encrypted_data.extend(tag)

    return base64.b64encode(encrypted_data).decode("utf-8")

def decryptAES(encrypted, password):
    if password == "":
        password = "mR3m"
    encrypted_data = base64.b64decode(encrypted)

    salt = encrypted_data[:16]
    associated_data = encrypted_data[:16]
    nonce = encrypted_data[16:32]
    ciphertext = encrypted_data[32:-16]
    tag = encrypted_data[-16:]
    key = hashlib.pbkdf2_hmac("sha1", password.encode(), salt, 1000, dklen=32)
    #print("salt: {}, nonce: {}, ciphertext: {}, tag: {}".format(salt, nonce, ciphertext, tag))

    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    cipher.update(associated_data)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode("utf-8")

if __name__ == "__main__":
    print(decryptAES(encryptAES("AES Test Passed", ""), ""))
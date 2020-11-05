from mRNGcipher import encryptAES, decryptAES

def test_encryption():
    assert decryptAES(encryptAES("AES Test Passed", ""), "") == "AES Test Passed"
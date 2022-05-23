from Crypto.PublicKey import RSA

# 產生 2048 位元 RSA 金鑰
key = RSA.generate(2048)

# RSA 私鑰
privateKey = key.export_key()
with open("private.pem", "wb") as f:
    f.write(privateKey)

# RSA 公鑰
publicKey = key.publickey().export_key()
with open("public.pem", "wb") as f:
    f.write(publicKey)
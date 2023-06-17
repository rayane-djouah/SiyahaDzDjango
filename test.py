import hashlib
import binascii
import os

password = "monmotdepasse"
salt = os.urandom(16)  # Génération d'un sel aléatoire

# Hachage du mot de passe avec PBKDF2 et SHA-256
hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
hashed_password = binascii.hexlify(hashed_password).decode('utf-8')

print(hashed_password)

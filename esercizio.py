import hashlib

testo=input("testo da hashare: ")

hash_finale = hashlib.md5(testo.encode()).hexdigest()

print("Testo:", testo, "MD5:", hash_finale)

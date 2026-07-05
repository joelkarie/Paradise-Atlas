from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

password = input("Enter your password: ")

print(password_hash.hash(password))
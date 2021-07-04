import hashlib,binascii
choice = int(input('''
Choose 1 Project number:-

1) Write a program in python to generate MD5 of strung data

2) Write a program in python to generate hashes of string using 3 algorithm from hashlib

3) Add salting and iteration to your hashes

Choice:- '''))

print('\n\n')

string = input('Enter the String:- ')

# Write a program in python to generate MD5 of strung data
if choice == 1:


  md5 = hashlib.md5(string.encode())
  print(md5.hexdigest())


# Write a program in python to generate hashes of string using 3 algorithm from hashlib
elif choice == 2:


  md5 = hashlib.md5(string.encode())
  print(md5.hexdigest())

  sha1 = hashlib.sha1(string.encode())
  print(sha1.hexdigest())

  sha224 = hashlib.sha224(string.encode())
  print(sha224.hexdigest())


# Add salting and iteration to your hashes
elif choice == 3:


  salt = input('Enter your salt:- ')

  md5 = hashlib.pbkdf2_hmac('md5', bytes(string,'utf-8'), bytes(salt,'utf-8'), 100000)
  sha1 = hashlib.pbkdf2_hmac('sha1', bytes(string,'utf-8'), bytes(salt,'utf-8'), 100000)
  sha224 = hashlib.pbkdf2_hmac('sha224', bytes(string,'utf-8'), bytes(salt,'utf-8'), 100000)
  sha256 = hashlib.pbkdf2_hmac('sha256', bytes(string,'utf-8'), bytes(salt,'utf-8'), 100000)
  sha384 = hashlib.pbkdf2_hmac('sha384', bytes(string,'utf-8'), bytes(salt,'utf-8'), 100000)
  sha512 = hashlib.pbkdf2_hmac('sha512', bytes(string,'utf-8'), bytes(salt,'utf-8'), 100000)

  print(str(binascii.hexlify(md5)).replace("b'","").replace("'",""))
  print(str(binascii.hexlify(sha1)).replace("b'","").replace("'",""))
  print(str(binascii.hexlify(sha224)).replace("b'","").replace("'",""))
  print(str(binascii.hexlify(sha256)).replace("b'","").replace("'",""))
  print(str(binascii.hexlify(sha384)).replace("b'","").replace("'",""))
  print(str(binascii.hexlify(sha512)).replace("b'","").replace("'",""))


else:  
  print('ENTER 1 OR 2 OR 3')
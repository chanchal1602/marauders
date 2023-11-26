import random

def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a

def is_prime(num):
  if num <= 1:
    return False
  if num <= 3:
    return True
  if num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6
  return True

def generate_keypair(p, q):
  if not (is_prime(p) and is_prime(q)):
    raise ValueError("p and q must be prime numbers")
  n = p * q
  phi = (p - 1) * (q - 1)
  e = random.randrange(2, phi)
  d = pow(e, -1, phi)
  public_key = (e, n)
  private_key = (d, n)
  return public_key, private_key

def encrypt(message, public_key):
  e, n = public_key
  c = pow(message.encode(), e, n)
  return c

def decrypt(ciphertext, private_key):
  d, n = private_key
  m = pow(ciphertext, d, n)
  return m.decode()

def encrypt_string(message, public_key):
  encrypted_message = encrypt(message.encode(), public_key)
  return encrypted_message

def decrypt_string(encrypted_message, private_key):
  decrypted_message = decrypt(encrypted_message, private_key)
  return decrypted_message

# Example usage

p = 17
q = 23
public_key, private_key = generate_keypair(p, q)

message = "This is a secret message"
encrypted_message = encrypt_string(message, public_key)

decrypted_message = decrypt_string(encrypted_message, private_key)

print(decrypted_message)


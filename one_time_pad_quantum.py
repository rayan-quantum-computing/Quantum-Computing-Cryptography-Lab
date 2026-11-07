# 11/07/2026
# What I was testing: feeding my one-time pad with a key made from quantum
#   measurements instead of the system's randomness.
# What I expected: the message should encrypt and then decrypt back exactly,
#   just like before, but the key now comes from quantum bits.
# Note: the quantum bits come from a quantum simulator (Qiskit Aer), not real hardware yet.
# What came out:
#   Message:   Meet me at noon
#   Key (hex): 3fdecf9f4cdde1308a9fedc01d9a5b
#   Cipher:    72bbaaeb6cb08410ebebcdae72f535
#   Recovered: Meet me at noon

from quantum_password import quantum_bits
from one_time_pad import xor_bytes, encrypt, decrypt


def generate_quantum_key(length):
    # Build a key of 'length' bytes. Each byte is made from 8 quantum bits.
    key = bytearray()
    for _ in range(length):
        bits = quantum_bits(8)       # 8 quantum bits, as a string like "01101001"
        value = int(bits, 2)         # turn those 8 bits into a number from 0 to 255
        key.append(value)            # add that byte to the key
    return bytes(key)


if __name__ == "__main__":
    message = "Meet me at noon"
    key = generate_quantum_key(len(message.encode("utf-8")))   # key as long as the message, in bytes
    cipher = encrypt(message, key)
    recovered = decrypt(cipher, key)
    print("Message:  ", message)
    print("Key (hex):", key.hex())
    print("Cipher:   ", cipher.hex())
    print("Recovered:", recovered)

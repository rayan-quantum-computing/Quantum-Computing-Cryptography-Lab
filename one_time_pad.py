# one_time_pad.py
# Date : 2026-10-10
# What I was testing: encrypting a message with a one-time pad, XOR of the message with a random key of the same length.
# What I expected: the same key both encrypts and decrypts; a wrong key gives unreadable bytes.
# What came out:
#   Message    : Meet me at noon
#   Key (hex)  : adfe705cabff8a6539e477abca760c
#   Cipher hex : e09b15288b92ef45589057c5a51962
#   Recovered  : Meet me at noon
#   Wrong key  : (unreadable bytes, exactly as expected)


"""
One-Time Pad
Part of the "Cryptography in the Quantum Era" project.

The one-time pad is the only cipher proven to be unbreakable, on one
condition: the key must be truly random, as long as the message, used
only once, and kept secret. This file shows the mechanism on real bytes.
"""

import os


def generate_key(length):
    """Return `length` random bytes.
    os.urandom gives cryptographically strong random bytes from the
    operating system. Later this could be replaced by my own quantum
    random number generator from the first project."""
    return os.urandom(length)


def xor_bytes(data, key):
    """Combine two byte strings of equal length with XOR, byte by byte.
    XOR is its own inverse: applying the same key a second time gives
    back the original. That single fact is what makes the pad reversible."""
    return bytes(d ^ k for d, k in zip(data, key))


def encrypt(message, key):
    """Turn the text into bytes, then XOR those bytes with the key."""
    message_bytes = message.encode("utf-8")
    return xor_bytes(message_bytes, key)


def decrypt(ciphertext, key):
    """XOR the ciphertext with the same key, then read it back as text."""
    message_bytes = xor_bytes(ciphertext, key)
    return message_bytes.decode("utf-8")


if __name__ == "__main__":
    message = "Meet me at noon"
    key = generate_key(len(message.encode("utf-8")))

    ciphertext = encrypt(message, key)
    recovered = decrypt(ciphertext, key)

    print("Message    :", message)
    print("Key (hex)  :", key.hex())
    print("Cipher hex :", ciphertext.hex())
    print("Recovered  :", recovered)

    # Proof that the wrong key reveals nothing usable.
    wrong_key = generate_key(len(key))
    try:
        print("Wrong key  :", decrypt(ciphertext, wrong_key))
    except UnicodeDecodeError:
        print("Wrong key  : (unreadable bytes, exactly as expected)")

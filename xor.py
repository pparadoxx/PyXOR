def encryption(message, key):
    """Encrypt the string and return the XOR'd string."""
    return "".join([chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(message)])

def decryption(encrypted_message, key):
    """Decrypt the XOR'd string and return the original string."""
    return encryption(encrypted_message, key)

# Example usage
message = "secret message"
key = "key"
encrypted_message = encryption(message, key)
decrypted_message = decryption(encrypted_message, key)

print(f"Message: {message}")
print(f"Key: {key}")
print(f"Decrypted Message: {decrypted_message}")
print(f"Encrypted Message: {encrypted_message}")
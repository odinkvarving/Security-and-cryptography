import math

def create_alphabet():
    alphabet = {}

    for i in range(0, 26):
        alphabet[chr(ord("A") + i)] = i

    alphabet["Æ"] = 26
    alphabet["Ø"] = 27
    alphabet["Å"] = 28

    return alphabet


def decrypt(message, alphabet, k):
    plaintext = ""

    for i in range(len(message)):
        if message[i] != " ":
            y = int(alphabet[message[i]])
            x = (y - k) % len(alphabet)
            plaintext += list(alphabet)[x]

    return plaintext.lower()


def brute_force(message, alphabet):
    for k in range(len(alphabet)):
        decrypted = decrypt(message, alphabet, k)
        print(f"k: {k}\t{decrypted}")


def main():

    message = "YÆVFB VBVFR ÅVBV"
    alphabet = create_alphabet()
    brute_force(message, alphabet)

    k = 17
    print("\nThe decrypted message: ")
    plaintext = decrypt(message, alphabet, k)
    print(f"k: {k}\t{plaintext}")


if __name__ == "__main__":
    main()
    
import math

def create_table():
    table = {}

    for i in range(0, 26):
        table[chr(ord("A") + i)] = i

    table["Æ"] = 26
    table["Ø"] = 27
    table["Å"] = 28

    return table


def decrypt(message, table, k):
    plaintext = ""

    for i in range(len(message)):
        if message[i] != " ":
            y = int(table[message[i]])
            x = (y - k) % len(table)
            plaintext += list(table)[x]

    return plaintext.lower()


def brute_force(message, table):
    for k in range(len(table)):
        decrypted = decrypt(message, table, k)
        print(f"k: {k}\t{decrypted}")


def main():

    message = "YÆVFB VBVFR ÅVBV"
    table = create_table()
    brute_force(message, table)

    k = 17
    print("\nThe decrypted message: ")
    plaintext = decrypt(message, table, k)
    print(f"k: {k}\t{plaintext}")


if __name__ == "__main__":
    main()
    
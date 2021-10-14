#include <iomanip>
#include <iostream>
#include <openssl/evp.h>
#include <openssl/sha.h>
#include <sstream>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

enum { KEYLENGTH = 20, ITERATION = 2048 }; 

/// Return hex string from bytes in input string.
string hex(const string &input) {
  stringstream hex_stream;
  hex_stream << hex << internal << setfill('0');
  for (auto &byte : input)
    hex_stream << setw(2) << (int)(unsigned char)byte;
  return hex_stream.str();
}

/// Return the SHA-1 (160-bit) hash from input.
string pbkdf2(const string &input) {
  string hash;
  hash.resize(160 / 8);
  unsigned char salt[] = "Saltet til Ola";

  PKCS5_PBKDF2_HMAC_SHA1((char*)&input[0], -1, salt, sizeof(salt), ITERATION, KEYLENGTH, (unsigned char*)&hash[0]);

  return hash;
}

int main() {
  cout << hex(pbkdf2("Passord987")) << endl;
}
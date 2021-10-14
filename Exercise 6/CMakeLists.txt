cmake_minimum_required(VERSION 3.1)

project(exercise)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fsanitize=address -std=c++1y -Wall -Wextra")

if(CMAKE_SIZEOF_VOID_P EQUAL 8)
  set(OPENSSL_ROOT_DIR "/usr/lib/ssl")
endif()

add_executable(pbkdf2 pbkdf2.cpp)
target_link_libraries(pbkdf2 ${OPENSSL_CRYPTO_LIBRARY})

#include <string.h>
#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

string update_string(string input) {
    
    char input_array[input.length() + 1];
    
    strncpy(input_array, input.c_str(), sizeof(input_array));
    
    string return_string = "";
    
    for (char c : input_array)
    {
        if (c == '&')
        {
            return_string += "&amp;";
        }
        else if (c == '<')
        {
            return_string += "&lt;";
        }
        else if (c == '>')
        {
            return_string += "&gt;";
        }
        else
        {
            return_string += c;
        }
    }
    return return_string;
}

int main(int argc, char const *argv[])
{
    cout << "Enter input:\n";
    string input;
    cin >> input;
    cout << "Result:\n"
         << update_string(input) + "\n";
    return 0;
}
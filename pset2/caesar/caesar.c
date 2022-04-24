#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

bool check_valid_key(string s);

int main(int argc, string argv[])
{
    // If your program is executed without any command-line arguments or with more than one command-line argument, your program should print 1
    // If any of the characters of the command-line argument is not a decimal digit, your program should print the message 1
    if (argc != 2 || !check_valid_key(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int key = atoi(argv[1]); // converts string to integer

    string plaintext = get_string("plaintext: ");

    printf("ciphertext: ");
    for (int i = 0, len = strlen(plaintext); i < len; i++)
    {
        char c = plaintext[i];
        if (isalpha(c)) // checks for alphabetic character
        {
            char m = 'A';
            if (islower(c)) // checks for lowercase character
            {
                m = 'a';
            }
            printf("%c", (c - m + key) % 26 + m);
        }
        else
        {
            printf("%c", c);
        }
    }
    printf("\n");
}

bool check_valid_key(string s)
{
    for (int i = 0, len = strlen(s); i < len; i++)
        if (!isdigit(s[i])) // checks for a digit 0-9
        {
            return false;
        }
    return true;
}

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    // asks for input between 1-9
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);
    // iterates through height inputted
    for (int i = 0; i < height; i++)
    {
        // print spaces
        for (int j = height - 1; j > i; j--)
        {
            printf(" ");
        }
        // print hashes
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
        // new line
        printf("\n");
    }
}
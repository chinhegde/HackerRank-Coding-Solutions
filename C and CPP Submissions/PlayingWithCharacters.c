#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{   char ch,s[100],sen[100],k;
    scanf("%c",&ch);
    scanf("%s",s);
    scanf("%c",&k);
    scanf("%[^\n]s",sen);
    printf("%c\n%s\n%s",ch,s,sen);
    return 0;
}


# include<iostream>
#define NO_OF_CHARS 256
using namespace std;

int firstNonRepeating(char *str)
{
    int i;
    int *freq = new int[NO_OF_CHARS];
    for(i=0; *(str+i); i++)
        freq[*(str+i)]++;
    cout<<endl;
    for(i=0; *(str+i); i++)
    {
        if(freq[*(str+i)] == 1)
        {
            return i;
        }
    }
    return -1;
}

int main()
{
    char str[256];
    cout<<"Enter a string: ";
    cin>>str;
    int r = firstNonRepeating(str);
    if(r == -1)
        cout<<"No non-repeating character present in given string. Either all of the characters are repeating or string is empty";
    else
        cout<<"First non-repeating character present in given string: "<<str[r];
    return 0;
}

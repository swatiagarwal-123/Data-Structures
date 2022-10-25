#include <iostream>
using namespace std;

int checkSorted(int a[], int n)
{
    int i, first = 0, second = 0;
    int c = 0;
    for (i=1; i<n; i++) {
        if (a[i] < a[i-1]) {
            c++;
            if (first == 0)
                first = i;
            else
                second = i;
        }
    }
    if (c > 2)
        return false;

    if (c == 0)
        return true;

    if (c == 2)
        swap(a[first-1], a[second]);

    else if (c == 1)
        swap(a[first-1], a[first]);

    for (i=1; i<n; i++)
        if (a[i] < a[i-1])
            return false;

    return true;
}

int main()
{
    int n, a[100];
    cout<<"Enter the size of the array: ";
    cin>>n;
    cout<<"Enter the elements of the array: ";
    for(int i=0; i<n; i++)
        cin>>a[i];
    if (checkSorted(a, n))
        cout << "Yes";
    else
        cout << "No";
    return 0;
}

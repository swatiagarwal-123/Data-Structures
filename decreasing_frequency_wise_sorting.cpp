#include <iostream>
using namespace std;

void insertionSort(int A[],int B[], int N)
{
    int i, j, t1, t2;
    for(i=1;i<=N-1;i++)
    {
        t1 = A[i];
        t2 = B[i];
        j=i-1;
        while(t1>A[j]&&j>=0)
        {
            A[j+1] = A[j];
            B[j+1] = B[j];
            j--;
        }
        A[j+1] = t1;
        B[j+1] = t2;
    }
}

int main()
{
    int i, j, n, c, x=0;
    cout<<"Enter total no. of elements: ";
    cin>>n;
    int a[n], f[n], r[n], s[n];
    cout<<"Enter the elements of array: "<<endl;
    for(i=0;i<n;i++)
    {
        cin>>a[i];
        f[i] = -1;
    }
    for(i=0;i<n;i++)
    {
        c = 1;
        for(j=i+1; j<n; j++)
        {
            if(a[i]==a[j])
            {
                c++;
                f[j] = 0;
            }
        }
        if(f[i] != 0)
            f[i] = c;
    }
    for(i=0;i<n;i++)
    {
        if(f[i]!=0)
        {
            r[x] = a[i];
            s[x] = f[i];
            x++;
        }
    }
    insertionSort(s, r, x);
    cout<<"Sorted array: "<<endl;
    for(i=0;i<x;i++)
    {
        for(j=0;j<s[i];j++)
            cout<<r[i]<<" ";
    }
    return 0;
}

//CodeForces round 665 - A

#include <bits/stdc++.h>
using namespace std;

main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, k, i, j, t, c=0;
    cin >> t;
    while (t--)
    {
        cin >> n >> k;

        if(n < k){
            cout << k - n << endl;
        }
        else if(n%2 == k%2){
            cout << 0 << endl;
        }
        else{
            cout << 1 << endl;
        }        
    }

    return 0;
}


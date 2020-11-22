#include<bits/stdc++.h>
using namespace std;

#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int mod=1000000007;
    int a,b,ans=0;
    sc2(a,b);
    for(;;){
        a*=3;
        b*=2;
        ans++;
        if (a>b) break;
    }
    printf("%d\n",ans);
    return 0;
}

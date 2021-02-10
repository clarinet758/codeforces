#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

bool d[1000005];
int main(){
    int n,m,k,p,t=1,x,y;
    sc3(n,m,k);
    rep(i,m) { sc1(p); d[p]=1; }
    rep(i,k) {
        if (d[t]) break;
        sc2(x,y);
        if (x==t) t=y;
        else if (y==t) t=x;
    }
    printf("%d\n",t);
    return 0;
}

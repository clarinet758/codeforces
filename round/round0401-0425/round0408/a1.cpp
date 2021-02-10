#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)


int w[205];
int main(){
    int mod=1000000007;
    int n,m,k,ans=mod;
    sc3(n,m,k);
    rep(i,n) sc1(w[i]);
    for(int i=m-1;i>=0;i--) if (w[i]<=k && w[i]>0) {
        ans=min(ans,(m-i-1));
        break;
    }
    for(int i=m;i<n;i++) if (w[i]<=k && w[i]>0) {
        ans=min(ans,(i-m+1));
        break;
    }
    printf("%d\n",ans*10);
    return 0;
}

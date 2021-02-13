#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int n,m,p=-1e9,q=1e9,ans=0;
    sc1(n);
    rep(i,n) {
        sc1(m);
        if(m>0) ans+=m;
        if(m<0 && m%2!=0) p=max(p,m);
        if(m>0 && m%2) q=min(q,m);
    }
    if (ans%2) printf("%d\n",ans);
    else if (ans==0 && p>-1e9) printf("%d\n",p);
    else if (ans%2==0) printf("%d\n",max(ans+p,ans-q));
    return 0;
}

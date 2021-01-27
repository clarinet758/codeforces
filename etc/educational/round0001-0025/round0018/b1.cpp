#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)

bool w[117];
int ans[117];
int main(){
    int n,k,p=0,mod;
    sc2(n,k);
    mod=n;
    vector <int> a(k);
    rep(i,k) sc1(a[i]);
    rep(i,k) {
        int l=a[i]%mod;
        for(;;) {
            if(l==0) {
                ans[i]=p+1;
                w[p]=1;
                mod--;
                for(;;){
                    if (w[p]==0) break;
                    p=(p+1)%n;
                }
                break;
            }
            p=(p+1)%n;
            if (w[p]==0) l--;

        }
    }
    rep(i,k-1) printf("%d ",ans[i]);
    printf("%d\n",ans[k-1]);
    return 0;
}

#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int n,m,ans=2e9+7,cnt=0;
    sc1(n);
    vector <int> a(n);
    rep(i,n) sc1(a[i]);
    sort(a.begin(),a.end());
    rep(i,n-1) {
        int x=abs(a[i+1]-a[i]);
        if (ans==x) cnt++;
        else if (ans>x) {ans=x; cnt=1;};
    }
    printf("%d %d\n",ans,cnt);
    return 0;
}

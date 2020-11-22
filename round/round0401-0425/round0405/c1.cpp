#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc2(a,b)  scanf("%d %d",&a,&b)

int x[100];
bool a[55];
int main(){
    int n,k;
    char s[10];
    sc2(n,k);
    int p=n-k+1;
    rep(i,p){
        scanf("%s",s);
        if (i==0) rep(j,k) x[j]=j%k;
        rep(j,55) a[j]=0;
        if (s[0]=='N') {
            x[i+k-1]=x[i];
        } else {
            int l=55;
            rep(e,k) a[x[i+e]]=1;
            rep(e,k) if (a[e]==0) l=e;
            x[i+k-1]=l;
        }
    }
    rep(i,n) {
        printf("%c%c%c",x[i]/25+'A',x[i]%25+'a',i==n-1?'\n':' ');
    }
    return 0;
}

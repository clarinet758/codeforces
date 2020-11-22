#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int n,k,x[100];
    char s[10];
    sc2(n,k);
    rep(i,100) x[i]=i;
    rep(i,n){
        scanf("%s",s);
        if (s[0]=='N')  x[i+k-1]=x[i];
    }
    rep(i,n)  printf("%c%c%c",x[i]/25+'A',x[i]%25+'a',i==n-1?'\n':' ');
    return 0;
}

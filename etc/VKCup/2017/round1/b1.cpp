#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define per(i,n)  for(int i=n-1;i>=0;--i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)
#define sl1(a)  scanf("%lld",&a)
#define sl2(a,b)  scanf("%lld %lld",&a,&b)
#define sl3(a,b,c)  scanf("%lld %lld %lld",&a,&b,&c)
#define PI 3.1415926535897932

int lcm(int a,int b) { return a*b/__gcd(a,b); }
//long long lcm(ll a,ll b) { return a*b/__gcd(a,b); }

/**
 * sort(ar.begin(),ar.end())
 * int sum=accumulate(ar.begin(),ar.end(),0);
 **/


int main(){
    int mod=1000000007;
    int n,m,ans;
    //scanf("%d %d",&n,&m);
    n=5;
    per (i,n) {
        printf("%d\n",i);
    }
    return 0;
}

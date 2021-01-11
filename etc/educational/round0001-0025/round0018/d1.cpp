#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sl1(a)  scanf("%lld",&a)
#define sl2(a,b)  scanf("%lld %lld",&a,&b)

long long w[65][3],mav=576460752303423488;
int main(){
    long long a,b,n,q,tf1=0,tf2;
    w[0][0]=1;
    w[0][1]=mav;
    w[59][0]=mav+1;
    rep(i,58) {
        w[i+1][0]=w[i][0]*2;
        w[i+1][1]=w[i][1]-w[i][0];
    }
    sl2(n,q);
    for (long long i=0;i<61;i++){
        tf1=tf1*2+1;
        if (tf1==n) { tf2=i; break; }
    }

    for (long long i=0ll;i<q;i++) {
        char s[100005];
        sl1(a);
        scanf("%s",s);
        long t=strlen(s);
        if (a%2) {
            b=0ll;
        } else {
            for(int j=58;j>0;j--){
                if (a==w[j][0]) {
                    b=j;break;
                } else if(a%w[j+1][0]==w[j][0]){
                    b=j;break;
                }
            }
        }
        for (long j=0;j<t;j++){
            if ( (b==tf2 && s[j]=='U') || (a%2 && (s[j]=='L' || s[j]=='R')) ) {
                //cout<< a<< " " << b << " "<< s[j] << endl;
            } else if (s[j]=='U' && a%(w[b][0]*4ll)==w[b][0]%(w[b][0]*4ll)) {
                a+=w[b][0];b++;
            } else if (s[j]=='U') {
                a-=w[b][0];b++;
            } else if (s[j]=='L') {
                a-=w[b-1][0];b--;
            } else if (s[j]=='R') {
                a+=w[b-1][0];b--;
            }
        }
        cout<< a << endl;
    }
    return 0;
}

#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int n,k;
    sc2(n,k);
    vector <int> ans;
    for(int i=2;i<334;i++) {
        if(i==2 && k==1) {ans.push_back(n); k=0;}
        //cout<< n ;
        while (n%i==0 && k>0) {
            if (k>1) {
                ans.push_back(i);
                k--;
                n/=i;
            } else {
                ans.push_back(n);
                k=0;
                n=1;
            }
        }
    }
    if (k>0) {
        printf("-1\n");
    } else {
        bool f=0;
        for(auto x:ans) {
            if (f) {
                printf(" %d",x);
            }else {
                printf("%d",x);
                f=1;
            }
        }
        puts("");
    }
    return 0;
}

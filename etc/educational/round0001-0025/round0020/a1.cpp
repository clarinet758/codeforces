#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define per(i,n)  for(int i=n-1;i>=0;--i)
#define sc2(a,b)  scanf("%d %d",&a,&b)


int main(){
    int mod=1000000007;
    int n,k;
    sc2(n,k);
    vector < vector<int> > ans(n, vector <int> (n,0));

    if (k>n*n) {
        printf("-1\n");
        return 0;
    }

    rep(i,n) rep(j,n){
        if (k==0) {i=n;j=n;break;}
        if (ans.at(i).at(j)==0) {
            ans.at(i).at(j)=1;
            ans.at(j).at(i)=1;
            if(i!=j) k-=2; 
            else k--;
        } 
        if (k==1) {ans.at(i+1).at(i+1)=1; k--;}
    }
    rep(i,n) rep(j,n) {
        if (j<n-1) printf("%d ", ans.at(i).at(j));
        else printf("%d\n", ans.at(i).at(j));
    }
    return 0;
}

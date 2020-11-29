#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int t,n,x,y;
    sc1(t);
    rep(i,t) {
        sc1(n);
        vector<set<int>> g(n);
        rep(j,n) {
            sc2(x,y);
            --x,--y;
            g[x].insert(y);
            g[y].insert(x);
        }
        vector<int> val(n,1);
        queue<int> leafs;
        rep(j,n)  if (g[j].size()==1) leafs.push(j);

        while (!leafs.empty()) {
            int v=leafs.front();
            leafs.pop();
            int to=*g[v].begin();
            val[to] += val[v];
            val[v]=0;
            g[v].clear();
            g[to].erase(v);
            if (g[to].size()==1) leafs.push(to);
        }
        long long ans=0ll;
        rep(j,n) {
            ans+=val[j]*1ll*(val[j]-1)/2;
            ans+=val[j]*1ll*(n-val[j]);
        }
        printf("%lld\n",ans);
    }
    return 0;
}

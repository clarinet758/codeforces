#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int cnt[150005]; 
struct UnionFind {
    vector<int> data;
    UnionFind(int size) : data(size, -1) {}
    bool unite(int x, int y) {
        x=root(x), y=root(y);
        if (x!=y) {
            if (data[y]<data[x]) {
                swap(x, y);
            }
            data[x]+=data[y], data[y]=x;
        }
        return x!=y;
    }

    bool find(int x, int y) {
        return root(x)==root(y);
    }

    int root(int x) {
        return data[x]<0 ? x : data[x]=root(data[x]);
    }

    int size(int x) {
        return -data[root(x)];
    }
};


int main(){
    int mod=1000000007;
    int n,m;
    sc2(n,m);
    UnionFind uf(n);
    rep(i,m) {
        int a,b;
        sc2(a,b);
        a--;b--;
        cnt[a]++;cnt[b]++;
        uf.unite(a,b);
    }

    bool f=1;
    rep(i,n) {
        if (uf.size(i)!=cnt[i]+1) f=0;
    }
    printf("%s\n",f?"YES":"NO");
    return 0;
}

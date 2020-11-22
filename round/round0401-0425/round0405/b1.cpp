#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define per(i,n)  for(int i=n-1;i>=0;--i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

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

int chk[150005];
int main(){
    bool f=1;
    int n,m,a,b,ans;
    sc2(n,m);
    UnionFind uf(n+1);
    rep(i,m) {
        sc2(a,b);
        uf.unite(a,b);
        chk[a]++;
        chk[b]++;
    }
    rep(i,n+1){
        if (uf.size(i)!=chk[i]+1) f=0;
    }
    printf("%s\n",f?"YES":"NO");
    return 0;
}

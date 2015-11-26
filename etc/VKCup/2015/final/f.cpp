#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;

const int MAXN=1000001;
int a[MAXN];
int b[MAXN];
int dp[MAXN];
int n;

int dfs(int cur){
    if(b[cur]==0){
        return 0;
    }
    int& ret=dp[cur];
    if(ret>0){
        return ret;
    }
    ret=0;
    for(int i=2;i*cur<MAXN;i++){
        ret=max(ret,dfs(i*cur));
    }
    ret+=b[cur];
    return ret;
}

int main(){
    for(int i=0;i<MAXN;i++){
        a[i]=0;
        b[i]=0;
        dp[i]=0;
    }
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
        b[a[i]]++;
    }
    int ans=0;
    for(int i=1;i<MAXN;i++){
        if(dp[i]==0){
            ans=max(ans,dfs(i));
        }
    }
    printf("%d\n",ans);
    return 0;
}

#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


int main(){
    long long n,k;
    scanf("%lld %lld",&n,&k);
    if (k<=(n+1)/2){
        printf("%lld\n",1+(k-1)*2);
    }else{
        printf("%lld\n",(k-(n+1)/2)*2);
    }
    return 0;
}

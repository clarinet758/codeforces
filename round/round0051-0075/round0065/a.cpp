#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


int main(){
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        char c[100];
        scanf("%s",&c);
        string chk=c;
        int tmp=chk.length();
        if(tmp<=10){
            printf("%s\n",c);
        }else{
            printf("%c%d%c\n",c[0],tmp-2,c[tmp-1]);
        }
    }
    return 0;
}

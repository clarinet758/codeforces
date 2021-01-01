#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int cl[5],cr[5];
bool sl[100005]; 

int main(){
    int total=0;
    char s[100005]; 
    scanf("%s",s);
    long t=strlen(s),kugiri=t-1l;
    bool sentou=0;
    for (long i=0;i<t;i++){
        int x=s[i]-'0';
        total=(total+x)%3;
        if (x==0 && kugiri==t-1l) kugiri=i;
        if (x==0) sentou=1;
        if (sentou) cr[x%3]++;
        else cl[x%3]++;
    }

    if (total==0) {
        true;
    } else if (total==1 && cl[1]==1 && cl[0]+cl[2]+cr[0]+cr[1]+cr[2]==0) {
        printf("-1\n"); return 0;
    } else if (total==1 && cl[2]==2 && cl[0]+cl[1]+cr[0]+cr[1]+cr[2]==0) {
        printf("-1\n"); return 0;
    } else if (total==2 && cl[2]==1 && cl[0]+cl[1]+cr[0]+cr[1]+cr[2]==0) {
        printf("-1\n"); return 0;
    } else if (total==2 && cl[1]==2 && cl[0]+cl[2]+cr[0]+cr[1]+cr[2]==0) {
        printf("-1\n"); return 0;
    } else if ((total==1 && (s[0]-'0')%3==1 && s[1]-'0'==0 && s[2]-'0'==0 && cl[2]+cr[2]>1)){
        int chk0=0;
        for (long i=t-1;i>=0;i--) {
            if ((s[i]-'0')%3==2 && chk0==0) {sl[i]=1; chk0++;}
            else if ((s[i]-'0')%3==2 && chk0==1) {sl[i]=1; break;}
        }
    } else if (total==1 && cr[1]+cl[1]>0){
        for (long i=t-1;i>=0;i--) if ((s[i]-'0')%3==1) {sl[i]=1; break;}
    } else if (total==1 && cr[1]+cl[1]==0 && cl[2]+cr[2]>1){
        int chk1=0;
        for (long i=t-1;i>=0;i--) {
            if ((s[i]-'0')%3==2 && chk1==0) {sl[i]=1; chk1++;}
            else if ((s[i]-'0')%3==2 && chk1==1) {sl[i]=1; break;}
        }
    } else if (total==2 && cr[2]>0){
        for (long i=t-1;i>=0;i--) if ((s[i]-'0')%3==2) {sl[i]=1; break;}
    } else if (total==2 && cr[2]+cl[2]==0 && cr[1]+cl[1]>1){
        int chk1=0;
        for (long i=t-1;i>=0;i--) {
            if ((s[i]-'0')%3==1 && chk1==0) {sl[i]=1; chk1++;}
            else if ((s[i]-'0')%3==1 && chk1==1) {sl[i]=1; break;}
        }
    } else if ((total==2 && cr[2]+cl[2]>0 && cr[1]+cl[1]<2)||(total==2 && cr[2]+cl[2]>1)){
        for (long i=t-1;i>=0;i--) if ((s[i]-'0')%3==2) {sl[i]=1; break;}
    } else if ((total==2 && (s[0]-'0')%3==2 && s[1]-'0'==0 && cr[1]>1)){
        int chk2=0;
        for (long i=t-1;i>=0;i--) {
            if ((s[i]-'0')%3==1 && chk2==0) {sl[i]=1; chk2++;}
            else if ((s[i]-'0')%3==1 && chk2==1) {sl[i]=1; break;}
        }
    } else if (total==2 && cr[2]+cl[2]>0){
        for (long i=t-1;i>=0;i--) if ((s[i]-'0')%3==2) {sl[i]=1; break;}
    }

    for (long i=0;i<t-1;i++) {
        int xxx=s[i]-'0';
        if (xxx>0 && sl[i]==0) break;
        else sl[i]=1;
    }
    for (long i=t-1;i>=0;i--) {
        int xxx=s[i]-'0';
        if (xxx>0 && sl[i]==0) break;
        if (xxx==0 && sl[i]==1) {sl[i]=0; break;}
    }
    bool taisaku=0;
    for(long i=0;i<t;i++){
        if (sl[i]==0) {
            if (taisaku==1 || s[i]-'0'>0) {
                taisaku=1;
                printf("%c",s[i]);
            }else if (s[i]-'0'==0 && taisaku==0) {
                printf("%c",s[i]);
                break;
            }
        }
    }
    puts("");

    return 0;
}

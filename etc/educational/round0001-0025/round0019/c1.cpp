#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)

//BEGIN CUT HERE
template <typename T,typename E>
struct SegmentTree{
  typedef function<T(T,T)> F;
  typedef function<T(T,E)> G;
  int n;
  F f;
  G g;
  T d1;
  E d0;
  vector<T> dat;
  SegmentTree(){};
  SegmentTree(int n_,F f,G g,T d1,
	      vector<T> v=vector<T>()):
    f(f),g(g),d1(d1){
    init(n_);
    if(n_==(int)v.size()) build(n_,v);
  }
  void init(int n_){
    n=1;
    while(n<n_) n*=2;
    dat.clear();
    dat.resize(2*n-1,d1);
  }
  void build(int n_, vector<T> v){
    for(int i=0;i<n_;i++) dat[i+n-1]=v[i];
    for(int i=n-2;i>=0;i--)
      dat[i]=f(dat[i*2+1],dat[i*2+2]);
  }
  void update(int k,E a){
    k+=n-1;
    dat[k]=g(dat[k],a);
    while(k>0){
      k=(k-1)/2;
      dat[k]=f(dat[k*2+1],dat[k*2+2]);
    }
  }
  inline T query(int a,int b){
    T vl=d1,vr=d1;
    for(int l=a+n,r=b+n;l<r;l>>=1,r>>=1) {
      if(l&1) vl=f(vl,dat[(l++)-1]);
      if(r&1) vr=f(dat[(--r)-1],vr);
    }
    return f(vl,vr);
  }
};
//END CUT HERE

char s[100005];
vector <int> ans;
int main(){
    vector <int> w;
    scanf("%s",s);
    long dd=strlen(s);
    SegmentTree<int,int> rmq(100005,[](int a,int b){return min(a,b);}, [](int a,int b){return b;}, INT_MAX);
    for (long i=0;i<dd;i++) rmq.update(i,s[i]-'a');
    
    for(long i=0;i<dd;i++){
        if(w.empty()) {
            w.push_back(s[i]-'a');
        } else {
            int x=rmq.query(i,dd+1);
            while(!w.empty()) {
                auto y=w.back();
                if (y>x) break;
                ans.push_back(y+'a');
                w.pop_back();
            }
            w.push_back(s[i]-'a');
        }
    }
    int vs=w.size();
    rep(i,vs) {
        int vv=w.back();
        ans.push_back(vv+'a');
        w.pop_back();
    }
    for (auto e:ans) printf("%c",e);
    puts("");
    return 0;
}

#define PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_A

#include <iostream>
#include "cpp/lib/prime_factorize.hpp"
using namespace std;


int main(){
    int n; cin >> n;
    auto r = prime_factorize(n);
    cout << n << ":";
    for (auto pe:r){
        for (int i=0; i<pe.second;++i){
            cout << " " << pe.first;
        }
    }
    cout << endl;
}
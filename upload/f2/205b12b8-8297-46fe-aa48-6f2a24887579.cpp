#include <iostream>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <cmath>
#define open(a,b) freopen(a,"r",stdin);freopen(b,"w",stdout);

using namespace std;
typedef long long ll;
ll prime[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59};
int pcnt;

struct dump
{
	int px[20];
	bool tag;
	dump();
	memset(px,0,sizeof(px));
	dump(ll a){
		tag=true;
		int pos=0;
		for (int i = 0; i < pcnt; ++i)
		{
			if(a==1)
				break;
			while(a%prime[i]==0){
				++px[pos];
			}
			if(px[pos]){
				if(pos){
					if(px[pos]>px[pos-1]){
						tag=false;
						return;
					}
				}
				pos++;
			}
		}
	}
}arr[50000];

int tot;

int main(){
	pcnt=sizeof(prime)>>2;
	return 0;
}
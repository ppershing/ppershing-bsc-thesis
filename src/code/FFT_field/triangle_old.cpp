#include <stdio.h>
#include <algorithm>
#include <vector>
#include <cassert>
using namespace std;

#define MAX 1000010

#define FOR(q,n) for(int q=0; q<n; q++)

int n;
vector<long long> data,data2,holder;
vector<int> bitReversal;
int L;

//#define FFT_SIZE 64

//long long  prime=193; //2114977793;
//long long  unity=125; //1134133719;
//long long  revUnity=105;//72614673;
//long long  sizeInverse=190; //2114973759;

#define FFT_SIZE 8
long long  prime=41; //2114977793;
long long  unity=14; //1134133719;
long long  revUnity=3;//72614673;
long long  sizeInverse=36; //2114973759;

//#define FFT_SIZE (1<<20)
//long long  prime=2114977793;
//long long  unity=1097923455;
//long long  revUnity=72614673;
//long long  sizeInverse=2114973759;

long long rootsOfUnity[MAX];
void precomputeRootsOfUnity(long long unity){
    rootsOfUnity[0]=1; //unity;
    for (int q=1; q<FFT_SIZE; q++) {
        rootsOfUnity[q]=(rootsOfUnity[q-1]*unity)%prime;
        assert(rootsOfUnity[q]!=1);
    }
    assert((rootsOfUnity[FFT_SIZE-1]*unity)%prime==1);
}

// {{{ precomputeReversal 
void precomputeReversal(){
    bitReversal.resize(FFTSize);

    int rev=0;
    for (int i=0;i<FFTSize-1;i++) {
        bitReversal[i]=rev;

        int mask=FFTSize/2;
        while (rev>=mask){
            rev-=mask;
            mask/=2;
        }
        rev+=mask;
    }
    bitReversal[FFTSize-1]=FFTSize-1;
}
// }}}

// {{{ getLog
int getLog(int x){
    int t=0;
    while (x>0) {x/=2; t++;}
    return t;
}
// }}}

// {{{ init
void init(){
    scanf("%d",&n);
    data.resize(FFT_SIZE);
    data2.resize(FFT_SIZE);
    FOR(q,FFT_SIZE) data[q]=0;

    FOR(q,n) {
        long long w=q;
        w*=q;
        w%=n;
        data[w]++;
        data2[n-w]++;
    }
}
// }}}

void make_fourier(vector<long long> &data,int rootSkip){
 if (n==1) return;
 int size=data.size();
 if (size==1) return; 
 
 vector<long long> tmp1,tmp2;
 tmp1.resize(size/2);
 for (int q=0; q<size/2; q++)
     tmp1[q]= data[2*q];
 make_fourier(tmp1,rootSkip*2); 
 
 tmp2.resize(size/2);
 for (int q=0; q<size/2; q++)
     tmp2[q]= data[2*q+1];
 make_fourier(tmp2,rootSkip*2);
     
 for (int q=0; q<size/2; q++) {
     data[q]=(tmp1[q]+(long long)rootsOfUnity[rootSkip*q]*tmp2[q])%prime;
     data[size/2+q]=(
                (tmp1[q]-(long long)rootsOfUnity[rootSkip*q]*tmp2[q])%prime
             +prime)%prime;
 }

}


int main(){
    init();
    

    // forward
    precomputeReversal();
    precomputeRootsOfUnity(unity);  
    moveData(data,holder);
    make_fourier(holder,1);
    moveDeta(data2,holder);
    make_fourier(holder,1);
    //convolution
    
    for (int q=0; q<FFT_SIZE; q++) data[q]= ((long long)
            data[q]*data[q])%prime;
    //backward
    precomputeRootsOfUnity(revUnity);
    make_fourier(data,1);
    //backward scaling
    for (int q=0; q<FFT_SIZE; q++) data[q]=
        ((long long) data[q]*sizeInverse)%prime;

    for (int q=0; q<FFT_SIZE; q++) printf("%lld\n",data[q]);

}

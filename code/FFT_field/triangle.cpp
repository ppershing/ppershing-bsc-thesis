#include <stdio.h>
#include <algorithm>
#include <vector>
#include <cassert>
using namespace std;

#define MAX 1500010

#define FOR(q,n) for(int q=0; q<n; q++)

int n;
vector<long long> data,data2,holder;
vector<int> bitReversal;

/*
#define LOG_SIZE 6
#define FFT_SIZE 64

long long  prime=193; //2114977793;
long long  unity=125; //1134133719;
long long  revUnity=105;//72614673;
long long  sizeInverse=190; //2114973759;
*/

/*
#define LOG_SIZE 3
#define FFT_SIZE (1<<3)
long long  prime=41; //2114977793;
long long  unity=14; //1134133719;
long long  revUnity=3;//72614673;
long long  sizeInverse=36; //2114973759;
*/


#define LOG_SIZE 20
#define FFT_SIZE (1<<20)
long long  prime=2114977793;
long long  unity=1097923455;
long long  revUnity=72614673;
long long  sizeInverse=2114975776;



// {{{ precomputeRootsOfUnity
long long rootsOfUnity[MAX];
void precomputeRootsOfUnity(long long unity){
    rootsOfUnity[0]=1; //unity;
    for (int q=1; q<FFT_SIZE; q++) {
        rootsOfUnity[q]=(rootsOfUnity[q-1]*unity)%prime;
        assert(rootsOfUnity[q]!=1);
    }
    assert((rootsOfUnity[FFT_SIZE-1]*unity)%prime==1);
}
// }}}

// {{{ precomputeReversal 
void precomputeReversal(){
    bitReversal.resize(FFT_SIZE);

    int rev=0;
    for (int i=0;i<FFT_SIZE-1;i++) {
        bitReversal[i]=rev;

        int mask=FFT_SIZE/2;
        while (rev>=mask){
            rev-=mask;
            mask/=2;
        }
        rev+=mask;
    }
    bitReversal[FFT_SIZE-1]=FFT_SIZE-1;
}
// }}}


// {{{ init
void init(){
    scanf("%d",&n);
    data.resize(FFT_SIZE);
    FOR(q,FFT_SIZE) data[q]=0;

    FOR(q,n) {
        long long w=q;
        w*=q;
        w%=n;
        data[w]++;
    }
}
// }}}

// {{{ make_fourier
void make_fourier(vector<long long> &data){
    int step=1;
    long long int size=FFT_SIZE/2;

    for (int level=1; level<=LOG_SIZE; level++){
      //  printf("in level %d\n",level);
        int increment=step*2;

        for(int q=0; q<step; q++) {
            for (int i=q; i<FFT_SIZE; i+=increment) {
                int rr=(i*size)&(FFT_SIZE-1);
               // printf("%d %d ",level,i);
                long long r=rootsOfUnity[rr];
                //printf("using root of unity %d %d\n",rr,r);
                
                long long t=(data[i+step]*r)%prime;
                data[i+step]=(data[i]+prime-t)%prime;
                data[i]=(data[i]+t)%prime;
            }
        }
        size/=2;
        step*=2;
    }
}
// }}}

void moveData(vector<long long> &from,vector<long long> &to){
 for (int q=0; q<FFT_SIZE; q++)
     to[bitReversal[q]]=from[q];
     
}

int main(){
    init();
    

    data[0]--;

    precomputeReversal();
    precomputeRootsOfUnity(unity);  
    holder.resize(FFT_SIZE);
    long long totalsum=0;
    // forward
    moveData(data,holder);
    make_fourier(holder);
   
    data2.resize(FFT_SIZE);
    //convolution    
    for (int q=0; q<FFT_SIZE; q++) data2[q]= ((long long)
            holder[q]*(long long)holder[q])%prime;
    //backward
    
    moveData(data2,holder);
    precomputeRootsOfUnity(revUnity);
    make_fourier(holder);
    
    //backward scaling
    for (int q=0; q<FFT_SIZE; q++) data2[q]=
        ((long long) holder[q]*(long long)sizeInverse)%prime;

    for (int q=0; q<FFT_SIZE; q++) assert(data2[q]<n*50);

    for (int q=0; q<FFT_SIZE; q++) 
            totalsum+=(long long)data[q%n]*(long long)data2[q];
//    for (int q=0; q<FFT_SIZE; q++) printf("%d %d\n",(int)data[q%n],(int)data2[q]);
  //  printf("totalsum %d\n",(int)totalsum);
   

    
   
    for (int q=0; q<FFT_SIZE; q++) 
                totalsum+=(long long)data[q]*(long long)data[(2*q)%n];

    printf("%lld\n",totalsum/2);
}

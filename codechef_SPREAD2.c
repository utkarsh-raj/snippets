#include<stdio.h>
int main(){
    int i,t;
    scanf("%d",&t);
    for(i=0;i<t;i++){
        int n,j;
        scanf("%d",&n);
        long long int arr[n],c=0,count=0,sum=0;
        for(j=0;j<n;j++)
            scanf("%lld",&arr[j]);
        long int start=0;
        while(c<n-1){
            for(j=start;j<=c;j++){
                sum=sum+arr[j];
            }
            start=c+1;
            c=c+sum;
            count++;
        }
        printf("%lld\n",count);
    }
    return 0;
}

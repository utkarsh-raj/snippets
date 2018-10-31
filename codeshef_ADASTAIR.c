#include <stdio.h>

int main() {
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int n,k,a[129],i,count=0,diff=0,flag;
        scanf("%d",&n);
        scanf("%d",&k);
        for(i=1;i<=n;i++)
        {
            scanf("%d ",&a[i]); 
        }
         flag = a[1];
        while(flag>k)
           {
              
               flag -= k;
               count++;
               
               
           }
        for(i=1;i<n;i++)
        {
            diff = a[i+1]-a[i];
            
           while(diff>k)
           {
               diff -= k;
               count++;
              
               
           }
           
        }
        printf("%d\n",count);
        
    }
    
    
	//code
	return 0;
}

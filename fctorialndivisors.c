#include<stdio.h>
int main()
{
	int i,n,a=1,b;
	printf("Enter a number: ");
	scanf("%d",&n);
	int c[n];
	for (i=n,b=0;i>=1;i--,b++)
	{
		if(n%i==0)
		{	
			c[b]=i;
			printf("%d ",c[b]);
		}
		a*=i;
	}
	printf("are the divisors of %d\n",n);
	printf("%d is Factorial of %d.\n",a,n);
	return 0;
}

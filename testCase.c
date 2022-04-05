#include <stdio.h>

int main(void) {
    int n = 0;
    scanf("%d",&n);
    for(long i=0;i<n;i++)
    {
        long long start = 0,end = 0;
        scanf("%lld %lld",&start,&end);
        long min_steps = 0;
        int check_prime(long long a)
            {
               long long c;

               for ( c = 2 ; c <= a - 1 ; c++ )
               {
                  if ( a%c == 0 )
                 return 0;
               }
               return 1;
            }
        while(start<end)
        {
            if(check_prime(start+2) == 1)
            {
                start = start+2;
                min_steps+=1;

            }
            else
            {
                start+=1;
                min_steps+=1;
            }
        }
        printf("%d",min_steps);
    }



	// your code goes here
	return 0;
}

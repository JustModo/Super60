#include<stdio.h>
void main(){
int a;
printf("Enter value");
scanf("%d",&a);
long long int x=0,y=1,z,count=1;
for (int i=0;i<=a;i++){
    for (int j=0;j<=i;j++){
        z=x;
        x+=y;
        count++;
        if(count%2==0)
        printf("%d\t",x);
        if (count%2==1)
        printf("-%d\t",x);
        y=z;
    }
    printf("\n");
}


}
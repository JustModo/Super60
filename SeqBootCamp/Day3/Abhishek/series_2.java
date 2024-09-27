import java.util.*;
public class series_2 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int a=1;
        if(n>0)
        System.out.println("1");
        for(int i=4;a<n;i=i+4)
        {   if(i%12==0)
            continue;
            a=a+i;
            System.out.println(a);
            
        }
    }
}
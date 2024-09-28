import java.util.*;
public class base {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt(),s=0,b=1;
        while(a!=0)
        {int t=a%2;
            s=s+t*b;
            b=b*10;
            a=a/2;
        }
        System.out.println(""+s);
}
}
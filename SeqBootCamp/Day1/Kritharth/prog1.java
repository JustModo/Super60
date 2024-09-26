import java.util.Scanner;


public class prog1 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum = 1;
        int sum1 = 0;
        int count = 0;
        for (int i = 0; sum < n; i++) {
            sum+=i;
            if(sum>n){break;}
            System.out.print(sum +"\t");
            sum1+=sum;
            count++;
        }
        System.out.println();
        System.out.println("Count: "+count);
        System.out.println("Sum: "+sum1);
        sc.close();
    }
}
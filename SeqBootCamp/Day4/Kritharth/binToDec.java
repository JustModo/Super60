package SeqBootCamp.Day4.Kritharth;

import java.util.Scanner;

public class binToDec {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int bn = sc.nextInt();
        int dc = 0;
        int i = 0;
        int rem;
        while (bn != 0) {
            rem = bn%10;
            dc = dc + rem*(int)Math.pow(2, i);
            i++;
            bn/=10;
        }

        System.out.println(dc);
        sc.close();
    }
    
}

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
            if(rem !=0 || rem != 1){
                System.out.println("Enter a valid binary number!");
                return;
            }
            dc = dc + rem*(int)Math.pow(2, i);
            i++;
            bn/=10;
        }

        System.out.println("Decimal Value"+ dc);
        sc.close();
    }
    
}

package SeqBootCamp.Day4.Kritharth;

import java.util.Scanner;

public class decToBin {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int dec = sc.nextInt();
        int bin = 0;
        int rem;
        while (dec !=0) {
            rem = dec%2;
            bin = (bin*10)+rem;
            dec/=2;
        }
        System.out.println(dec);
    }
}

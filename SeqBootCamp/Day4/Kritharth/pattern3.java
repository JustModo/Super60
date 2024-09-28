package SeqBootCamp.Day4.Kritharth;
// 1	5	14	28	47	71	100	134	173	217	266	320	379	443	512	586

import java.util.Scanner;

public class pattern3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int dif = 4;
        int n = sc.nextInt();
        int a[] = new int[n];
        a[0] = 1;
        for (int i = 1; i < n; i++) {
            a[i] = a[i-1] + dif;
            dif+=5;
        }
        for (int i = 0; i < a.length; i++) {
            System.out.print(a[i]+"  ");
        }
    }
}

package SeqBootCamp.Day4.Kritharth;

import java.util.Scanner;

// 1	3	5	9	15	25	41	67	109	177	287	465	753	1219	1973	3193
public class pattern4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a[] = new int[n];
        a[0] = 1;
        a[1] = 3;
        a[2] = 5;
        for (int i = 3; i < a.length; i++) {
            a[i] = a[i-1]+((a[i-1] - a[i-2])+(a[i-2]-a[i-3]));
        }
        for (int i = 0; i < a.length; i++) {
            System.out.print(a[i] + "  ");
        }
        sc.close();
    }
}

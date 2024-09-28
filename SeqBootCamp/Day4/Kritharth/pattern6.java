package SeqBootCamp.Day4.Kritharth;
// 6	-8	10	-14	20	-30	46	-72	114	-182	292	-470	758	-1224	1978	-3198

import java.util.Scanner;

public class pattern6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a[] = new int[n];
        a[0] = 6;
        a[1] = 8;
        a[2] = 10;
        int dif;
        for ( int i = 3; i < a.length; i++) {
            dif = (a[i-1]-a[i-2])+(a[i-2]-a[i-3]);
            a[i] = a[i-1] + dif;
            
        }
        for (int j = 0; j < a.length; j++) {
            System.out.print(a[j]*(int)Math.pow(-1, j)+"  ");
        }
        sc.close();
    }
}

package SeqBootCamp.Day4.Kritharth;
// 1			
// -1	2		
// -3	5	-8	
// 13	-21	34	-55
// N Rows			

import java.util.Scanner;

public class pattern9 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a[] = new int[n];
        a[0] = 1;
        a[1] = 1;
        
        for(int i = 2; i < n; i++) {
            a[i] = a[i-1] + a[i-2];
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i+1; j++) {
                System.out.print(a[i]);
            }
        }
    }
}

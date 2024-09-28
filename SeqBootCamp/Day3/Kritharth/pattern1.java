package SeqBootCamp.Day3.Kritharth;
//1,4,7,12,23

import java.util.Scanner;

public class pattern1 {
    static Scanner sc = new Scanner(System.in);
    static int n = sc.nextInt();
    static int a[] = new int[n];
    
    public static void intNext(){
        a[0] = 1;
        a[1] = 4;
        a[2] = 7;        
        for (int i = 3; i < n; i++) {
            a[i] = a[i-1]+a[i-2]+a[i-3];
        }
         for (int i = 0; i < a.length; i++) {
            System.out.println(a[i]);
         }
    }
    public static void main(String[] args) {
        
        System.out.println("Enter the number of terms: ");
        
            intNext();
        
    }
}

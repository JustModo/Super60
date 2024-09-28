package SeqBootCamp.Day3.Kritharth;
//1,5,13,29,49,77

import java.util.Scanner;

public class pattern2 {
    static Scanner sc = new Scanner(System.in);
    static int n = sc.nextInt();
    static int a[] = new int[n];
    static void pat(){
        int mul = 4;
        a[0] = 1;
        // int j = 1;
        // for (int i = 1; i < n; i++) {
            
        //     if(mul%12!=0){
        //         a[i] = a[i-1] + mul;    
        //     }
        //     mul+=4;
        //     // j++;
        // }
        int count=1;
        
        for (int i = 0; count<n; i++) {
            if (mul%12!=0) {
                a[count] = a[count-1]+mul;
                count++;
            }
            mul+=4;
        }
        for (int i = 0; i < n; i++) {
            System.out.println(a[i]);
        }
        
    }
    public static void main(String[] args) {
        pat();
        
    }
}

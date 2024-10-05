package SeqBootCamp.Day4.Kritharth;

			

import java.util.Scanner;
// 1
// 2	4		
// 7	11	16	
// 22	29	37	46


public class pattern8 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int num = 1,count=0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i+1; j++) {
                num += count;
                count++;
                System.out.print(num+"  ");
                
            }
            System.out.println();
            sc.close();
        }
    }    
}

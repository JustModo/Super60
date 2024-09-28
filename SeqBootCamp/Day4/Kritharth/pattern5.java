package SeqBootCamp.Day4.Kritharth;

// 1	-4	15	-34	61	-96	139	-190	249	-316	391	-474	565	-664	771	-886

import java.util.Scanner;


public class pattern5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int num = 1;
        int dif=3;
        for (int i = 0; i < n; i++) {
            System.out.print(num*(int)Math.pow(-1, i)+"  ");
            num += dif;
            dif+=8;
        }
        
        
        
        sc.close();
        
    }
}

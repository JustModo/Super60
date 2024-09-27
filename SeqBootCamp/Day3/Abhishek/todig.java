import java.util.*;
import java.math.*;

public class qwe {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(), b = a, n,n1;
        for (n = 0; a != 0;) {
            n++;
            a = a / 10;
        }
        n1=n;
        a=b;
        System.out.println(n + "\n");
        String m[] = new String[n];
        for (int i = n - 1; i >= 0; i--) {
            int t = a % 10;
            System.out.println("t="+t);
            switch (t) {
                case 1:
                    m[i] = "One ";
                    break;
                case 2:
                    m[i] = "Two ";
                    break;
                case 3:
                    m[i] = "Three ";
                    break;
                case 4:
                    m[i] = "four ";
                    break;
                case 5:
                    m[i] = "five ";
                    break;
                case 6:
                    m[i] = "Six ";
                    break;
                case 7:
                    m[i] = "seven ";
                    break;
                case 8:
                    m[i] = "eight ";
                    break;
                case 9:
                    m[i] = "nine ";
                    break;
                case 0:
                    m[i] = "Zero ";
                    break;

            }
            a=a/10;

        }
        for (int i = 0; i <= n1 - 1; i++)
            System.out.print(m[i]);

    }

}
//extremely inefficent but works.. :)

import java.util.Scanner;

public class prog3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int mul = 1;
        for (int i = 4; mul < n; i*=4) {
            System.out.println(mul+"  ");
            mul*=-i;

        }
        sc.close();
    }
}

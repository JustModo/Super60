
import java.util.Scanner;

public class prog_2 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int mul = 3;
            for (int i = 1; mul < n; i++) {
                if(i%5 == 0)
                {
                    continue;
                }
                mul*=i;
                if (mul < n) {
                    break;
                }
                System.out.print(mul +"  ");
            }
        }
    }
}

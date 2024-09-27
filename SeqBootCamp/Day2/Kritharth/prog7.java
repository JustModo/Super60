
import java.util.Scanner;

public class prog7 {

   
    public static void main(String[] args) {
        int a[] = new int[3];
        int temp;
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < a.length; i++) {
            a[i] = sc.nextInt();
        }
       for (int i = 0; i < a.length; i++) {
        for (int j = i+1; j < a.length; j++) {
            if (a[i]>a[j]) {
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
        }
        System.out.println("Largest= "+a[2]);
        System.out.println("Second Largest= "+a[1]);
        sc.close();
    }
}

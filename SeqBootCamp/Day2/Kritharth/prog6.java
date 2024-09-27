import java.util.Scanner;

//Write a program to accept a double value.
// Separate the whole value from the fractional value and store them in two variables. Display the same.

public class prog6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a double number:");
        double n = sc.nextDouble();
        
        
        int  num = (int)n;
        double n1 = n;
        n1-=num;
        n1*=Math.pow(10,6);

       System.out.println("Integerr Part: "+num+"  Decimal Part: "+(int)n1);
        

        sc.close();
    }
}

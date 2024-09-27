package SeqBootCamp.Day3.Kritharth;




import java.util.Scanner;

public class numDisplay {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int rem;
        String sb = "";
        for (int i = 0; i < n; i++) {
            rem = n%10;
            switch (rem) {
                case 1:
                    sb = sb + " one";
                    break;
                case 2 :
                    sb = sb + " two";
                    break;
                case 3 : 
                    sb = sb + " three";
                    break;
                case 4: 
                sb = sb + " four";
                break;
                case 5 : 
                    sb = sb + " five";
                    break;
                case 6 : 
                    sb = sb + " six";
                    break;
                case 7 : 
                    sb = sb + " seven";
                    break;
                case 8 : 
                    sb = sb + " eight";
                    break;
                case 9 : 
                    sb = sb + " nine";
                    break;
            }
        } 
        System.out.println(sb);
        sc.close();       
    }
}


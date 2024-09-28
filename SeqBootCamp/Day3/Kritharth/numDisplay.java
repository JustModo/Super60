package SeqBootCamp.Day3.Kritharth;




import java.util.Scanner;

public class numDisplay {
    
    public static int rev(int n){
        int rem,revnum=0;
        while (n!=0) {
            rem = n%10;
            
            revnum= (revnum*10)+rem;;
            n/=10;
        }
        return revnum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = rev(n);
        String sb = "";
        int rem;
        while(m!=0) {
            rem = m%10;
            switch (rem) {
                case 0:
                    sb = sb + " zero";
                case 1:
                    sb = sb + " one";
                    break;
                case 2 :
                    sb =  sb  + " two";
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
            m/=10;
        }
        System.out.println(sb);
        sc.close();       
    }
}


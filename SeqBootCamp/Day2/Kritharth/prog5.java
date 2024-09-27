public class prog5 {
    public static void main(String[] args) {
        int mul = 0;
        int n = 301;
        int iter = 0;
        while(mul<4){
            if(n%7==0){
                mul+=1;
                if(mul!=3){
                    System.out.println(n);
                }
                n+=60*7;
                iter+=1;
            }
        }
        System.out.println("Iterations:"+iter);

    }
}

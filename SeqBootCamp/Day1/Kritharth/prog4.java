

public class prog4 {
    public static void main(String[] args) {
        int n;
        int count = 0;
        int i = 1;
        int iterations = 0;

        while(count<5) {
            n = i*7;
            if ((n%2==1)&&(n%3==1)&&(n%4==1)&&(n%5==1)&&(n%6==1)) {
                    count++;
                    if(count!=3){
                        System.out.println(n);
                    }
            }
            i++;
            iterations++;
        }
        System.out.println("Iterations:"+iterations);
    }
            
}


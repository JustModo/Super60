import java.util.Scanner;
 

public class Test {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of students:");
        int n = sc.nextInt();
        String name;
        Student s[] = new Student[n];
        Student stud1 = new Student();
        stud1.setM1(14);
        stud1.setM2(15);

        s[0] = stud1;

        Student stud2 = new Student();
        stud2.setM1(17);
        stud2.setM2(15);

        s[1] = stud2;
        // for (int i = 0; i < s.length; i++) {
        //     System.out.println("Enter the name:");
        //     name = sc.nextLine();
        //     s[0].get
        // }
        // System.out.print(Arrays.toString(s));
        System.out.println(s.length);
        for(int i=0; i<s.length; i++){
            System.out.println(s[i].getM1());
        }

        

    }
}


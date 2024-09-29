package SeqBootCamp.Day4.Kritharth;
// 6	23	90	267	638	1311	2418	4115	6582	10023	14666	20763	28590	38447	50658.
//REFER EXCEL SHEET FOR LOGIC


// 6	23	90	267	638	1311	2418	4115	6582
// 	17	67	177	371	673	1107	1697	2467
// 		50	110	194	302	434	590	770
// 			60	84	108	132	156	180
// 				24	24	24	24	24


import java.util.Scanner;






public class pattern7 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int lOne = 6;
        int lTwo = 17;
        int lThree = 50;
        int lFour = 60;
        int lFive = 24;


        for (int i = 0; i< n; i++) {
            System.out.print(lOne+"  ");
            lOne += lTwo;
            lTwo += lThree;
            lThree += lFour;
            lFour += lFive;
        }
    }
}

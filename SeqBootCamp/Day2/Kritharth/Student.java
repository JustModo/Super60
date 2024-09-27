
// Display the 1 st, 2nd average and total. 
//Display whether the student has secured 1 st , 2nd , pass class or has failed. 
//1 st class is for a score of 60 and above, 2 nd class is for a score of 50 and above, 
//while pass class is for a score of 35 and above.
// If the score is less than 35, then the student fails.

public class Student {
    String name;
    int m1, m2, m3;

    

    public int getM1() {
        return m1;
    }

    public int getM2() {
        return m2;
    }

    public int getM3() {
        return m3;
    }

    public String getName() {
        return name;
    }

    public void setM1(int m1) {
        this.m1 = m1;
    }

    public void setM2(int m2) {
        this.m2 = m2;
    }

    public void setM3(int m3) {
        this.m3 = m3;
    }
    public void setName(String name) {
        this.name = name;
    }
    
}


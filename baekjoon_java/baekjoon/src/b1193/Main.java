package b1193;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int i = 1;
        int num = 0;

        int down, upper;
        Scanner sc = new Scanner(System.in);
        int X = sc.nextInt();

        while (true) {
            if (num + i >= X) {
                if (i % 2 == 0) {
                    down = i - (X - num - 1);
                    upper = X - num;
                    break;
                } else {
                    upper = i - (X - num - 1);
                    down = X - num;
                    break;
                }
            } else {
                num += i;
                i++;
            }
        }
        System.out.println(upper+"/"+down);
    }
}

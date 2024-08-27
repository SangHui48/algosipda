package b7113;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        System.out.println(countSquare(n, m));
    }

    static int countSquare(int n, int m) {
        if (m == 0) {
            return 0;
        }

        int answer = n / m;

        return answer + countSquare(m, n % m);
    }
}

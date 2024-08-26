package b5956;

import java.util.Scanner;

public class Main {
    static long total;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextInt();
        long M = sc.nextInt();
        sc.close();
        countCows(N, M, 0);
        System.out.println(total);
    }

    private static void countCows(long n, long m, long i) {
        if (n % 2 == 0 || m % 2 == 0) {
            return;
        }

        total += (int) Math.pow(4, i);
        countCows(n / 2, m / 2, i + 1);

    }

//    private static long countCows(long n, long m) {
//        long ans = 0;
//        long cow = 1;
//        while (n % 2 == 1 && m % 2 == 1) {
//            long midRow = n / 2;
//            long midCol = m / 2;
//
//            ans += cow;
//
//            n = midRow;
//            m = midCol;
//            cow *= 4;
//        }
//
//        return ans;
//
//    }
}

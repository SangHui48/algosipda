//package b17910;
//
//import java.util.Scanner;
//
//public class Main {
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
//        int[] coefficients  = new int[n];
//        for (int i = 0; i < n; i++) {
//            coefficients [i] = sc.nextInt();
//        }
//    }
//
//    static long[] calculateFraction(int[] coefficients, int index) {
//        if (index == coefficients.length - 1) {
//            return new long[]{coefficients[index], 1};
//        }
//
//        long[] next = calculateFraction(coefficients, index + 1);
//
//        long numerator = coefficients[index] * next[0];
//    }
//}
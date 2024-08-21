package b1436;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int num = 666;
        int count = 1;

        while (count != N) {
            num++;
            if (String.valueOf(num).contains("666")) {
                count++;
            }
        }
        System.out.println(num);
//        if (N > 1) {
//            func(N);
//        } else {
//            System.out.println(666);
//        }
//    }
//
//    public static void func(int n) {
//        int count = 1;
//        int prev_digit = 0; // 선수 자릿수
//        int num = 0; // 선수 자릿수를 제외한 나머지가 된 자릿수
//
//        while (true) {
//            if (())
//        }
    }
}

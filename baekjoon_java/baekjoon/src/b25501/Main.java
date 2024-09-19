package b25501;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int result;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            String s = br.readLine();
            result = 0;
            System.out.println(isPalindrome(s) + " " + result);
        }
    }

    static int recursion(String s, int l, int r) {
        result++;
        if (l >= r) {
            return 1;
        } else if (s.charAt(l) != s.charAt(r)) {
            return 0;
        } else {
            return recursion(s, l + 1, r - 1);
        }
    }

    static int isPalindrome(String s) {
        return recursion(s, 0, s.length() - 1);
    }
}
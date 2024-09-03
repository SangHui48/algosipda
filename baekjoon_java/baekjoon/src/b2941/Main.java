package b2941;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String[] arr = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
        Scanner sc = new Scanner(System.in);
        String str = sc.next();

        for (String s : arr) {
            if (str.contains(s)) {
                str = str.replace(s, "@");
            }
        }
        System.out.println(str.length());
    }
}

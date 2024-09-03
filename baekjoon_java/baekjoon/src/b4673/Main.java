package b4673;

public class Main {
    public static void main(String[] args) {
        boolean[] check = new boolean[10001];
        for (int i = 1; i < 10001; i++) {
            int sum = i;
            int num = i;
            while (num != 0) {
                sum += (num % 10);
                num = num / 10;
            }

            if (sum < 10001) {
                check[sum] = true;
            }
        }

        for (int i = 1; i < 10001; i++) {
            if (!check[i]) {
                System.out.println(i);
            }
        }
    }
}

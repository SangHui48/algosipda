package b1018;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        String[] board = new String[N];

        for (int i = 0; i < N; i++) {
            board[i] = br.readLine();
        }
        br.close();

        int result = Integer.MAX_VALUE;

        for (int i = 0; i < N - 7; i++) {
            for (int j = 0; j < M - 7; j++) {
                for (int k = 0; k < 2; k++) {
                    char start = k == 0 ? 'W' : 'B';

                    int count = 0;
                    for (int n = i; n < i + 8; n++) {
                        for (int m = j; m < j + 8; m++) {
                            if (start != board[n].charAt(m)) {
                                count++;
                            }

                            start = start == 'W' ? 'B' : 'W';
                        }
                        start = start == 'W' ? 'B' : 'W';
                    }
                    result = Math.min(result, count);

                    if (result == 0) {
                        System.out.println(0);
                        break;
                    }
                }
            }
        }
        System.out.println(result);
    }
}

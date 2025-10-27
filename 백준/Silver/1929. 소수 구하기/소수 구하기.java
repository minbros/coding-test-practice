import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        StringBuilder sb = new StringBuilder();
        for (int num = m; num <= n; num++) {
            boolean isPrime = true;
            double limit = Math.sqrt(num);
            for (int k = 2; k <= limit; k++) {
                if (num % k == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (num > 1 && isPrime) sb.append(num).append("\n");
        }
        System.out.println(sb);
    }
}
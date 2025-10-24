import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int idx = 1;
        Deque<Integer> stack = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            int k = Integer.parseInt(br.readLine());
            while (k >= idx) {
                stack.push(idx++);
                sb.append("+\n");
            }

            Integer poll = stack.poll();
            if (poll == null || poll < k) {
                System.out.println("NO");
                System.exit(0);
            }
            sb.append("-\n");
        }

        System.out.println(sb);
    }
}
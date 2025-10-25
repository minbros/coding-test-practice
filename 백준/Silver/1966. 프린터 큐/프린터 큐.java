import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            Deque<int[]> docs = new ArrayDeque<>();
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                int p = Integer.parseInt(st.nextToken());
                docs.add(new int[]{p, j});
            }

            int result = 1;
            while (!docs.isEmpty()) {
                int maxP = Integer.MIN_VALUE;
                for (int[] doc : docs) {
                    maxP = Math.max(maxP, doc[0]);
                }

                int[] info = docs.poll();
                int p = info[0];
                int idx = info[1];
                if (p == maxP && idx == m) break;
                if (p == maxP) result++;
                else if (p < maxP) docs.offer(info);
            }
            System.out.println(result);
        }
    }
}
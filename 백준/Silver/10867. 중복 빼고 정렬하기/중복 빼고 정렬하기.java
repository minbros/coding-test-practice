import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] numbers = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(numbers);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (i == 0 || numbers[i - 1] != numbers[i]) {
                sb.append(numbers[i]).append(" ");
            }
        }
        System.out.println(sb);
    }
}
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());

        int[][] coords = new int[n][2];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            coords[i] = new int[]{x, y};
        }

        Arrays.sort(coords, compare());
        for (int[] coord : coords) {
            int x = coord[0];
            int y = coord[1];
            sb.append(x).append(" ").append(y).append("\n");
        }
        System.out.println(sb);
    }

    private static Comparator<int[]> compare() {
        return (a, b) -> {
            if (a[0] == b[0]) {
                return Integer.compare(a[1], b[1]);
            }
            return Integer.compare(a[0], b[0]);
        };
    }
}
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] trees = new int[n + 1];
        for (int i = 1; i < n + 1; i++) {
            trees[i] = Integer.parseInt(br.readLine());
        }

        int distance = trees[2] - trees[1];
        for (int i = 3; i < n + 1; i++) {
            distance = euclidean(trees[i] - trees[i - 1], distance);
        }

        int treeSpacingCount = (trees[n] - trees[1]) / distance - 1;
        System.out.println(treeSpacingCount - (n - 2));
    }

    // GCD(a, b) = GCD(b, r) (a = bq + r, 0 <= r < b)
    // r = 0이 될 때, a와 b의 최대공약수는 b가 됨
    private static int euclidean(int a, int b) {
        int r = a % b;
        if (r == 0) {
            return b;
        }
        return euclidean(b, r);
    }
}
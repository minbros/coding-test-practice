import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        char[][] grid = new char[r][c];
        for (int i = 0; i < r; i++) {
            String row = br.readLine();
            for (int j = 0; j < c; j++) {
                char ch = row.charAt(j);
                grid[i][j] = ch;
            }
        }

        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int h = r - Integer.parseInt(st.nextToken());
            boolean destroyed = throwSpear(grid, h, i);
            List<int[]> cluster = findIsolatedCluster(grid, destroyed);
            fall(grid, cluster);
        }
        for (char[] row : grid) {
            sb.append(row).append("\n");
        }
        System.out.println(sb);
    }

    private static boolean throwSpear(char[][] grid, int h, int i) {
        int dir = (i % 2 == 0) ? 1 : -1;
        int col = grid[0].length;
        int start = (i % 2 == 0) ? 0 : col - 1;
        while (start >= 0 && start < col && grid[h][start] == '.') {
            start += dir;
        }

        if (start >= 0 && start < col) {
            grid[h][start] = '.';
            return true;
        }
        return false;
    }

    private static List<int[]> findIsolatedCluster(char[][] grid, boolean destroyed) {
        if (!destroyed) {
            return List.of();
        }

        int row = grid.length;
        int col = grid[0].length;
        Deque<int[]> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[row][col];
        for (int i = 0; i < col; i++) {
            if (grid[row - 1][i] == 'x') {
                queue.offer(new int[]{row - 1, i});
                visited[row - 1][i] = true;
            }
        }

        int[][] directions = new int[][]{{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
        while (!queue.isEmpty()) {
            int[] mineral = queue.pop();
            int x = mineral[0];
            int y = mineral[1];

            for (int[] dir : directions) {
                int nx = x + dir[0];
                int ny = y + dir[1];
                if (nx >= 0 && nx < row && ny >= 0 && ny < col && grid[nx][ny] == 'x' && !visited[nx][ny]) {
                    queue.offer(new int[]{nx, ny});
                    visited[nx][ny] = true;
                }
            }
        }

        List<int[]> cluster = new ArrayList<>();
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 'x' && !visited[i][j]) {
                    cluster.add(new int[]{i, j});
                }
            }
        }
        return cluster;
    }

    private static void fall(char[][] grid, List<int[]> cluster) {
        if (cluster.isEmpty()) {
            return;
        }

        int[] lowestPos = new int[grid[0].length];
        Arrays.fill(lowestPos, -1);
        for (int[] pos : cluster) {
            lowestPos[pos[1]] = Math.max(lowestPos[pos[1]], pos[0]);
        }

        int count = 0;
        while (true) {
            boolean canFall = true;
            for (int i = 0; i < lowestPos.length; i++) {
                int r = lowestPos[i];
                if (r != -1 && (r + count + 1 >= grid.length || grid[r + count + 1][i] != '.')) {
                    canFall = false;
                    break;
                }
            }

            if (!canFall) {
                break;
            }
            count += 1;
        }

        for (int[] pos : cluster) {
            int x = pos[0];
            int y = pos[1];
            grid[x][y] = '.';
        }

        for (int[] pos : cluster) {
            int x = pos[0];
            int y = pos[1];
            grid[x + count][y] = 'x';
        }
    }
}
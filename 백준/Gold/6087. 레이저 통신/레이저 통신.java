import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int w = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());

        char[][] grid = new char[h][w];
        int[][] c = new int[2][2];
        int k = 0;
        for (int i = 0; i < h; i++) {
            String row = br.readLine();
            for (int j = 0; j < w; j++) {
                char ch = row.charAt(j);
                grid[i][j] = ch;
                if (ch == 'C') {
                    c[k++] = new int[]{i, j};
                }
            }
        }

        int result = find(h, w, c, grid);
        System.out.println(result);
    }

    private static int find(int h, int w, int[][] c, char[][] grid) {
        int[][] directions = new int[][]{{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        boolean[][] visited = new boolean[h][w];

        int[][] costs = new int[h][w];
        for (int i = 0; i < h; i++) {
            Arrays.fill(costs[i], Integer.MAX_VALUE);
        }
        costs[c[0][0]][c[0][1]] = 0;

        Deque<int[]> queue = new ArrayDeque<>();
        for (int i = 0; i < 4; i++) {
            // row 값, col 값, 방향, 거울 개수
            queue.offer(new int[]{c[0][0], c[0][1], i, 0});
        }

        while (!queue.isEmpty()) {
            int[] info = queue.pop();
            int row = info[0];
            int col = info[1];
            int[] dir = directions[info[2]];
            int depth = info[3];

            visited[row][col] = true;
            int nextRow = row + dir[0];
            int nextCol = col + dir[1];
            while (nextRow >= 0 && nextRow < h && nextCol >= 0 && nextCol < w && grid[nextRow][nextCol] != '*') {
                if (!visited[nextRow][nextCol]) {
                    if (grid[nextRow][nextCol] == 'C') {
                        return depth;
                    }
                    queue.offer(new int[]{nextRow, nextCol, rotate(info[2], true), depth + 1});
                    queue.offer(new int[]{nextRow, nextCol, rotate(info[2], false), depth + 1});
                    costs[nextRow][nextCol] = Math.min(costs[nextRow][nextCol], depth);
                    visited[nextRow][nextCol] = true;
                }
                nextRow += dir[0];
                nextCol += dir[1];
            }
        }

        return -1;
    }

    private static int rotate(int direction, boolean isClockwise) {
        return (isClockwise) ? (direction + 1) % 4 : (direction + 3) % 4;
    }
}
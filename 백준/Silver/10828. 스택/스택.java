import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        Deque<Integer> stack = new ArrayDeque<>();
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String command = br.readLine();
            switch (command) {
                case "pop":
                    sb.append((stack.isEmpty()) ? -1 : stack.pop()).append('\n');
                    break;
                case "size":
                    sb.append(stack.size()).append('\n');
                    break;
                case "empty":
                    sb.append((stack.isEmpty()) ? 1 : 0).append('\n');
                    break;
                case "top":
                    sb.append((stack.isEmpty()) ? -1 : stack.peek()).append('\n');
                    break;
                default:
                    int k = Integer.parseInt(command.split(" ")[1]);
                    stack.push(k);
                    break;
            }
        }

        System.out.println(sb);
    }
}
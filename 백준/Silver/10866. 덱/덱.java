import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        Deque<Integer> deque = new ArrayDeque<>();
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            switch (command) {
                case "pop_front":
                    sb.append((deque.isEmpty()) ? -1 : deque.poll()).append('\n');
                    break;
                case "pop_back":
                    sb.append((deque.isEmpty()) ? -1 : deque.pollLast()).append('\n');
                    break;
                case "size":
                    sb.append(deque.size()).append('\n');
                    break;
                case "empty":
                    sb.append((deque.isEmpty()) ? 1 : 0).append('\n');
                    break;
                case "front":
                    sb.append((deque.isEmpty()) ? -1 : deque.peek()).append('\n');
                    break;
                case "back":
                    sb.append((deque.isEmpty()) ? -1 : deque.peekLast()).append('\n');
                    break;
                default:
                    int k = Integer.parseInt(st.nextToken());
                    if (command.equals("push_front")) deque.push(k);
                    else deque.offer(k);
                    break;
            }
        }

        System.out.println(sb);
    }
}
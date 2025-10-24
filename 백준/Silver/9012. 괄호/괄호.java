import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            String result = (isCorrect(br.readLine())) ? "YES" : "NO";
            System.out.println(result);
        }
    }

    private static boolean isCorrect(String input) {
        Deque<Character> stack = new ArrayDeque<>();
        for (int i = 0; i < input.length(); i++) {
            char ch = input.charAt(i);
            if (ch == '(') {
                stack.push('(');
            } else {
                if (stack.poll() == null) {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
}
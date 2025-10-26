import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String result = find("", n);
        System.out.println(result);
    }

    private static String find(String sequences, int n) {
        int length = sequences.length();
        for (int i = 1; i <= length / 2; i++) {
            String subsequence1 = sequences.substring(length - i, length);
            String subsequence2 = sequences.substring(length - 2 * i, length - i);
            if (subsequence1.equals(subsequence2)) {
                return null;
            }
        }

        if (length == n) {
            return sequences;
        }

        String result = find(sequences + "1", n);
        if (result == null) result = find(sequences + "2", n);
        if (result == null) result = find(sequences + "3", n);
        return result;
    }
}
import java.io.*;
import java.util.*;

public class Main {
    private static final int MOD = 1000000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(br.readLine());

        List<Long> fib = new ArrayList<>(List.of(0L, 1L));
        int cycle = 1;
        while (true) {
            long cur = (fib.get(cycle) + fib.get(cycle - 1)) % MOD;
            if (fib.get(cycle) == 0 && cur == 1) {
                break;
            }
            fib.add(cur);
            cycle++;
        }

        System.out.println(fib.get((int) (n % cycle)));
    }
}
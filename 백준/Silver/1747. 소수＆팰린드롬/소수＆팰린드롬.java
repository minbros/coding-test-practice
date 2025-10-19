import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (n == 1) {
            n = 2;
        }

        while (true) {
            boolean isPrime = true;
            int limit = (int) Math.sqrt(n);
            for (int i = 2; i <= limit; i++) {
                if (n % i == 0) {
                    isPrime = false;
                    break;
                }
            }

            if (!isPrime) {
                n++;
                continue;
            }

            String iStr = String.valueOf(n);
            String rStr = new StringBuilder(iStr).reverse().toString();
            if (!iStr.equals(rStr)) {
                n++;
                continue;
            }

            break;
        }

        System.out.println(n);
        sc.close();
    }
}
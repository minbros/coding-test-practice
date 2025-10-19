import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        String line1 = sc.nextLine();

        int m = sc.nextInt();
        sc.nextLine();
        String line2 = sc.nextLine();

        String[] parts = line1.split("\\s");
        Set<Integer> nums = new HashSet<>();
        for (int i = 0; i < n; i++) {
            nums.add(Integer.parseInt(parts[i]));
        }

        parts = line2.split("\\s");
        for (int i = 0; i < m; i++) {
            if (nums.contains(Integer.parseInt(parts[i]))) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }
    }
}
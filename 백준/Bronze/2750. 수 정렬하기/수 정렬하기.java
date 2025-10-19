import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            int k = sc.nextInt();
            nums[i] = k;
        }

        Arrays.sort(nums);
        for (int num : nums) {
            System.out.println(num);
        }
    }
}
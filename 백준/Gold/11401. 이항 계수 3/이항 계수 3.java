import java.io.*;
import java.util.*;

public class Main {
    // 1,000,000,007은 소수 값
    static final int MOD = 1000000007;

    /**
     * 덧셈, 뺄셈, 곱셈은 모듈러 연산과 교환이 가능하지만, 나눗셈은 그렇지 않음
     * 모듈러 연산에서 나눗셈을 계산할 때는 모듈러 역원을 구해서 곱해줘야 함
     * ex) (a + b) mod m = ((a mod m) + (b mod m)) mod m
     * ex) (a / b) mod m = (a * b^(-1)) mod m (b^(-1)은 m에 대한 b의 모듈러 역원)
     * 식에서 b^(-1)은 마치 1/b과 유사하게 적용됨
     **/
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int p = n - k;

        long kFac = factorial(k);
        long pFac = factorial(p);
        long result = factorial(n);

        result = (result * inverse(kFac)) % MOD;
        result = (result * inverse(pFac)) % MOD;
        System.out.println(result);
    }

    static long factorial(int n) {
        long result = 1;
        for (int i = 2; i <= n; i++) {
            result = (result * i) % MOD;
        }
        return result;
    }

    // 페르마의 소정리 n^p mod p = n에서
    // n^(-1) = n^(p - 2) mod p (p는 소수)를 통해 모듈러 역원 계산
    static long inverse(long n) {
        return power(n, MOD - 2);
    }

    // 분할 정복을 통해 거듭제곱 계산
    static long power(long base, int exp) {
        long result = 1;
        base %= MOD;
        while (exp > 0) {
            if (exp % 2 == 1) {
                result = (result * base) % MOD;
            }
            base = (base * base) % MOD;
            exp /= 2;
        }
        return result;
    }
}
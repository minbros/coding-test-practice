import java.io.*;
import java.util.*;

public class Main {
    static class Info {
        String name;
        int age;
        int index;

        public Info(String name, int age, int index) {
            this.name = name;
            this.age = age;
            this.index = index;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        PriorityQueue<Info> priorityQueue = new PriorityQueue<>(compare());
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int age = Integer.parseInt(st.nextToken());
            String name = st.nextToken();
            priorityQueue.offer(new Info(name, age, i));
        }

        StringBuilder sb = new StringBuilder();
        while (!priorityQueue.isEmpty()) {
            Info info = priorityQueue.poll();
            sb.append(info.age).append(" ").append(info.name).append("\n");
        }
        System.out.println(sb);
    }

    private static Comparator<Info> compare() {
        return (a, b) -> {
            if (a.age == b.age) return Integer.compare(a.index, b.index);
            return Integer.compare(a.age, b.age);
        };
    }
}
import java.util.*;

public class Second {
    public static void main(String[] args) {
        int[][] data = {{1, 0, 5},{2, 2, 2},{3, 3, 1},{4, 4, 1},{5, 10, 2}};
        ArrayList<Integer> answer = new ArrayList<>();
        Arrays.sort(data, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if(o1[2]<o2[2]){
                    return -1;
                }
                else{
                    return 1;
                }
            }
        });
        
        int current = 0;
        boolean[] done = new boolean[data.length];
        while (true){
            boolean isEven = false;
            if (answer.size()==data.length){
                break;
            }
            for (int i = 0; i < data.length; i++) {
                if (done[i]) continue; // 처리 되었다면 무시
                if (current==data[i][1]){
                    done[i] = true;
                    answer.add(data[i][0]);
                    current += data[i][2];
                    isEven = true;
                    break;
                }
            }
            if (!isEven){
                for (int i = 0; i < data.length; i++) {
                    if(done[i]) continue;
                    else{
                        done[i] = true;
                        answer.add(data[i][0]);
                        current += data[i][2];
                        break;
                    }
                }
            }
        }
        answer.get()
    }
}

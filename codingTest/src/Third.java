import static java.lang.Math.max;
import static java.lang.Math.min;
public class Third {
    static int[] histogram;
    public static void main(String[] args) {
        int[] histogram = {2,2,2,3};
        System.out.println(histogram.length);
    }

    public static int div(int left, int right) {
        if (left == right) {
            return histogram[left];
        }
        int mid = (right + left) / 2;
        int result = max(div(left, mid), div(mid + 1, right));

        int h = mid + 1;
        int l = mid;
        int minH = min(histogram[l], histogram[h]);
        result = max(result, minH * 2);
        while (l > left || h < right) {
            if (h < right && (l == left || histogram[l - 1] < histogram[h + 1])) {
                h++;
                minH = min(minH, histogram[h]);
            } else {
                l--;
                minH = min(minH, histogram[l]);
            }
            result = max(result, minH * (h - l + 1));
        }
        return result;
    }
}

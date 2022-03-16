import java.util.Scanner;

public class First {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int number = n;
        int sum = 0;
        loop : while(true)
        {
            int mok = number / n;
            int nmg = number % n;
            if(mok >= n) {
                break loop;
            } //몫과 n의 값이 같아지면 더이상 //몫과 나머지가 같은 수는 없다. if(mok == nmg) { sum += number; } number++; } System.out.println(sum);
            if(mok == nmg) {
                sum += number;
            } number++;
        }
        System.out.println(sum);

    }
}

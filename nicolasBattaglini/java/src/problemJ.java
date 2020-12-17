import java.util.Arrays;
import java.util.Scanner;

public class problemJ {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.nextLine());
        String a = scanner.nextLine();
        String b = scanner.nextLine();

        Scanner scanA = new Scanner(a);
        scanA.useDelimiter(" ");
        int[] atab = new int[n];
        for (int i = 0; i < n; i++) {
            atab[i] = Integer.parseInt(scanA.next());
        }
        Scanner scanB = new Scanner(b);
        scanB.useDelimiter(" ");
        int[] btab = new int[n];
        for (int i = 0; i < n; i++) {
            btab[i] = Integer.parseInt(scanB.next());
        }

        int[] res = new int[3];

        for (int i = 0; i < atab.length; i++) {
            for (int j = 0; j < btab.length; j++) {
                res[(i+j+2)%3] += atab[i] * btab[j];
            }
        }

        System.out.print(res[0] + " " + res[1] + " " + res[2]);

    }

}

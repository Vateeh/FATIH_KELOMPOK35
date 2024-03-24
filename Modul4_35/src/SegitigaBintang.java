import java.util.Scanner;
public class SegitigaBintang {

    public static void cetakSegitiga(int tinggi) {
        for (int i = 0; i < tinggi - 1; i++) {

            for (int j = 0; j < tinggi - i - 1; j++) {
                System.out.print(" ");
            }

            System.out.print("*");

            if (i > 0) {
                for (int k = 0; k < 2 * i - 1; k++) {
                    System.out.print(" ");
                }

                System.out.print("*");
            }

            System.out.println();
        }

        for (int i = 0; i < tinggi * 2 - 1; i++) {
            if (i % 2 == 0) {
                System.out.print("*");
            } else {
                System.out.print(" ");
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Masukkan tinggi segitiga: ");
        int tinggi = scanner.nextInt();
        cetakSegitiga(tinggi);
        scanner.close();
    }
}

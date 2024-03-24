import java.util.Scanner;

public class Persegi {

    public static double hitungLuasPersegi(double sisi) {
        return sisi * sisi;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Masukkan panjang sisi persegi: ");
        double sisi = input.nextDouble();

        double luas = hitungLuasPersegi(sisi);
        System.out.println("Luas persegi: " + luas);

        input.close();
    }
}

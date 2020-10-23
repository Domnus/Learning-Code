import java.util.Scanner;

public class Exercício04 {
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		
		System.out.print("Dias: ");
		int dias = scan.nextInt();

		System.out.print("Horas: ");
		int horas = scan.nextInt();

		System.out.print("Minutos: ");
		int minutos = scan.nextInt();
		
		System.out.print("Segundos: ");
		int segundos = scan.nextInt();

		int total = (dias*24*60*60) + (horas*60*60) + (minutos*60) + segundos;

		System.out.println("Total de segundos: " + total);

		scan.close();

	}
}

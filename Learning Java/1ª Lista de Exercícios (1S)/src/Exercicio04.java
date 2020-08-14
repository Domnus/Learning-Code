import java.util.Scanner;

public class Exercicio04 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
		System.out.println("Dias:");
		int dias = scan.nextInt();
		
		System.out.println("Horas:");
		int horas = scan.nextInt();
		
		System.out.println("Minutos:");
		int minutos = scan.nextInt();
		
		System.out.println("Segundos:");
		int segundos = scan.nextInt();
		
		int total = segundos + (minutos * 60) + (horas * 3600) + (dias * 24 * 3600);
		
		System.out.println("Total de segundos: " + total);
	}

}

import java.util.Scanner;

public class Exercicio03S1 {
	
	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		System.out.println("Digite um número em metros:");
		float metro = scan.nextFloat();
		
		float mil = metro * 100;
		
		System.out.println(metro + " metro(s) em milímetros é igual a " + mil + " milímetro(s).");
		
		scan.close();
	}

}

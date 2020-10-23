import java.util.Scanner;

public class Exercício02{
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);

		System.out.print("Digite o primeiro número: ");
		int n1 = scan.nextInt();
	
		System.out.print("Digite o segundo número: ");
		int n2 = scan.nextInt();

		System.out.print("Digite o terceiro número: ");
		int n3 = scan.nextInt();

		float m = (n1 + n2 + n3) / 3;

		System.out.println("A média entre os números é igual a " + m);

		scan.close();
	}
}

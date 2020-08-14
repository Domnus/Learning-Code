import java.util.Scanner;

public class Exercicio01 {

	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		final Scanner scan = new Scanner(System.in);

		System.out.println("Digite um número:");
		final int n1 = scan.nextInt();

		System.out.println("Digite outro número:");
		final int n2 = scan.nextInt();

		final int n3 = n1 + n2;
		
		System.out.println("A soma entre " + n1 + " e " + n2 + " é igual a " + n3);

	}

}

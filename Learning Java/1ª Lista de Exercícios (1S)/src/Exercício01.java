import java.util.Scanner;

public class Exercício01 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
		System.out.println("Digite um número:");
		int n1 = scan.nextInt();
		
		System.out.println("Digite outro número:");
		int n2 = scan.nextInt();
		
		int n3 = n1 + n2;
		
		System.out.println("A soma entre " + n1 + " e " + n2 + " é igual a " + n3);

	}

}

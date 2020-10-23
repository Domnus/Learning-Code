import java.util.Scanner;

public class Exercício01 {
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);

		System.out.println("Digite o primeiro número: ");
		int n1 = scan.nextInt();
		
		System.out.println("Digite o segundo número: ");
		int n2 = scan.nextInt();
		
		int r = n1 + n2;
		
		System.out.println("A soma dos 2 números é igual a " + r);		

		scan.close();
	}
}

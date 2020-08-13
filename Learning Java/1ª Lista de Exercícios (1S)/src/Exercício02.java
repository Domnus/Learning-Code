import java.util.Scanner;

public class Exercício02 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
		System.out.println("Digite um número:");
		float n1 = scan.nextFloat();
		
		System.out.println("Digite outro número:");
		float n2 = scan.nextFloat();
		
		System.out.println("Digite outro número:");
		float n3 = scan.nextFloat();
		
		float n4 = (n1 + n2 + n3) / 3;
		
		System.out.println("A média é igual a " + n3);
	}

}

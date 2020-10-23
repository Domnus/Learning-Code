import java.util.Scanner;

public class Exercício03{
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);

		System.out.println("Digite um valor em metros: ");
		int metros = scan.nextInt();

		int milimetros = metros * 100;

		System.out.println(metros + " metro em milimetros é igual a " + milimetros);

		scan.close();
	}
}

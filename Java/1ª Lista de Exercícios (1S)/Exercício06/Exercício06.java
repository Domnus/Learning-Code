import java.util.Scanner;

public class Exercício06{
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		
		System.out.print("Salário: ");
		float salario = scan.nextFloat();

		System.out.print("Reajuste: ");
		float reajuste = scan.nextFloat();

		float novo_Salario = salario + (salario * reajuste);

		System.out.println("Seu novo salário é igual a R$" + novo_Salario);

		scan.close();
		
	}
}

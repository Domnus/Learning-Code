import java.util.Scanner;

public class Exercício06 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
		System.out.print("Salário: R$");
		float salario = scan.nextFloat();
		
		System.out.print("Reajuste: ");
		float reajuste = scan.nextFloat();
		
		float novoSalario = salario + (salario * (reajuste / 100));
		
		System.out.print("O novo salário será R$" + novoSalario);
	}

}

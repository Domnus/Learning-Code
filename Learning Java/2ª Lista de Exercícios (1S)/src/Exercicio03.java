import java.util.Scanner;

public class Exercicio03 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
		System.out.println("1 - Área de um retângulo \n2 - Área de um triângulo");
		int op = scan.nextInt();
		
		System.out.print("Valor da base: ");
		float base = scan.nextFloat();
		
		System.out.print("Valor da altura: ");
		float altura = scan.nextFloat();
				
		if (op == 1)
		{
			float area = base * altura;
			System.out.println("A área do retângulo é " + area);
		}
		else if (op == 2)
		{
			float area = (base * altura) / 2;
			System.out.println("A área do triângulo é " + area);
		}
		else
		{
			System.out.println("Valor inválido.");
		}

		scan.close();
	}

}

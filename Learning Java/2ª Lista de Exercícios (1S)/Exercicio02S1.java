import java.util.Scanner;

public class Exercicio02S1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
		System.out.print("Digite o número da placa [XXXX]: ");
		int numPlaca = scan.nextInt();
		
		if (numPlaca > 9999 || numPlaca < 1000)
		{
			System.out.print("O número deve ter 4 algarismos!");
		}
		else
		{
		    int fimPlaca = ((numPlaca % 1000) % 100) % 10;
		    
		    if (fimPlaca == 1 || fimPlaca == 2)
		    {
		    	System.out.println("Dia do Rodízio: Segunda-Feira");
		    }
		    if (fimPlaca == 3 || fimPlaca == 4)
		    {
		    	System.out.println("Dia do Rodízio: Terça-Feira");
		    }
		    if (fimPlaca == 5 || fimPlaca == 6)
		    {
		    	System.out.println("Dia do Rodízio: Quarta-Feira");
		    }
		    if (fimPlaca == 7 || fimPlaca == 8)
		    {
		    	System.out.println("Dia do Rodízio: Quinta-Feira");
		    }
		    if (fimPlaca == 9 || fimPlaca == 0)
		    {
		    	System.out.println("Dia do Rodízio: Sexta-Feira");
		    }
		}

		scan.close();
	}

}

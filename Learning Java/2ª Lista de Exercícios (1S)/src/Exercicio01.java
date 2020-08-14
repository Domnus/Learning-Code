import java.util.Scanner;

public class Exercicio01 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
		System.out.print("Informe um número: ");
		int num = scan.nextInt();
		
		if (num > 1000 || num < 100)
		{
			System.out.println("O número deve contem 3 algarismos!");
		}
		else
		{
			int u = num / 100;
		    int d = (num / 10) % 10;
		    int c = num % 10;
		    
		    if (u < d && d < c)
		    {
		    	System.out.println("O número é ascendente.");
		    }
		    else
		    {
		    	System.out.println("O número não é ascendente.");
		    }
		}
	}

}

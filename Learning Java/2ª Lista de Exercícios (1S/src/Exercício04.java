import java.util.Scanner;

public class Exercício04 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
		System.out.print("Lado 1: ");
		float l1 = scan.nextFloat();
		
		System.out.print("Lado 2: ");
		float l2 = scan.nextFloat();
		
		System.out.print("Lado 3: ");
		float l3 = scan.nextFloat();
		
		if ((l1 +l2) < l3 || (l1 + l3) < l2 || (l2 + l3) < l1)
		{
			System.out.println("Não é um triângulo\n");
	    }
	    else if (l1==l2 && l2==l3)
	    {
	    	System.out.println("É um triângulo equilátero.\n");
	    }
	    else if (l1==l2 || l1==l3 || l2==l3)
	    {
	    	System.out.println("É um triângulo isósceles.\n");
	    }
	    else
	    {
	        System.out.println("É um triângulo escaleno.\n");
	    }
	}

}

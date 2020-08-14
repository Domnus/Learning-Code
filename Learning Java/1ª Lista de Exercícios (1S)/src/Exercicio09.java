import java.util.Scanner;

public class Exercicio09 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
		System.out.print("ºF:");
		float F = scan.nextFloat();
		
		float C = ((F - 32F) / 9F) * 5F;
		
		System.out.print("ºC: " + C);
	}

}

import java.util.Scanner;

public class Exercicio05S1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
		System.out.print("A: ");
		String A = scan.next();

		System.out.print("B: ");
		String B = scan.next();
		
		String X = A;
			   A = B;
			   B = X;
			   
		System.out.println("A: " + A + "\nB: " + B);
		
		scan.close();
	}

}

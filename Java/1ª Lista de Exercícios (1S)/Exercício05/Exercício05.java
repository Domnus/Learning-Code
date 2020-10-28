import java.util.Scanner;

public class Exercício05{
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		
		System.out.print("A: ");
		int A = scan.nextInt();
		
		System.out.print("B: ");
		int B = scan.nextInt();
		
		int X = A;
		A = B;
		B = X;

		System.out.println("A: " + A);
		System.out.println("B: " + B);
		
		scan.close();
	}
}

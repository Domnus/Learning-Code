import java.util.Scanner;

public class Exercicio08S1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
		System.out.print("Km percorridos: ");
		float kmPercorridos = scan.nextFloat();
		
		System.out.print("Dias alugado: ");
		float diasAlugado = scan.nextFloat();
		
		float aPagar = (kmPercorridos * 0.15F) + (diasAlugado * 60F);
		
		System.out.print("Total a pagar: R$" + aPagar);

		scan.close();
	}

}

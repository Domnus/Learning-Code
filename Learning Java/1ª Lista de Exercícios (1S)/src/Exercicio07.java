import java.util.Scanner;

public class Exercicio07 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
		System.out.print("Preço do combustível: R$");
		float precoCombustivel = scan.nextFloat();
		
		System.out.print("Desempenho do Veículo [Km/L]: ");
		float desempenhoVeiculo = scan.nextFloat();
		
		System.out.print("Distância entre as cidades [Km]: ");
		float distanciaCidades = scan.nextFloat();
		
		float litros = desempenhoVeiculo * distanciaCidades;
		float dinheiroGasto = litros * precoCombustivel;
		
		System.out.print("Você gastará " + litros + " litros e R$" + dinheiroGasto + " para fazer a viagem");

		scan.close();
	}

}

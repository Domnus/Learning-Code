/*
Desenvolva um programa que leia através do teclado uma frase e exiba-a de forma invertida (troque
a posição de suas letras - primeira passa ser a última).
 */

import java.util.Scanner;

public class ex09 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String frase, fraseInv;

        System.out.print("Digite uma frase: ");
        frase = scan.nextLine();

        fraseInv = new StringBuffer(frase).reverse().toString();

        System.out.println("Frase invertida: " + fraseInv);

    }
}

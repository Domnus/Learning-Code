/* Desenvolva um programa que conte quantas vogais fazem parte da frase “Bacharelado em Ciência
da Computação” e exiba este valor.
 */

import java.lang.*;

public class ex07 {
    public static void main(String[] args ) {
        String frase = "Bacharelado em Ciência da Computação";

        int cont = frase.replaceAll("[\\saãeêiou]", "").length();

        System.out.println(cont);
    }
}

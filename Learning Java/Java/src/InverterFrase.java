import java.util.*;

public class InverterFrase
{
  public static void main(String[] args)
  {
    String frase, esarf = "";
    Scanner scan = new Scanner(System.in);

    System.out.println("Digite uma frase: ");
    frase = scan.nextLine();

    int lenght = frase.length();

    for (int i = lenght - 1; i >= 0; i--)
    {
      esarf = esarf + frase.charAt(i);
    }

    String output = esarf.substring(0, 1).toUpperCase() + esarf.substring(1);
    System.out.println("Frase invertida: " + output);

    scan.close();
  }
  
}

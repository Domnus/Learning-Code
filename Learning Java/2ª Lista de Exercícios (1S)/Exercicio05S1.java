import java.util.Scanner;

public class Exercicio05S1 {
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);

        System.out.print("Ângulo 1: ");
        float ang1 = scan.nextFloat();

        System.out.print("Ângulo 2: ");
        float ang2 = scan.nextFloat();

        System.out.print("Ângulo 3: ");
        float ang3 = scan.nextFloat();
        
        if (ang1 + ang2 + ang3 != 180){
            System.out.println("Não é um triângulo!\n");
        }
        else if (ang1 > 90 && ang2 > 90 && ang3 > 90){
            System.out.println("Acutângulo\n");
        }
        else if (ang1 == 90 || ang2 == 90 || ang3 == 90){
            System.out.println("Triângulo Retângulo");
        }
        else if (ang1 > 90 || ang2 > 90 || ang3 > 90){
            System.out.println("Obtusângulo");
        }

        scan.close();
    }
    
}
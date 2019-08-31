import java.math.BigDecimal;
import java.util.Scanner;


public class Find_PI_to_the_Nth_Digit{

    public static void main(String []args){
        
        BigDecimal numerator = new BigDecimal(22.0);
        BigDecimal denominator = new BigDecimal(7.0);
        
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter the number of deciaml places to display : ");
        
        int i = sc.nextInt();
        
        System.out.println(numerator.divide(denominator, i , BigDecimal.ROUND_UP));

    }
}
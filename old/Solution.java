import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
	
    public static void main(String[] args) {
        int i = 4;
        double d = 4.0;
        String s = "HackerRank ";
		System.out.println(s);
        Scanner scan = new Scanner(System.in);
        int j = scan.nextInt();
        double f = scan.nextFloat();
        String y = scan.nextLine();
    
        /* Declare second integer, double, and String variables. */

        /* Read and save an integer, double, and String to your variables.*/
        // Note: If you have trouble reading the entire String, please go back and review the Tutorial closely.
        
        /* Print the sum of both integer variables on a new line. */
        int sum = i+ j;
        System.out.println(sum);    
        /* Print the sum of the double variables on a new line. */
        double z = d + f ;
        System.out.println(z);
        /* Concatenate and print the String variables on a new line; 
        	the 's' variable above should be printed first. */
        // String l = s.concat(y);
        // System.out.println(s +""+ y);
        scan.close();
    }
}
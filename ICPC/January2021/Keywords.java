import java.util.Scanner;
import java.util.*;
public class Keywords {
    public static void main(String[] args) {
       TreeSet<String> uniqueKeyWords = new TreeSet<String>();
       Scanner myObj = new Scanner(System.in);
       Integer numInputs = myObj.nextInt();
       myObj.nextLine(); // this line is crucial in order to make sure it skips reading an empty line
       for (int i = 0; i < numInputs; i++){
           String keyWordInput = myObj.nextLine();
           String str = keyWordInput.toLowerCase();
           String str2 = str.replace('-', ' ');
           uniqueKeyWords.add(str2);
        //    System.out.println("New String:" + str2);
       }
      System.out.println(uniqueKeyWords.size()); 
    }
}
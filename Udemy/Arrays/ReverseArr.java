
public class ReverseArr {
    public static void main(String[] args){
    char[] inputArr = {'c','o','m','p','u','t','e','r','-','s','c','i','e','n','c','e'};
    int len = inputArr.length;
    int pivot = (len/2);
    for(int i = 0; i <pivot; i++){
      char tempL = inputArr[(len)-i-1];
      char tempU = inputArr[i];

        inputArr[i] = tempL;
        inputArr[(len)-1-i] = tempU;
 }
   System.out.println(inputArr);
    }
}
import java.util.Arrays;

public class ArrayRev {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

//		int num[] = new  int[5];
//		num[0] =10; 
		
		int[] num = {10,55,67,89,2};
		//if you dont set a value the default is 0
		for (int i = 0; i<num.length; i++) {
			System.out.println(num[i]);
		}
		// sorting the array
		Arrays.sort(num);
		System.out.println("Elements post sorting");
		for (int i = 0; i<num.length; i++) {
			System.out.println(num[i]);
		}
	}

}

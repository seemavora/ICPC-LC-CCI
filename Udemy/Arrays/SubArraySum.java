
public class SubArraySum {
//	Write a program to find continuous sub-array whose sume is equal to a given number. 
//	Lets suppose the sum is equal to 50 and the input int array is
//	int[] num = {5,15,,25,10,50,12,20,30}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [] indexHolder = new int[2];
		int[] num = {5,15,20,10,2,12,25,30};
		int sum = 15;
		indexHolder = findArrLocation(num, 50);
		int ubound = indexHolder[0];
		int lbound = indexHolder[1];
//		System.out.println("ubound" +ubound +"   lbound" +lbound);
		for(int k = ubound; k<=lbound; k++) {
			System.out.println(num[k]);
		}
//		System.out.println("hi");
	}
	
	public static int[] findArrLocation(int[]arr, int sum) {
		int lengthArr = arr.length;
		int [] index = new int[2];
		for (int i = 0; i<lengthArr; i++) {
			int k = i;
			int tempSum =0;
//			System.out.println("sum " +sum);
			while(k <lengthArr) {			
				tempSum = tempSum + arr[k];
				if(tempSum > sum) {
					k = lengthArr;
//					System.out.println("Greater sum " +tempSum);
				}else if (tempSum == sum) {
					index[0] = i;
					index[1] = k;
//					System.out.println("Equal sum " +tempSum);
					k = lengthArr;
				}else {
					k++;
//					System.out.println("Other sum " +tempSum);
				}
			}
		}
		return index;
	}

}

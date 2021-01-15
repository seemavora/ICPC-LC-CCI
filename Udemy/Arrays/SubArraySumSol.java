
public class SubArraySumSol {
//	Write a program to find continuous sub-array whose sume is equal to a given number. 
//	Lets suppose the sum is equal to 50 and the input int array is
//	int[] num = {5,15,,25,10,50,12,20,30}

	public static void main(String[] args) {

		int[] inputArray = { 5, 15, 25, 10, 50, 12, 20, 30 };
		int len = inputArray.length;
		int givenSum = 50;

		/*
		 * Approach 1: Brute Force FInd subarrays, and check sum, time complexity =
		 * O(n^2)
		 */

		for(int i = 0; i <len; i++) {
			int subArraySum = inputArray[i];
			if(subArraySum == givenSum) {
				System.out.println("Single element SubArray with sum equal to " +givenSum+"  : (" +i+"," +i+")");
			}
			for(int j = i+1; j<len; j++) {
				subArraySum += inputArray[j];
				if(subArraySum == givenSum) {
					System.out.println("SubArray with sum equal to " +givenSum+"  : (" +i+"," +j+")");
				}
			}
		}
		
		/*
		 * Approach 2: Efficient 
		 * Complexity = o(n)
		 */
		
		System.out.println("Better Approach");
		int prefixSum = inputArray[0];
		int startIndex = 0;

		for (int i = 0; i < len; i ++){
			if(prefixSum == givenSum || inputArray[i] == givenSum){
				System.out.println("Single element SubArray with sum equal to " +givenSum+"  : (" +i+"," +i+")");
			}
			prefixSum += inputArray[i];
			while(prefixSum > givenSum && startIndex <i-1){
				prefixSum = prefixSum -inputArray[startIndex];
				startIndex++;
			}

			if(prefixSum == givenSum){
				System.out.println("SubArray with sum equal to " +givenSum+"  : (" +startIndex+"," +i+")");
			}
		}
	}
}

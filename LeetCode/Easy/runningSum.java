package LeetCode.Easy;

public class runningSum {
  static int[] nums = { 1, 2, 3, 4, 5, 6 };

  public static int[] calcArr(int[] x) {
    int[] sumArr = new int[nums.length];
    for (int i = 0; i < x.length; i++) {
      if (i == 0) {
        sumArr[i] = nums[i];
      } else {
        sumArr[i] = nums[i] + sumArr[i - 1];
      }
    }
    return sumArr;
  }

  public static void main(String args[]) {
    int[] resultArr = new int[nums.length];
    resultArr = calcArr(nums);
    for (int i = 0; i < resultArr.length; i++) {
      System.out.println(resultArr[i]);
    }
  }
}

class TwoSum {
  public int[] twoSum(int[] nums, int target) {
    int arr[];
    arr = new int[2];
    int len = nums.length;
    int counter =1;
    for(int i = 0; i <len; i++){
    counter = i+1;
      while (counter != (len)){
        int sum = nums[i] + nums[counter];
        if (sum == target){
          arr[0] = i;
          arr[1]=counter;
        }
        counter++;
        sum = 0;
      }
    }

    return arr;
  }
}
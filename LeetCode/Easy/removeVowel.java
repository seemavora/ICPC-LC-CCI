package LeetCode.Easy;

public class removeVowel {
  public static String removeVowels(String s) {

    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < s.length(); i++) {
      if (s.charAt(i) != 'a' & s.charAt(i) != 'e' & s.charAt(i) != 'i' & s.charAt(i) != 'o' & s.charAt(i) != 'u') {
        sb.append(s.charAt(i));
      }
    }
    String noVowel = sb.toString();
    return noVowel;
  }

  public static void main(String args[]) {
    String trial = "hi my name is seema and i love having fun";
    String result = removeVowels(trial);
    System.out.println(result);
  }

}

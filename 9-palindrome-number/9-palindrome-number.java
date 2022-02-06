class Solution {
    public boolean isPalindrome(int x) {

        String str = String.valueOf(x);
        
        StringBuilder sb = new StringBuilder();

        for (int i = str.length()-1; i >= 0; i--) {
            sb.append(str.charAt(i));
        }

        String palindrome = sb.toString();
        return str.equals(palindrome);

    }
}
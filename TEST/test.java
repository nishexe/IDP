public class test{
    public static void main(String args[]){
        String str = "ooloo";
        int firstIdx = 0;
        int lastIdx = str.length() - 1;
        while(firstIdx < lastIdx){
            if(str.charAt(firstIdx) == str.charAt(lastIdx)){
                firstIdx += 1;
                lastIdx -= 1;
            }else{
                System.out.println("FALSE");
                System.exit(0);
            }
        }
        System.out.println("TRUE");
    }
}
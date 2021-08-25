package test;
public class person {
    public static void main(final String[] args) throws Exception {
        System.out.println(isPalindrome("Mom"));
    }

    public static void main(){
        System.out.println("Main method of person class");
        //test comment 
    }
    public static void testMethod(String string){
        System.out.println(string);
    }

    static boolean isPalindrome(String p)
    {
        System.out.println(new StringBuilder(p).reverse());
        return p.equals(new StringBuilder(p).reverse().toString());
        
    }
    
}
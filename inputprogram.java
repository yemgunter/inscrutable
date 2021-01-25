import java.util.Scanner; // Import the Scanner class

class inputprogram {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in); // Create a Scanner object

    System.out.print("Enter your first name : ");
    String firstname = input.next(); // Read user input

    System.out.print("Enter your last name : "); // Read user input
    String lastname = input.next();

    System.out.println("Your Full Name is " + firstname + " " + lastname); // Output user input
  }
}

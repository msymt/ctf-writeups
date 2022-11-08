import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Scanner;

public class soda {
  static final int NUM_DRINKS = 12;
  
  static boolean bystanders = true;
  
  static float wallet = 5.0F;
  
  public static void main(String[] paramArrayOfString) {
    VendingMachine vendingMachine = new VendingMachine();
    Scanner scanner = new Scanner(System.in);
    System.out.println("\nThe prophecy states that worthy customers receive flags in their cans...");
    while (true) {
      System.out.println("\n" + vendingMachine);
      System.out.println(String.format("I have $%.02f in my wallet", new Object[] { Float.valueOf(wallet) }));
      System.out.print("command> ");
      try {
        String str = scanner.nextLine();
        if (str.isEmpty())
          break; 
        String[] arrayOfString = str.split(" ");
        processCommand(vendingMachine, arrayOfString);
      } catch (Exception exception) {
        break;
      } 
    } 
    System.out.println();
    scanner.close();
  }
  
  private static void processCommand(VendingMachine paramVendingMachine, String[] paramArrayOfString) {
    if (paramArrayOfString[0].equalsIgnoreCase("help")) {
      System.out.println(">> You're telling me you don't know how to use a vending machine?");
      return;
    } 
    if (paramArrayOfString[0].equalsIgnoreCase("purchase")) {
      if (paramArrayOfString.length > 1)
        try {
          int i = Integer.parseInt(paramArrayOfString[1]);
          if (i < 1 || i > 12)
            throw new RuntimeException(); 
          paramVendingMachine.buy(i - 1);
          return;
        } catch (Exception exception) {
          System.out.println(">> That's not a real choice");
          return;
        }  
      System.out.println(">> Purchase what?");
      return;
    } 
    if (paramArrayOfString[0].equalsIgnoreCase("reach")) {
      if (bystanders) {
        System.out.println(">> I can't do that with people around!\n>> They'll think I'm stealing!");
        return;
      } 
      int i = paramVendingMachine.reach();
      paramVendingMachine.dropped += i;
      if (i > 0) {
        System.out.println(">> Ok, here goes... gonna reach through the door and try to knock it down...");
        pause(3);
        System.out.println(">> !!! I heard something fall!");
      } else {
        System.out.println(">> There's nothing to reach for");
      } 
      return;
    } 
    if (paramArrayOfString[0].equalsIgnoreCase("wait")) {
      int i = 0;
      try {
        i = Integer.parseInt(paramArrayOfString[1]);
      } catch (Exception exception) {
        System.out.println(">> Not sure what you mean");
        return;
      } 
      pause(i);
      if (i >= 10) {
        bystanders = false;
        System.out.println(">> ...Looks like nobody's around...");
      } else {
        bystanders = true;
        System.out.println(">> People are walking down the street.");
      } 
      return;
    } 
    if (paramArrayOfString[0].equalsIgnoreCase("tap")) {
      System.out.println(">> Tapping the glass is harmless, right?");
      pause(1);
      paramVendingMachine.tap();
      System.out.println(">> Not sure if that helped at all...");
      return;
    } 
    if (paramArrayOfString[0].equalsIgnoreCase("grab")) {
      if (paramVendingMachine.dropped > 0) {
        System.out.println(">> Alright!! Let's see what I got!");
        paramVendingMachine.retrieve();
      } else {
        System.out.println(">> There's nothing to grab...");
      } 
      return;
    } 
    System.out.println(">> Not sure what you mean");
  }
  
  private static void printFlag() {
    try {
      BufferedReader bufferedReader = new BufferedReader(new FileReader("flag.txt"));
      System.out.println(">> WOAH!! There's a flag in here!!");
      String str;
      while ((str = bufferedReader.readLine()) != null)
        System.out.println(str); 
    } catch (Exception exception) {
      System.out.println(">> You find a piece of paper in the can! It reads:");
      System.out.println("\n\t\"You are not worthy\"\n");
    } 
  }
  
  private static void pause(int paramInt) {
    try {
      for (byte b = 0; b < paramInt; b++) {
        System.out.print(". ");
        Thread.sleep(1000L);
      } 
    } catch (Exception exception) {}
    System.out.println();
  }
  
  static class VendingMachine {
    soda.Drink[] drinks = new soda.Drink[12];
    
    public int dropped = 0;
    
    public VendingMachine() {
      for (byte b = 0; b < 12; b++)
        this.drinks[b] = new soda.Drink(); 
    }
    
    public boolean hasDroppedDrinks() {
      for (byte b = 0; b < 12; b++) {
        if ((this.drinks[b]).status == soda.Drink.DrinkStatus.DROPPED)
          return true; 
      } 
      return false;
    }
    
    public void buy(int param1Int) {
      if ((this.drinks[param1Int]).status != soda.Drink.DrinkStatus.READY) {
        System.out.println(">> [OUT OF STOCK]");
        return;
      } 
      if (soda.wallet > (this.drinks[param1Int]).cost) {
        System.out.println(">> [VENDING]");
        soda.pause(5);
        System.out.println(">> ...Wait... IT'S STUCK?? NOOOOOO");
        (this.drinks[param1Int]).status = soda.Drink.DrinkStatus.STUCK;
        soda.wallet -= (this.drinks[param1Int]).cost;
        return;
      } 
      System.out.println(">> I don't have enough money :(");
    }
    
    public void tap() {
      for (byte b = 0; b < 12; b++) {
        if ((this.drinks[b]).status == soda.Drink.DrinkStatus.STUCK && (this.drinks[b]).stuck > 0)
          (this.drinks[b]).stuck--; 
      } 
    }
    
    public int reach() {
      byte b1 = 0;
      for (byte b2 = 0; b2 < 12; b2++) {
        if ((this.drinks[b2]).status == soda.Drink.DrinkStatus.STUCK && (this.drinks[b2]).stuck == 0) {
          (this.drinks[b2]).status = soda.Drink.DrinkStatus.DROPPED;
          b1++;
        } 
      } 
      return b1;
    }
    
    public void retrieve() {
      byte b = -1;
      float f = -1.0F;
      for (byte b1 = 0; b1 < 12; b1++) {
        if ((this.drinks[b1]).status != soda.Drink.DrinkStatus.EMPTY && 
          (this.drinks[b1]).cost > f) {
          b = b1;
          f = (this.drinks[b1]).cost;
        } 
      }
      System.out.println(b);
      if ((this.drinks[b]).status == soda.Drink.DrinkStatus.DROPPED) {
        soda.printFlag();
      } else {
        System.out.println(">> No flags in here... was the prophecy a lie...?");
      } 
    }
    
    public String toString() {
      String str = "-------".repeat(6) + "-\n";
      byte b;
      for (b = 0; b < 6; b++) {
        for (byte b1 = 0; b1 < 6; b1++)
          str = str + str; 
        str = str + "|\n";
      } 
      str = str + str + "-\n";
      for (b = 0; b < 6; b++) {
        for (byte b1 = 6; b1 < 12; b1++)
          str = str + str; 
        str = str + "|\n";
      } 
      str = str + str + "-\n";
      return str;
    }
  }
  
  static class Drink {
    float cost = (float)(Math.random() * 6.0D);
    
    DrinkStatus status = (Math.random() > 0.75D) ? DrinkStatus.EMPTY : DrinkStatus.READY;
    
    int stuck = 3;
    
    public String getCostLabel() {
      return String.format("%1.02f", new Object[] { Float.valueOf(this.cost) });
    }
    
    public String[] asText(int param1Int) {
      String[] arrayOfString = { "| " + param1Int + ((param1Int < 10) ? "    " : "   "), "|      ", "|      ", "|      ", "|      ", "| " + getCostLabel() + " " };
      if (this.status != DrinkStatus.EMPTY && this.status != DrinkStatus.DROPPED)
        return new String[] { "| " + param1Int + (
            
            (param1Int < 10) ? "    " : "   "), "|  __  ", 
            
            (this.status == DrinkStatus.STUCK) ? "| |**| " : "| |  | ", "| |__| ", "|      ", "| " + 
            
            getCostLabel() + " " }; 
      return arrayOfString;
    }
    
    enum DrinkStatus {
      EMPTY, READY, STUCK, DROPPED;
    }
  }
  
  enum DrinkStatus {
    EMPTY, READY, STUCK, DROPPED;
  }
}

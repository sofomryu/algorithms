public class account {
	public static void main(String[] args) {
		double vos = Double.parseDouble(args[0]);
		double vat = vos*0.1;
		double total = vos+vat;
		double expense = total*0.3;
		double income = total-expense;
		double dividend1 = income *0.5;
		double dividend2= income * 0.3;
		double dividend3 = income *0.2;

		System.out.println("Value of Supply : "+(vos));
		System.out.println("VAT : "+(vat));
		System.out.println("Total : "+(total));
		System.out.println("Expense : "+(expense));
		System.out.println("Income : "+(income));
		System.out.println("Dividend1 : "+(dividend1));
		System.out.println("Dividend2 : "+(dividend2));
		System.out.println("Dividend3 : "+(dividend3));
	}
}

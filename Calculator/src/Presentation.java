import java.util.Scanner;

public class Presentation {
    public static void main(String[] args) {
        Scanner sca = new Scanner(System.in);

        String operator = verifyOperation(sca);

        System.out.println();
        System.out.println("Primeiro número: ");
        double num1 = verifyNumber(sca);
        System.out.println("Primeiro número escolhido: " + num1);

        System.out.println();
        System.out.println("Segundo número: ");
        double num2 = verifyNumber(sca);
        System.out.println("Segundo número escolhido: " + num2);

        System.out.println();
        System.out.println("Resultado da operação: " + calculate(operator, num1, num2));

        sca.close();
    }

    public static String verifyOperation(Scanner scannerOperation) {
        System.out.println();
        System.out.println("Escolha uma operação entre: +, -, x, /, ^, // e ///: ");

        String operation = scannerOperation.nextLine();

        while (!(operation.equals("+") ||
                operation.equals("-") ||
                operation.equals("x") ||
                operation.equals("/") ||
                operation.equals("^") ||
                operation.equals("//") ||
                operation.equals("///")
        )
        ) {
            System.out.println("Tente novamente: ");
            operation = scannerOperation.nextLine();
        }
        System.out.println("Operação escolhida: " + operation);

        return operation;
    }

    public static double verifyNumber(Scanner scannerNumber) {
        double number;

        while (true) {
            String enterNumber = scannerNumber.nextLine();

            try {
                number = Double.parseDouble(enterNumber);
                break;
            }
            catch (NumberFormatException e) {
                System.out.println("Tente novamente: ");
            }
        }
        return number;
    }

    public static double calculate(String operate, double numX, double numY) {
        if (operate.equals("+")) {
            return Calculations.adi(numX, numY);
        }

        if (operate.equals("-")) {
            return Calculations.sub(numX, numY);
        }

        if (operate.equals("x")) {
            return Calculations.multi(numX, numY);
        }

        if (operate.equals("/")) {
            return Calculations.div(numX, numY);
        }

        if (operate.equals("^")) {
            return Calculations.pot(numX, numY);
        }

        if (operate.equals("//")) {
            return Calculations.rad2(numX);
        }

        return Calculations.rad3(numX);
    }
}

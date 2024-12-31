import java.util.Scanner;

public class Presentation {
    public static final Scanner sca = new Scanner(System.in);

    public static void main(String[] args) {
        String resp = "Sim";

        while (resp.equalsIgnoreCase("Sim") ||
               resp.equalsIgnoreCase("s")) {

            String operator = verifyOperation();

            System.out.println();
            System.out.println("Primeiro número: ");
            double num1 = verifyNumber();
            System.out.println("Primeiro número escolhido: " + num1);

            System.out.println();
            System.out.println("Segundo número: ");
            double num2 = verifyNumber();
            System.out.println("Segundo número escolhido: " + num2);

            System.out.println();
            System.out.println("Resultado da operação: " + calculate(operator, num1, num2));

            System.out.println();
            System.out.println("Deseja continuar? ");

            resp = sca.nextLine();

            while (!(resp.equalsIgnoreCase("Sim") ||
                    resp.equalsIgnoreCase("s") ||
                    resp.equalsIgnoreCase("Não") ||
                    resp.equalsIgnoreCase("Nao") ||
                   resp.equalsIgnoreCase("N"))) {
                System.out.println("Resposta inválida, tente novamente: ");
                resp = sca.nextLine();
            }

            if (resp.equalsIgnoreCase("Não") ||
                resp.equalsIgnoreCase("Nao") ||
                resp.equalsIgnoreCase("N" )) {
                break;
            }
        }
        sca.close();
    }

    public static String verifyOperation() {
        System.out.println();
        System.out.println("Escolha uma operação entre: +, -, x, /, ^, // e ///: ");

        String operation = sca.nextLine();

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
            operation = sca.nextLine();
        }
        System.out.println("Operação escolhida: " + operation);

        return operation;
    }

    public static double verifyNumber() {
        double number;

        while (true) {
            String enterNumber = sca.nextLine();

            try {
                number = Double.parseDouble(enterNumber);
                break;
            } catch (NumberFormatException e) {
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

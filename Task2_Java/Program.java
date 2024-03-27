package IntermediateWorkSpecializationBlock.Task2_Java;

public class Program {
    public static void main(String[] args) {
        System.out.println("Добро пожаловать!");
        String fileName = "input.txt";
        Proccessing proc = new Proccessing();
        proc.proccessing(fileName);
        System.out.println("До новых встреч!");
    }
}


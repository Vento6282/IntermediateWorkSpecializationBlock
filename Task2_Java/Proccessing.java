package IntermediateWorkSpecializationBlock.Task2_Java;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;

public class Proccessing {

    public void proccessing(String fileName){
        String text = "";
        try {
            text = readFile(fileName);
        } catch (IOException e) {
            e.printStackTrace();
        }
        if(text == ""){
            System.out.println("В файле нет данных!");
        } else {
            text = prepareText(text.trim());
            countValues(text);
            longestWord(text);
            quantityEachValue(text);
        }
    }

    public void countValues(String text){
        String[] array = text.split(" ");
        System.out.println("В файле найдено всего слов - " + array.length + ".");
    }

    public void longestWord(String text){
        String[] array = text.split(" ");
        int maxLength = array[0].length();
        HashSet<String> words = new HashSet<String>();
        for (String string : array) {
            if(string.length() > maxLength){
                words.clear();
                maxLength = string.length();
                words.add(string);
            } else if (string.length() == maxLength){
                words.add(string);
            }
        }
        String lineWords = "";
        for (String string : words) {
            lineWords = lineWords + " " + string; 
        }
        if(words.size() == 1){
            System.out.println("Самое длинное слово в файле - " + lineWords.trim() + ".");
        } else {
            System.out.println("С максимальной длиной " + maxLength + " найдено несколько слов: " + lineWords.trim().replace(" ", ", ") );
        }
    }

    public void quantityEachValue(String text){
        String[] array = text.split(" ");
        HashMap<String, Integer> list = new HashMap<>();
        for (String string : array) {
            if(list.containsKey(string)){
                list.put(string, list.get(string) + 1);
            } else {
                list.put(string, 1);
            }
        }
        System.out.println("Анализ, сколько раз каждое слово встречается в файле: ");
        for(int i = array.length; i >= 1 ; i--)
            for (String string : list.keySet()) {
                if(list.get(string) == i){
                    System.out.println(string + ": " + list.get(string));
                }
            }
    }

    public String prepareText(String text){
        while (text.contains("  ")){
            text = text.replaceAll("  ", " ");
        }
        return text;
    }

    public String readFile(String fileName) throws IOException {
        String text = "";
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line = "";
            while ((line = reader.readLine()) != null) {
                text = text.trim() + " " + line.trim();
            }
        }
        return text;
    }

}

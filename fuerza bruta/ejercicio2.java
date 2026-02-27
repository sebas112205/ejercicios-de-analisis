import java.util.ArrayList;

public class ejercicio2 {
    public static void main (String[] args)
    {
        int[] array = {-1,2,6,7,-9,8,-10,15};
        maxima(array);
    }
    public static void maxima(int[] array)
    {
        int conteo = 0;
        ArrayList<Integer> resultado = new ArrayList<>();
        for (int i=0;i < array.length; i++)
            {
                if (array.length > conteo)
                    {
                        for (int j=0;j<array.length -1; j++)
                            {
                                int pos1 = array[i];
                                int pos2 = array[j+1];
                                int suma = pos1 + pos2; 
                                if (suma > 0)
                                    {
                                        resultado.add(suma);
                                        
                                    }
                            }
                    }
            }
    }
}

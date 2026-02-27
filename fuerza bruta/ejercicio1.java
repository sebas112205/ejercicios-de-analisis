public class ejercicio1 {
    // CAMBIO 1: Debe ser String[] args
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
        int x = 15;
        suma(array, x);
    }

    public static void suma(int[] array, int x) {
        // CAMBIO 2: Ajustamos límites para evitar el error de índice 12
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array.length - 1; j++) { // Restamos 1 porque usas j+1
                if (i != j) {
                    for (int k = 0; k < array.length - 1; k++) { // Restamos 1 porque usas k+1
                        if (k == j) {
                            int pos1 = array[i];
                            int pos2 = array[j + 1];
                            int pos3 = array[k + 1];
                            
                            int sumas = pos1 + pos2 + pos3;
                            
                            if (sumas == x) {
                                // Imprimimos los números que sumaron x para ver el resultado
                                System.out.println("Encontrado: " + pos1 + " + " + pos2 + " + " + pos3 + " = " + sumas);
                            }
                        }
                    }
                }
            }
        }
    }
}
import java.util.Random;

public class random_generator {
	public static void rand_generator(int size) {
		Random random = new Random();
		for (int i = 0; i < size; i++) {
			System.out.print(random.nextInt(2));
		}
	}

	public static void main(String[] args) {
		int BITS = 128;
		rand_generator(BITS);
	}
}
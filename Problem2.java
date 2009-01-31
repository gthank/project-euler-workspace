public final class Problem2 {
    private Problem2() {
        // Intentionally blank
    }

    private static final int fib(final int term) {
        if (1 >= term) {
            return 1;
        }
        return fib(term - 2) + fib(term - 1);
    }

    public static final int problem2() {
        int sum = 0;
        // I precalculated the max term that is less than 4 mil; it was 32.
        for (int i = 0; i < 33; i++) {
            final int currentFib = fib(i);
            if (0 == currentFib % 2) {
                sum += currentFib;
            }
        }
        return sum;
    }

    public static void main(final String... args) {
        System.out.println(problem2());
    }
}


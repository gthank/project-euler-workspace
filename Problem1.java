/**
 * Finds the solution to Problem 1 from Project Euler.
 *
 * For more details, see <a href="http://projecteuler.net/index.php?section=problems&id=1" title="Problem 1 of Project Euler">Project Euler, Problem 1</a>.
 */
public final class Problem1 {
    private Problem1() {
        // Intentionally blank
    }

    /**
     * Sums the natural numbers less than 1000 that are multiples of 3 or 5.
     *
     * @return the result.
     */
    public static int problem1() {
        int sum = 0;
        for (int n = 3; n < 1000; n++) {
            if ((0 == (n % 3)) || (0 == (n % 5))) {
                sum += n;
            }
        }
        return sum;
    }

    public static void main(final String... args) {
        System.out.println(problem1());
    }
}


public class nullsteps {
    public static void main(String[] args) {
	System.out.printf("%d\n", numWays(6, 13));
    }
    
    public static int numWays(int steps, int arrLen) {
        // int mod = 10 ^ 9 + 7;
	int mod = 1000000007;
	System.out.printf("mod %d\n", mod);
        int[] pos = new int[arrLen], npos = new int[arrLen];
        pos[0] = 1;
        for (int s = 0; s < steps; s++) {
            for (int i = 0; i < arrLen; i++) {
                npos[i] = pos[i];
                if (i > 0) npos[i] = (npos[i] + pos[i - 1]) % mod;
                if (i < arrLen - 1) npos[i] = (npos[i] + pos[i + 1]) % mod;
            }
            for (int i = 0; i < arrLen; i++) {
                pos[i] = npos[i];
            }
	    System.out.printf("%d %d %d\n", pos[0], pos[1], pos[2]);
        }
        return pos[0];
    }
}

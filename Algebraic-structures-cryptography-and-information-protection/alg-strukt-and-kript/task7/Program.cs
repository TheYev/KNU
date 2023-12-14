int modulo(int Base, int exponent, int mod)
{
    int x = 1;
    int y = Base;

    while (exponent > 0)
    {
        if (exponent % 2 == 1)
            x = (x * y) % mod;

        y = (y * y) % mod;
        exponent = exponent / 2;

    }
    return x % mod;
}

int Jacobi(int a, int n)
{
    if (n <= 0 || n % 2 == 0)
    {
        throw new ArgumentException("The parameter 'n' must be a natural odd number.");
    }

    a = a % n;
    int t = 1;
    int r;

    while (a != 0)
    {
        while (a % 2 == 0)
        {
            a /= 2;
            r = n % 8;
            if (r == 3 || r == 5)
            {
                t = -t;
            }
        }
        r = n;
        n = a;
        a = r;

        if (a % 4 == 3 && n % 4 == 3) t = -t;

        a = a % n;
    }

    if (n == 1) return t;
    else return 0;
}

bool solovoyStrasen(int p, int iteration)
{
    if (p < 2)
        return false;
    if (p != 2 && p % 2 == 0)
        return false;

    // Create Object for Random Class
    Random rand = new Random();
    for (int i = 0; i < iteration; i++)
    {

        // Generate a random number r
        int r = Math.Abs(rand.Next());
        int a = r % (p - 1) + 1;
        int jacobian = (p + Jacobi(a, p)) % p;
        int mod = modulo(a, (p - 1) / 2, p);

        if (jacobian == 0 || mod != jacobian)
            return false;
    }
    return true;
}

void Main()
{
    int iteration = 50;
    int a = 13;//10
    bool test = solovoyStrasen(a, iteration);
    if (test) Console.WriteLine("is prime");
    else Console.WriteLine("not composite");
}

Main();
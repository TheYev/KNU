//Jacobi
int Jacobi(int a, int n)
{
    if (n <= 0 || n % 2 == 0)
    {
        throw new ArgumentException("Параметр 'n' повинен бути натуральним непарним числом.");
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
//Lejandra
bool IsPrime(long N)
{
    if (N < 0) return false;

    if (N == 2 || N == 1) return true;

    if (N % 2 == 0) return false;

    for (long k = 3; k <= Math.Sqrt(N); k += 2)
    {
        if (N % k == 0) return false;
    }

    return true;
}

int Lejandra(long a, long p)
{
    if (p < 3 || !IsPrime(p) || a % p == 0) return 0;

    return (Math.Pow(a, (p - 1) / 2) % p) == 1 ? 1 : -1;
}

void Main()
{
    int a = Jacobi(11, 11);//7,11
    Console.WriteLine("Jacobi: " + a);

    int b = Lejandra(7, 11);//11,11
    Console.WriteLine("Lejandra: " + b);
}

Main();
//Eilor function
int eilorFunk(int n)
{
    int ret = 1;
    for (int i = 2; i * i <= n; ++i)
    {
        int p = 1;
        while (n % i == 0)
        {
            p *= i;
            n /= i;
        }
        if ((p /= i) >= 1) ret *= p * (i - 1);
    }
    if (--n != 0) return n * ret;
    else return ret;
}

//Mobius function
bool isPrime(int n)
{
    if (n == 2) return true;

    if (n % 2 == 0) return false;
    for (int i = 3; i * i <= n / 2; i += 2)
        if (n % i == 0) return false;
    return true;
}

int mobiusFunction(int N)
{
    if (N == 1) return 1;
    int p = 0;

    for (int i = 2; i <= N; i++)
    {
        if (N % i == 0 && isPrime(i))
        {
            if (N % (i * i) == 0) return 0;
            else p++;
        }
    }
    if (p % 2 != 0) return -1;
    else return 1;
}

//NSK for arr number
int LCM(int a, int b)
{
    return (a * b / GCD(a, b));
}

int GCD(int a, int b)
{
    while (b != 0)
    {
        var t = b;
        b = a % b;
        a = t;
    }
    return a;
}

int FindLCM(int[] numbers)
{
    int result = numbers[0];
    for (int i = 1; i < numbers.Length; i++)
    {
        result = LCM(result, numbers[i]);
    }
    return result;
}

void Main()
{
    //Eliot
    int testEilor = 10;
    int eilor = eilorFunk(testEilor);
    Console.WriteLine("Eliot: ");
    Console.WriteLine(eilor);

    //Mobius
    int testMobius = 10;
    int mobius = mobiusFunction(testMobius);
    Console.WriteLine("Mobius: ");
    Console.WriteLine(mobius);

    //NSK
    int[] nsk = { 18, 30 };
    int nskTest = FindLCM(nsk);
    Console.WriteLine("NSK: ");
    Console.WriteLine(nskTest);
}

Main();
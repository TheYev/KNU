using System;

class Program
{
    static int LegendreSymbol(int a, int p)
    {
        if (a % p == 0)
        {
            return 0;
        }
        else if ((int)Math.Pow(a, (p - 1) / 2) % p == 1)
        {
            return 1;
        }
        else
        {
            return -1;
        }
    }

    static int TonelliShanks(int a, int p)
    {
        if (LegendreSymbol(a, p) != 1)
        {
            return -1;
        }

        int q = p - 1;
        int s = 0;
        while (q % 2 == 0)
        {
            q /= 2;
            s++;
        }

        if (s == 1)
        {
            return (int)Math.Pow(a, (p + 1) / 4) % p;
        }

        int z = 1;
        while (LegendreSymbol(z, p) != -1)
        {
            z++;
        }

        int c = (int)Math.Pow(z, q) % p;
        int r = (int)Math.Pow(a, (q + 1) / 2) % p;
        int t = (int)Math.Pow(a, q) % p;
        int m = s;
        int t2 = 0;

        while ((t - 1) % p != 0)
        {
            t2 = (t * t) % p;
            int i;
            for (i = 1; i < m; i++)
            {
                if ((t2 - 1) % p == 0)
                {
                    break;
                }
                t2 = (t2 * t2) % p;
            }
            int b = (int)Math.Pow(c, 1 << (m - i - 1)) % p;
            r = (r * b) % p;
            c = (b * b) % p;
            t = (t * c) % p;
            m = i;
        }

        return r;
    }

    static void Main()
    {
        int test_a = 10;
        int test_p = 13;//29

        int result = TonelliShanks(test_a, test_p);
        Console.WriteLine(result);
    }
}

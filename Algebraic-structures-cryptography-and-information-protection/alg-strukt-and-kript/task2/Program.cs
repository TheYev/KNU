//task 2
int ModInverse(int a, int m)
{
    int m0 = m, x0 = 0, x1 = 1;

    while (a > 1)
    {
        int q = a / m;
        int t = m;

        m = a % m;
        a = t;

        t = x0;
        x0 = x1 - q * x0;
        x1 = t;
    }

    if (x1 < 0) x1 += m0;

    return x1;
}

int China(List<Tuple<int, int>> congruences)
{
    int n = congruences.Count;
    int M = 1;
    int result = 0;

    foreach (var congruence in congruences)
    {
        M *= congruence.Item2;
    }

    for (int i = 0; i < n; i++)
    {
        int Mi = M / congruences[i].Item2;
        int MiInv = ModInverse(Mi, congruences[i].Item2);
        result += congruences[i].Item1 * Mi * MiInv;
    }

    return result % M;
}

void Main()
{
    List<Tuple<int, int>> congruences = new List<Tuple<int, int>>
        {
            Tuple.Create(2, 3),
            Tuple.Create(3, 5),
            Tuple.Create(2, 7)
        };

    int result = China(congruences);
    Console.WriteLine("res: " + result);
}

Main();

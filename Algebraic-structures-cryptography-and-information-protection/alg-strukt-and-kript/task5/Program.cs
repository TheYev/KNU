int BabyStepGiantStep(int baseVal, int target, int modulus)
{
    // Визначаємо межу для великого кроку
    int m = (int)Math.Sqrt(modulus) + 1;

    // Знаходимо a^m mod p
    int a = ModPow(baseVal, m, modulus);

    // Обчислюємо таблицю малих кроків
    Dictionary<int, int> smallStepTable = new Dictionary<int, int>();

    for (int j = 0; j < m; j++)
    {
        int u = ModPow(baseVal, j, modulus);
        smallStepTable[u] = j;
    }

    // Шукаємо великий крок
    int v = target;
    for (int i = 0; i < m; i++)
    {
        // Обчислюємо v * a^(-i) mod p
        v = (int)((long)v * ModInverse(a, modulus) % modulus);

        // Перевіряємо, чи є це значення в таблиці малих кроків
        if (smallStepTable.ContainsKey(v))
        {
            // Знайшли великий крок
            int j = smallStepTable[v];
            int result = i * m + j;
            return result;
        }
    }

    return -1; // Дискретний логарифм не знайдено
}

int ModPow(int x, int y, int mod)
{
    int result = 1;
    for (int i = 0; i < y; i++)
    {
        result = (int)((long)result * x % mod);
    }
    return result;
}

int ModInverse(int a, int m)
{
    int m0 = m;
    int x0 = 0, x1 = 1;

    if (m == 1)
        return 0;

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

    if (x1 < 0)
        x1 += m0;

    return x1;
}

void Main()
{
    int baseVal = 2;
    int target = 8;
    int modulus = 11;

    int result = BabyStepGiantStep(baseVal, target, modulus);
    Console.WriteLine("Result: " + result);
}

Main();
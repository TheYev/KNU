int PollardRho(int n)
{
    // Ініціалізуємо змінні x, y і d
    int x = 2;
    int y = 2;
    int d = 1;

    // Функція для обчислення f(x) = x^2 + 1 (модуль n)
    int f(int num)
    {
        int numSquared = num * num;
        return (numSquared + 1) % n;
    }

    // Пошук спільного дільника
    while (d == 1)
    {
        x = f(x);
        y = f(f(y));

        // Використовуємо великий спільний дільник для n та |x - y|
        int temp = Math.Abs(x - y);
        int gcdResult = GCD(temp, n);
        d = gcdResult;
    }

    return d;
}

int GCD(int a, int b)
{
    while (b != 0)
    {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

void Main()
{
    Console.WriteLine("task4");
    Console.Write("Enter a number to factorize: ");
    int number = int.Parse(Console.ReadLine());

    Console.WriteLine("Prime factors of " + number + " are:");
    while (number != 1)
    {
        int factor = PollardRho(number);
        if (factor == number)
        {
            Console.WriteLine(number); // number is prime
            break;
        }
        Console.WriteLine(factor);
        number /= factor;
    }
}

Main();

using System;

class ElGamalEllipticCurve
{
    // Представлення еліптичної кривої: y^2 = x^3 + ax + b
    private int a;
    private int b;

    public ElGamalEllipticCurve(int a, int b)
    {
        this.a = a;
        this.b = b;
    }

    // Перевірка, чи належить точка (x, y) еліптичній кривій
    private bool IsPointOnCurve(int x, int y)
    {
        return y * y == x * x * x + a * x + b;
    }

    // Множення точки (x1, y1) на скаляр k
    private Tuple<int, int> MultiplyPoint(int x1, int y1, int k)
    {
        int x = x1;
        int y = y1;
        for (int i = 1; i < k; i++)
        {
            x += x1;
            y += y1;
            //if (!IsPointOnCurve(x, y))
            //{
            //    throw new Exception("Точка не належить кривій");
            //}
        }
        return new Tuple<int, int>(x, y);
    }

    public Tuple<Tuple<int, int>, Tuple<int, int>> GenerateKeys(int basePointX, int basePointY, int privateKey)
    {
        // basePointX, basePointY - координати базової точки на кривій
        // privateKey - закритий ключ

        // Генерація публічного ключа
        Tuple<int, int> publicKey = MultiplyPoint(basePointX, basePointY, privateKey);

        // Пара (публічний ключ, базова точка)
        return new Tuple<Tuple<int, int>, Tuple<int, int>>(publicKey, new Tuple<int, int>(basePointX, basePointY));
    }

    public Tuple<int, int> Encrypt(Tuple<int, int> basePoint, Tuple<int, int> publicKey, int message, int k)
    {
        // basePoint - базова точка на кривій
        // publicKey - публічний ключ
        // message - повідомлення, яке потрібно зашифрувати
        // k - випадкове число для шифрування

        // Шифрування повідомлення
        Tuple<int, int> encrypted = MultiplyPoint(basePoint.Item1, basePoint.Item2, k);
        int cipherText = message * publicKey.Item1 + encrypted.Item1;

        return new Tuple<int, int>(encrypted.Item1, cipherText);
    }

    public int Decrypt(int cipherText, int privateKey, int basePointX)
    {
        // Розшифрування повідомлення
        int decrypted = cipherText - privateKey * basePointX;
        return decrypted;
    }
}

class Program
{
    static void Main()
    {
        // Параметри еліптичної кривої
        int a = 2;
        int b = 3;

        ElGamalEllipticCurve ellipticCurve = new ElGamalEllipticCurve(a, b);

        // Параметри базової точки на кривій
        int basePointX = 5;
        int basePointY = 7;

        // Приватний ключ
        int privateKey = 11;

        // Генерація ключів
        var keys = ellipticCurve.GenerateKeys(basePointX, basePointY, privateKey);
        var publicKey = keys.Item1;
        var basePoint = keys.Item2;

        // Повідомлення для шифрування
        int message = 10;

        // Випадкове число для шифрування
        int k = 13;

        // Шифрування повідомлення
        var encrypted = ellipticCurve.Encrypt(basePoint, publicKey, message, k);

        Console.WriteLine("Encrypted message:");
        Console.WriteLine("C1: " + encrypted.Item1);
        Console.WriteLine("C2: " + encrypted.Item2);

        // Розшифрування повідомлення
        int decrypted = ellipticCurve.Decrypt(encrypted.Item2, privateKey, basePointX);

        Console.WriteLine("\nDecrypted message:");
        Console.WriteLine(decrypted);
    }
}

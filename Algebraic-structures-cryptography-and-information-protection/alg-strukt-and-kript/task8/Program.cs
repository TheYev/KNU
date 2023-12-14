using System;
using System.Numerics;

class RSA
{
    public BigInteger Encrypt(BigInteger message, BigInteger publicKey, BigInteger modulus)
    {
        return BigInteger.ModPow(message, publicKey, modulus);
    }

    public BigInteger Decrypt(BigInteger ciphertext, BigInteger privateKey, BigInteger modulus)
    {
        return BigInteger.ModPow(ciphertext, privateKey, modulus);
    }
}

class Program
{
    static void Main()
    {
        BigInteger modulus = 3233; // Приклад значення модуля (n)
        BigInteger publicKey = 17; // Публічний ключ (e)
        BigInteger privateKey = 413; // Приватний ключ (d)

        BigInteger plaintext = 123;//наше повідомленя для шифрування/дешифрування повинно бути меншим за modulus

        RSA rsa = new RSA();

        BigInteger ciphertext = rsa.Encrypt(plaintext, publicKey, modulus);//шифруванян plaintext

        Console.WriteLine("Encrypt: " + ciphertext);

        BigInteger decryptedMessage = rsa.Decrypt(ciphertext, privateKey, modulus);//розшифрування plaintext

        Console.WriteLine("Decrypt: " + decryptedMessage);
    }
}

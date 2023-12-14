using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

class TaskGoLang
{
    private List<Tuple<string, string>> typeLexem;

    public TaskGoLang()
    {
        typeLexem = new List<Tuple<string, string>>
        {
            Tuple.Create("RESERVEDWORDS", "^(package|import|func|var|const|if|else|for|range|return|true|false|int|fmt|Println|float|string|bool)$"),
            Tuple.Create("IDENTIFIER", "^[a-zA-Z_][a-zA-Z0-9_]*$"),
            Tuple.Create("NUMBER", "^(\\d+)$"),
            Tuple.Create("STRING", "^(\"[^\"]*\")"),
            Tuple.Create("OPERATOR", "^(\\+|-|\\*|/|==|!=|<|>|<=|>=|:=|&|\\||\\^|<<|>>|&&|\\|\\||!)$"),
            Tuple.Create("PUNCTUATIONSIGNS", "^[\\.,;:\\[\\]{}()]$"),
            Tuple.Create("COMMENT", "^//.*$")
        };
    }

    public List<Tuple<string, string>> Analiz(string codeExample)
    {
        var lexems = new List<Tuple<string, string>>();
        var wordsRegex = new Regex("//.*|\"[^\"]*\"|\\d+|\\w+|[\\.,;:\\[\\]{}()]|\\+|-|\\*|/|==|!=|<|>|<=|>=|:=|&|\\||\\^|<<|>>|&&|\\|\\||!");
        var matches = wordsRegex.Matches(codeExample);

        foreach (Match match in matches)
        {
            string word = match.Value;
            string lexemaType = "ERROR";

            foreach (var pattern in typeLexem)
            {
                if (Regex.IsMatch(word, pattern.Item2) && lexemaType == "ERROR")
                {
                    lexemaType = pattern.Item1;
                }
            }

            lexems.Add(Tuple.Create(word, lexemaType));
        }

        return lexems;
    }
}

class Program
{
    static void Main()
    {
        string example =
            "package main" +
            "import \"fmt\"" +
            "func main() {" +
            "   fmt.Println(\"Hello, World!\")" +
            "   var number1, number2, number3 int" +
            "   number1 = 99" +
            "   number2 = 81" +
            "   number3 = number1 + number2" +
            "   fmt.Println(number3)" +
            "   //comment" +
            "}";


        TaskGoLang test = new TaskGoLang();
        var result = test.Analiz(example);
        foreach (var res in result)
        {
            Console.WriteLine($"{res.Item1} => {res.Item2}");
        }
    }
}

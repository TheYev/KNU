#include <iostream>
#include <vector>
#include <string>
#include <regex>
#include <utility>

using namespace std;
class AssemblerLexerFinalV2 {
public:
    AssemblerLexerFinalV2() {
        token_patterns = {
                {"NUMBER_FLOAT", "^\\d*\\.\\d+$"},
                {"NUMBER_DEC", "^\\d+$"},
                {"NUMBER_HEX", "^0[xX][0-9a-fA-F]+$"},
                {"STRING_CONST", "^\".*\"$"},
                {"CHAR_CONST", "^'.*'$"},
                {"PREPROCESSOR", "^#[a-zA-Z_]\\w*$"},
                {"COMMENT", "^;.*$"},
                {"RESERVED_WORD", "^(MOV|ADD|SUB|DIV|MUL)$"},
                {"OPERATOR", "^(AND|OR|XOR)$"},
                {"SEPARATOR", "^[\\.,;:\\[\\]{}()]$"},
                {"IDENTIFIER", "^[a-zA-Z_][a-zA-Z0-9_]*$"},
        };
    }

    vector<pair<string, string>> tokenize(const string& text) {
        vector<pair<string, string>> tokens;
        regex words_regex(";.*|\\d*\\.\\d+|\\w+|[\\.,;:\\[\\]{}()]");
        smatch match;

        string::const_iterator searchStart(text.cbegin());

        while (regex_search(searchStart, text.cend(), match, words_regex)) {
            string word = match[0];
            string token_type = "ERROR";

            for (const auto& pattern : token_patterns) {
                if (regex_match(word, regex(pattern.second))) {
                    token_type = pattern.first;
                    break;
                }
            }

            tokens.emplace_back(word, token_type);
            searchStart = match.suffix().first;
        }

        return tokens;
    }

private:
    vector<pair<string, string>> token_patterns;
};

int main() {
    string sample_code =
            "MOV AX, 1\n"
            "ADD BX, AX\n"
            "SUB CX, 0x10\n"
            "; This is a comment\n"
            "#directive\n"
            "MOV AL, 'a'\n"
            "DIV DX, 3.14\n";

    AssemblerLexerFinalV2 lexer_final_v2;
    auto tokens_final_v2 = lexer_final_v2.tokenize(sample_code);
    for (const auto& token : tokens_final_v2) {
        cout << "(" << token.first << " | " << token.second << ")" << endl;
    }

    return 0;
}
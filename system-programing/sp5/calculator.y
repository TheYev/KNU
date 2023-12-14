%{
#include <stdio.h>
#include <stdlib.h>
int yylex();
void yyerror(const char*);
%}

%token NUMBER
%left '+' '-'
%left '*' '/'

%%

calclist: /* пустий вираз */
    | calclist exp '\n' { printf("= %d\n", $2); }
    ;

exp: NUMBER
    | exp '+' exp { $$ = $1 + $3; }
    | exp '-' exp { $$ = $1 - $3; }
    | exp '*' exp { $$ = $1 * $3; }
    | exp '/' exp { 
        if ($3 != 0) 
            $$ = $1 / $3; 
        else {
            yyerror("Ділення на нуль");
            exit(1);
        }
    }
    | '(' exp ')' { $$ = $2; }
    | '-' exp %prec '-' { $$ = -$2; } /* унарний мінус */
    ;

%%

void yyerror(const char *s) {
    printf("Помилка: %s\n", s);
}

int main() {
    yyparse();
    return 0;
}

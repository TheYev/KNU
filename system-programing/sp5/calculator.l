%{
#include <stdio.h>
#include <stdlib.h>
#include "y.tab.h"
%}

%%
[0-9]+      { yylval = atoi(yytext); return NUMBER; }
[-+*/()=\n] { return *yytext; }
[ \t]       ; /* пропуск пробілів і табуляцій */
.           { printf("Невідомий символ\n"); }

%%

int yywrap() {
    return 1;
}

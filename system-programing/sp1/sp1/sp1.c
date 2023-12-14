#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#pragma warning(disable: 4996)

double calculateChastka(const char* word) {
    int count = 0;
    int length = strlen(word);

    for (int i = 0; word[i] != '\0'; i++) {
        if (isalpha(word[i])) {
            char lowerC = tolower(word[i]);
            if (lowerC == 'a' || lowerC == 'e' || lowerC == 'i' || lowerC == 'o' || lowerC == 'u' || lowerC == 'y') {
                count++;
            }
        }
    }

    return (double)count / length;
}

int sorFunk(const void* a, const void* b) {
    const char* aWord = *(const char**)a;
    const char* bWord = *(const char**)b;

    double calculateA = calculateChastka(aWord);
    double calculateB = calculateChastka(bWord);

    if (calculateA < calculateB) {
        return -1;
    }
    else if (calculateA > calculateB) {
        return 1;
    }
    else {
        return 0;
    }
}

int main() {
    FILE* inputFile = fopen("labSP.txt", "r");

    char buffer[30];
    int wordCount = 0;
    int wordCapacity = 150;
    char** words = (char**)malloc(wordCapacity * sizeof(char*));

    while (fscanf(inputFile, "%s", buffer) != EOF) {
        char* notLetter = strtok(buffer, "()+-`'");

        while (notLetter != NULL) {
            if (wordCount == wordCapacity) {
                wordCapacity += 1;
                char** newWords = (char**)realloc(words, wordCapacity * sizeof(char*));
                if (!newWords) {
                    printf("ERROR\n");
                    return 1;
                }
                words = newWords;
            }

            words[wordCount] = strdup(notLetter);
            if (!words[wordCount]) {
                printf("ERROR\n");
                return 1;
            }

            wordCount++;

            notLetter = strtok(NULL, "()+-`'");
        }
    }



    qsort(words, wordCount, sizeof(char*), sorFunk);

    for (int i = 0; i < wordCount; i++) {
        printf("%s\n", words[i]);
    }

    free(words);
    fclose(inputFile);

    return 0;
}

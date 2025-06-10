#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int preassemble(FILE* result, FILE* source) {
	int j, ii,recordingMacro = 0,wasMacro = 0, macroIndex = 0, macroInternalIndex = 0;
	char line[100];
	char macros[100][100][100];
	char macro_names[10][10];
	char currentChar;
	char *macro_name;
	memset(macro_names, 0, 10*10);
	memset(macros, 0, 1000);

	for	 ( ; 1; ) {
		currentChar = fgetc(source);
		for ( ii = 0; currentChar != '\n' && currentChar != EOF; ii++) 
		{
			line[ii] = currentChar;
			currentChar = fgetc(source);
		}		
		if (currentChar == EOF) break;
		line[ii] = '\0';
		wasMacro = 0;
		for (j = 0; j < macroIndex; j++) {
			if (strcmp(line, macro_names[j]) == 0) {
				fprintf(result, "%s", (char *)macros[macroIndex]);
				wasMacro = 1; 
			}	
		}
		if (wasMacro) 
			continue;
		if (recordingMacro) {
			if (strncmp("mcroend", line, strlen("mcroend")) == 0) {
				recordingMacro = 0;
				macroIndex++;
				continue;
			}
			strlcpy((char *)&macros[macroIndex][macroInternalIndex++], line, 10);
			continue;
		}

		if (strncmp("mcro", line, strlen("mcro")) == 0) {
			recordingMacro = 1;
			macro_name = strchr(line, ' ');
			macro_name++;
			macroInternalIndex = 0;
			strlcpy(macro_names[macroIndex], macro_name, 10);
			continue;
		}

		if ( fprintf(result, "%s\n", line) == -1) {
			perror("Error writing result to file");
		}
		printf("end");
		fflush(stdout);
	}
	return 0;
}

int main(void) {
	FILE *result, *source;
	result = fopen("./result.asm", "w");
	if (!result) {
		perror("Error opening result.asm");
		exit(1);
	}
	source = fopen("./before.asm", "r");
	if (!source) {
		perror("Error opening result.asm");
		exit(1);
	}
	preassemble(result, source);
	
	fclose(result);
	fclose(source);
}

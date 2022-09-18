
#include <stdio.h>
#include <stdlib.h>

#define STACK_SIZE 100

void push(char input);
void print(void);
char pop(void);
char peek(void);
char getch(void);
void del(void);
int isEmpty(void);
int getSize(void);
char stack[STACK_SIZE];
int top = -1;

int main(void)
{
	int sel = 1;
	char ch;
	
	while(sel!=0)
	{
		system("cls");
		printf("<Menu>\n");
		printf("0. quit\n");
		printf("1. printf\n");
		printf("2. push\n");
		printf("3. pop\n");
		printf("4. peek\n");
		printf("5. dal\n");
		printf("6. isEmpty\n");
		printf("7. getSize\n");
		printf("--------------\n");
		scanf("%d", &sel);
		switch (sel)
		{
			case 1:;
				print();
				break;
			case 2:;
				scanf(" %c", &ch);
				push(ch);
				break;
			case 3:;
				if(!isEmpty())
					printf("pop data: %c\n", pop());
				break;
			case 4:;
				if(!isEmpty())
					printf("data: %c\n", peek());
				break;
			case 5:;
				if(!isEmpty())
					del();
				break;
			case 6:;
				if(!isEmpty())
					printf("state: Empty !");
				else
					printf("state: Not Empty !");
				break;
			case 7:;
				printf("size: %d\n", getSize());
				break;
		}
		getch();
	}
	
	return 0;
 } 
 
 void push(char input)
 {
 	if (top >= (STACK_SIZE - 1))
 	{
 		printf("Full !");
 		exit(0);
	 }
	 stack[++top] = input;
 }
 void print(void)
 {
 	int i;
 	
 	printf("<Stack>\n");
 	for (i = 0; i<=top; i++)
 		printf("%c ", stack[i]);
 	printf("\n\n");
 }
 
 char pop(void)
 {
 	if(top == -1)
 	{
 		printf("Empty !");
		exit (0); 
	}
	return stack[top];
 }
 void del(void)
 {
 	if(top ==-1)
 	{
 		printf("Empty !");
		exit (0); 
	}
	top--;
	
 }
 
 int isEmpty(void)
 {
 	if(top ==-1)
 		return 1;
 	else
 		return 0;
 }
 
 int getSize(void)
 {
 	return top +1;
 }
스택 구현.cpp
스택 구현.cpp 표시 중입니다.

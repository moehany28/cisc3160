%{ 
   /* Definition section */
  #include<stdio.h> 
  int flag=0; 
%} 
  
%token NUMBER 
  
%left '+' '-'
  
%left '*' '/' '%'
  
%left '(' ')'
  
/* Rules */
%% 
  
ArithmeticExpression: E{ 
  
         printf("\nAnswer=%d\n", $$); 
  
         return 0; 
  
        }; 
 E:E'+'E {$$=$1+$3;} 
  
 |E'-'E {$$=$1-$3;} 
  
 |E'*'E {$$=$1*$3;} 
  
 |E'/'E {$$=$1/$3;} 
  
 |E'%'E {$$=$1%$3;} 
  
 |'('E')' {$$=$2;} 
  
 | NUMBER {$$=$1;} 
  
 ; 
  
%% 

void main() 
{ 
   printf("\nEnter a basic arithmetic expression using any of the following symbols (+,-,*,/,()) : \n"); 
  
   yyparse(); 
   if(flag==0) 
   printf("\nEntered arithmetic expression is Valid\n\n"); 
} 
  
void yyerror() 
{ 
   printf("\nEntered arithmetic expression is Invalid\n\n"); 
   flag=1; 
} 

def __template_java(nome, matricula, nome_formatado) -> str : 
    return f"""/**
* Laboratorio X - Lab X
*
* @Author {nome} - {matricula}
*/

import java.util.Scanner;

public class {nome_formatado} {{
    public static void main(String[] args) {{
    	Scanner sc = new Scanner(System.in);
        
        sc.close();
    }}
}}
"""

def __template_python(nome, matricula) -> str : 
    return f"""# Laboratorio X - Lab X
#
# @Author {nome} - {matricula}

def main() :
    print(\"Hello World!!\")

if __name__ == "__main__" :
    main()
"""

def __template_c(nome, matricula) -> str : 
    return f"""// Laboratorio X - Lab X
//
// @Author {nome} - {matricula}

#include <stdio.h>

int main( int argc, char *argv[ ] ) {{
    printf("Hello World!!");
    return 0;
}}
"""

def __template_cpp(nome, matricula) -> str : 
    return f"""// Laboratorio X - Lab X
//
// @Author {nome} - {matricula}

#include <iostream>

int main(int argc, char *argv[]) {{
    std::cout << "Hello World!";
    return 0;
}}
"""

def __template_haskell(nome, matricula) -> str : 
    return f"""{{-
    Laboratorio X - Lab X

    @Author {nome} - {matricula}
-}}

main = putStrLn "Hello World!!"

"""

def __template_prolog(nome, matricula) -> str : 
    return f"""/**
* Laboratorio X - Lab X
*
* @Author {nome} - {matricula}
*/
    write('Hello World').
"""

def get_template(lang, nome, matricula, nome_formatado) -> str :
    if lang == "java" :
        return __template_java(nome, matricula, nome_formatado)
    elif lang == "python" :
        return __template_python(nome, matricula)
    elif lang == "c" :
        return __template_c(nome, matricula)
    elif lang == "c++" :
        return __template_cpp(nome, matricula)
    elif lang == "haskell" :
        return __template_haskell(nome, matricula)
    elif lang == "prologo" :
        return __template_prolog(nome, matricula)
    else :
        return ""

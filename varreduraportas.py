#              VARREDURA DE PORTAS, BADCONS

import socket

print('''

########     ###    ########   ######   #######  ##    ##  ######   #######    #####     #####    #######  
##     ##   ## ##   ##     ## ##    ## ##     ## ###   ## ##    ## ##     ##  ##   ##   ##   ##  ##     ## 
##     ##  ##   ##  ##     ## ##       ##     ## ####  ## ##              ## ##     ## ##     ##        ## 
########  ##     ## ##     ## ##       ##     ## ## ## ##  ######   #######  ##     ## ##     ##  #######  
##     ## ######### ##     ## ##       ##     ## ##  ####       ## ##        ##     ## ##     ## ##        
##     ## ##     ## ##     ## ##    ## ##     ## ##   ### ##    ## ##         ##   ##   ##   ##  ##        
########  ##     ## ########   ######   #######  ##    ##  ######  #########   #####     #####   ######### 
	                                                               
=-=-=-=-=-=-=-=-=-=-=-=-=-=-VARREDURA DE PORTAS  =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    |   [OPCAO]                    [TEMPO]        |
    |                                             |
    |   [1] - TOP PORTAS           (RÁPIDO)       |
    |   [2] - 0-1000               (MÉDIO)        |
    |   [3] - TODAS AS PORTAS      (LENTO)        |
               
                BADCONS2002
 
        ''')
try:
    op = int(input('<<< Digite sua opção >>> '))
    if op == 1:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5555, 5900, 8080, 8888]
    elif op == 2:
        ports = range(0, 1001)
    elif op == 3:
        ports = range(0, 65536)
    elif op >= 4 or op <= 0:
        print('[!] - ERRO NA SELECAO DE OPÇÃO...'); exit()
    target = str(input('\nALVO: '))
except:
    exit()
    print('[!] - ERRO NA SELECAO DE OPÇÃO...')
try:
    print('\tPORTA\tSTATUS')
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.settimeout(0.6)
        code = s.connect_ex((target, port))
        if code == 0:
            print(f"\t{port}\tABERTA")
except:
    exit()
    print('[!] IP OU SOCKET INVALIDO!')

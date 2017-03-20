#coding: UTF-8
import smtplib
print("""\033[1;31m
 __     __          _    _                        _____         
 \ \   / /         | |  | |                      / ____|        
  \ \_/ /    __ _  | |__| |   ___     ___       | |       _   _ 
   \   /    / _` | |  __  |  / _ \   / _ \      | |      | | | |
    | |    | (_| | | |  | | | (_) | | (_) |  _  | |____  | |_| |
    |_|     \__,_| |_|  |_|  \___/   \___/  (_)  \_____|  \__, |
                                                           __/ |
                                                          |___/ 
Coder > ejr_geek
GitHub > github.com/ejrgeek | Gmail.Cy v2.0
\033[0;0m""")
server = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
server.ehlo()

user = str(input("\033[1;34mSeu Email > \033[1;31m"))
senha = str(input("Sua Senha > \033[1;31m"))
para = str(input("Remetente > \033[1;31m"))
numero = int(input("\033[33mTotal de E-mails > \033[1;31m"))
msg = str(input("\033[36mInsira sua Mensagem > \033[1;31m"))

try:
	server.login(user, senha)
	print("\033[32mLogando\033[1;31m")
except:
	print("\033[31mEmail ou Senha errados || Permissao Negada\033[1;31m")

x = 0
while(x<numero):
	server.sendmail(user, para, msg)
	x=x+1
	print("\033[36mEnviado", x, "Email\033[1;31m")

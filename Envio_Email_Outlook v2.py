#coding: UTF-8
import smtplib
print("""\033[1;31m
   ____            _     _        _           _____         
  / __ \          | |   | |      | |         / ____|        
 | |  | |  _   _  | |_  | |      | | __     | |       _   _ 
 | |  | | | | | | | __| | |      | |/ /     | |      | | | |
 | |__| | | |_| | | |_  | |____  |   <   _  | |____  | |_| |
  \____/   \__,_|  \__| |______| |_|\_\ (_)  \_____|  \__, |
                                                       __/ |
                                                      |___/ 
Coder > ejr_geek
GitHub > github.com/ejrgeek | Gmail.Cy v2.0
\033[0;0m""")
server = smtplib.SMTP('smtp.live.com', 587)
server.ehlo()
server.starttls()

user = str(input("\033[1;34mSeu Email > \033[0;0m"))
senha = str(input("Sua Senha > \033[0;0m"))
para = str(input("Remetente > \033[0;0m"))
numero = int(input("\033[33mTotal de E-mails > \033[0;0m"))
msg = str(input("\033[36mInsira sua Mensagem > \033[0;0m"))

try:
	server.login(user, senha)
	print("\033[32mLogando\033[0;0m")
except:
	print("\033[31mEmail ou Senha errados || Permissao Negada\033[0;0m")

x = 0
while(x<numero):
	server.sendmail(user, para, msg)
	x=x+1
	print("\033[36mEnviado", x, "Email\033[0;0m")

#coding: UTF-8
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

user = str(input("\033[1;34mSeu Email > "))
senha = str(input("Sua Senha > "))
para = str(input("Remetente > "))
numero = int(input("\033[33mTotal de E-mails > "))
msg = str(input("\033[36mInsira sua Mensagem > "))

try:
	server.login(user, senha)
	print("\033[32mLogando")
except:
	print("\033[31mEmail ou Senha errados || Permissao Negada")

x = 0
while(x<numero):
	server.sendmail(user, para, msg)
	x=x+1
	print("\033[36mEnviado", x, "Email")
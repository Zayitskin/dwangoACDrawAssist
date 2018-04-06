import socket, time, sys

def post(socket, message):
    s.send(bytes(message + "\r\n", "UTF-8"))

#If you pass in an argument, it will use it as the file path.
#Otherwise, it will ask for a file path.
#Paths are relative to where this file is located.
if(len(sys.argv) == 1):
    file = input("path to file: ")
else:
    file = sys.argv[1]
f = open(file)

host = 'irc.chat.twitch.tv'
port = 6667
#Put in the twitch username of the account that will be sending the messages
user = ''
#Put the oAuth for the account above
oauth = ''

#These are dwangoAC's channel ID and pbn's UUID
#You could change them. But why?
channel = '70067886'
room = '334d02cb-f694-43b4-8ef5-7a9845fa931d'

s = socket.socket()
s.connect((host, port))
post(s, "PASS " + oauth)
post(s, "NICK " + user)
post(s, "JOIN #chatrooms:" + channel + ":" + room)

#If there are any connection errors, this will print them out.
#Otherwise, you will receive the generic Twitch IRC connection message.
#If there is an error, it will probably crash, seeing as I have
#done zero error handling.
print(s.recv(4096))

#NOTE: Twitch will send a message about every five minutes.
#I am not doing anything to handle this, so if it does happen
#Twitch will sever the socket, so try to keep it below 150 lines.
for line in f.readlines():
    post(s, "PRIVMSG #chatrooms:" + channel + ":" + room + " :" + line)
    time.sleep(2)

s.shutdown(socket.SHUT_RDWR)
f.close()
print("Done.")

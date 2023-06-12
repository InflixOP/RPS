import sys
import random
player=input("𝗘𝗡𝗧𝗘𝗥 𝗣𝗟𝗔𝗬𝗘𝗥 𝗡𝗔𝗠𝗘:")
b,u=0,0
for i in range(1,6):
    user=input("𝐄𝐧𝐭𝐞𝐫 𝐲𝐨𝐮𝐫 𝐜𝐡𝐨𝐢𝐜𝐞 𝐨𝐮𝐭 𝐨𝐟 𝐫𝐨𝐜𝐤,𝐩𝐚𝐩𝐞𝐫,𝐬𝐜𝐢𝐬𝐬𝐨𝐫:")
    user=user.lower()
    if user!='rock' and user!='paper' and user!='scissor':
        print("𝐘𝐨𝐮 𝐡𝐚𝐯𝐞 𝐩𝐥𝐚𝐲𝐞𝐝 𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐦𝐨𝐯𝐞")
    else:
       user=user.lower()
       choice=['rock','paper','scissor']
       bot=random.choice(choice)
       print("𝐘𝐨𝐮 𝐜𝐡𝐨𝐬𝐞:",user)
       print("𝐁𝐨𝐭 𝐜𝐡𝐨𝐨𝐬𝐞𝐬:",bot)
       if user==bot:
          print(i,"round tied")
       elif user=='rock' and bot=='scissor':
          print(player,"wins",i,"round because Rock crushes scissor")
          u+=1
       elif user == 'rock' and bot == 'paper':
          print("Bot wins",i,"round because paper cover rock")
          b+=1
       elif user == 'scissor' and bot == 'paper':
          u+=1
          print(player,"wins",i,"round because scissor cuts paper")
       elif user == 'scissor' and bot == 'rock':
          b+=1
          print("Bot wins",i,"round because rock cruses scissor")
       elif user == 'paper' and bot == 'scissor':
          b+=1
          print("Bot wins", i, "round because scissor cuts paper")
       elif user == 'paper' and bot == 'rock':
          u+=1
          print(player," wins", i, "round because paper cover rock")
       if b>=3:
          print("𝐁𝐎𝐓 𝐖𝐈𝐍𝐒 𝐓𝐇𝐈𝐒 𝐌𝐀𝐓𝐂𝐇")
          print("𝐒𝐂𝐎𝐑𝐄",b,'-',u)
          sys.exit()
       elif u>=3:
          print(player,"𝐖𝐈𝐍𝐒 𝐓𝐇𝐈𝐒 𝐌𝐀𝐓𝐂𝐇")
          print("𝐒𝐂𝐎𝐑𝐄", u,'-',b)
          sys.exit()
if b>u:
    print("𝐁𝐎𝐓 𝐖𝐈𝐍𝐒 𝐓𝐇𝐈𝐒 𝐌𝐀𝐓𝐂𝐇")
    print("𝐒𝐂𝐎𝐑𝐄",b,'-',u)
    sys.exit()
elif u>b:
    print(player,"𝐖𝐈𝐍𝐒 𝐓𝐇𝐈𝐒 𝐌𝐀𝐓𝐂𝐇")
    print("𝐒𝐂𝐎𝐑𝐄", u, '-', b)
    sys.exit()
elif u==b:
    print("𝐌𝐀𝐓𝐂𝐇 𝐓𝐈𝐄𝐃")
    print("𝐒𝐂𝐎𝐑𝐄", u, '-', b)
    sys.exit()
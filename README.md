# CWF-Fall'20
**Project :** Joeyy - A Discord Bot written in Python. *(Will be deployed on Heroku)*<br>
Joeyy is a Discord bot which gives sarcastic replies to a user's messages in a server. It can also play music & do general stuff to manage a server.

### Project Analogy 📝 
**- Discord Bot :** The main folder which contains all the code which was used to build & run the bot.<br>
*inside Discord Bot folder :-*<br>
- Bot.py - The prime python script which acts a hub of all other command cogs.<br>
- Cogs - Contains the code for all the different stuff which the bot can do.<br>
- Others - Files which are used for deployment on Heroku.<br>

**- Tester:** contains trash prototype code for testing purposes.<br>
**- Lavalink, venv etc:** These are all the subsidary stuff of the project.

### Bot Commands 🤖 
*Command prefix : '!'*
<br>_____________________
<br>
- **!Hey :** where 'Hey/hey' prompts the bot to await a text message from a channel member & replies upon reading it.<br>
*Ex :- Like when you say !hey followed by some text...*
 ![alt text](https://github.com/Dhruv-VINT/CWF-Fall20/blob/main/Images/rt.jpg?raw=true)<br>
 __________________________________________________________________________________________<br>
*Ex :- It can read specific words in a message & throw in a bit of joke...*
  ![alt text](https://github.com/Dhruv-VINT/CWF-Fall20/blob/main/Images/op.jpg?raw=true)

- **!clear :** clears the last n messages (n = 1,2,3,4,5.....)
- **!kick :** kicks a member from the channel.
- **!ban :** manually bans a member from the channel.
- **!unban :** manually unbans the banned member.

### Terminal Insights 🔍
1. When the Bot is **online/ready** on the Discord server :-<br>
  ![alt text](https://github.com/Dhruv-VINT/CWF-Fall20/blob/main/Images/ty.jpg?raw=true)<br>
  
2. When a user **joins/leaves** the server :-<br>
  ![alt text](https://github.com/Dhruv-VINT/CWF-Fall20/blob/main/Images/er.jpg?raw=true)<br>


### Under Development ⌨️ 
*Work in progress !* <br>
**Music bot** : Lavalink (Wavelink) is used to provide music playing commands. The code is somewhat finished, the process of intigrating it with the server & the main bot.py file is pending. <br>
**Snack-time reminder** : A Timely reminder whivh remind the 'active' server members to drink water or eat something. A little bit of tweaking with it's code is still needed for the function to run seamlessly.

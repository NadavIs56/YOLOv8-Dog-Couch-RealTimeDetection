#  <p align ="center" height="40px" width="40px"> Dog On Couch Detector 🐶🛋️ </p>

#  <p align ="center" height="40px" width="40px"> AI-powered pet detection for furniture protection 🤖 </p>



### <p align ="center"> Implemented using: </p>
<p align ="center">
<a href="https://www.python.org/" target="_blank" rel="noreferrer">   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png" width="64" height="64" /></a>
<a href="https://docs.ultralytics.com/" target="_blank" rel="noreferrer">   <img src="https://ultralytics.com/static/brand/yolov8-r1-1.svg" width="128" height="64" /></a>  
<a href="https://opencv.org/" target="_blank" rel="noreferrer">   <img src="https://opencv.org/wp-content/uploads/2022/05/logo.png" width="64" height="64" /></a> 
<a href="https://web.telegram.org/k/" target="_blank" rel="noreferrer">   <img src="https://www.pngkit.com/png/detail/897-8972864_telegram-telegram-logo-png.png" width="64" height="64" /></a>
</p>

<br>

### <p align ="center"> Do remember to star ⭐ the repository if you like what you see!</p>

<br>

##     <p align = "left"> Introduction 📚 </p>

Like many pet owners, I've faced a common problem:<br>every time I leave the house, my dogs jump on the sofa and leave behind a mess of fur 🐾🛋️. <br>I've tried countless methods to prevent this but to no avail.<br><br>
Motivated to find a solution, I decided to leverage the power of technology to create a tool to manage this issue. This led to the development of a system that combines computer vision, machine learning, object detection, and real-time notifications to my personal Telegram account. The application alerts 🚨 whenever it detects one of the dogs on the sofa, and it even sends an immediate update to my phone, complete with an image of the mischievous dog, enabling me to take immediate action, no matter where I am. This use of technology not only ensures my furniture's cleanliness but also allows me to remotely monitor my pets' behavior.

<br>

##     <p align = "left"> Implementation 💻 </p>
The system utilizes the YOLOv8 pre-trained model from Ultralytics. <br>I made several modifications, computations, and conditions to tailor the model for this specific application.

<br>

##     <p align = "left"> Features ⭐ </p>
 -  Real-time detection of a specific event: dog climbing on a couch.
 -  Utilizes the powerful YOLOv8 model for object detection.
 -  Triggers real-time alerts when the event is detected.
 -  Sends real-time alerts with photos to a specified Telegram chat.

<br>

##     <p align = "left"> Installation and Usage 🛠️ </p>
1. Clone this repository to your local machine.
2. Install the required packages using 'pip install -r requirements.txt'
3. Position your computer in front of the couch. It's preferable if the computer's camera is parallel to the couch.
4. Set up a Telegram bot
Update the telegram_key and chat_id variables in the code with your bot's API key and your chat ID.
5. Run the script 'python detector.py'
6. The tool will then use your computer's camera to monitor the couch.
7. The tool has been programmed to specifically detect dogs, cats, sofas, and beds while ignoring other objects.
<br>

##     <p align = "left"> Setting Up the Telegram Bot 📲 </p>
1. Message @BotFather on Telegram using the Telegram app.
2. Type /newbot to create a new bot. Follow the instructions and set a name and username for your bot.
3. After successfully creating the bot, BotFather will give you a token. This is your 'telegram_key' (keep it secret).
4. Message @userinfobot on Telegram using the Telegram app.
5. Press 'start'.
6. The bot will reply to you with some personal information. The 'Id' is your 'chat_id' (keep it secret).

<br>

##     <p align = "left"> Conclusion and Request for Feedback 📝 </p>
I hope that this tool will solve my problem. But even if it doesn't fully work as expected, I've thoroughly enjoyed the learning journey and the deep dive into the world of computer vision and object detection.<br><br>
This is my first project using the YOLO model, so I welcome any feedback regarding the implementation, the code quality, and any potential optimizations that could ensure efficient runtimes even on relatively weak hardware. Your time and insights are greatly appreciated. <br>Thank you! 🙏

<br>

##     <p align = "left"> Future Updates 🔮 </p>
Stay tuned for future updates, enhancements, and the results of this project. I'll be posting regular updates as we progress. <br>Thanks for stopping by! 👋

<br>

##     <p align = "left"> Acknowledgements 🙏 </p>
I'd like to express my gratitude to the creators of the YOLOv8 model, as their work served as the foundation for this project.

<br>

### <p align ="center"> Do remember to star ⭐ the repository if you like what you see!</p>

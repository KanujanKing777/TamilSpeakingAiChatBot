from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import random
app = Flask(__name__, static_folder= "templates")
CORS(app)

@app.route("/signin")
def signin():
    pass

@app.route("/webhook", methods=["GET","POST"])
def webhook():
    try:
            data = request.get_json()
            user_message = data["message"]
            user_message = user_message + ' '
            user_message.lower()
            # Debugging: Print received data
            hi_list = ['hi ', 'hello ', 'vanakkam ', 'good morning ', 'good evening ', 'good afternoon ']
            hi_list_gf = ['Hi', 'Hello', 'Vanakkam']
            caller_list = ['da', 'dear', 'darling']
            how_list = ['how are you ', 'epdi irukureenga ', 'vaazhkai epdi pothu ']
            how_list_gf = ['I am fine bcz of u', 'I am in luv with u', 'I will kiss you']
            bye_list = ['bye di ', 'Its time to say bye ', 'bye']
            bye_list_gf = ['bye da', 'bye da my luv']
            casual = ['love u darling', 'luv u forever', 'u r my favourite',
                      'I luv u for infinity']
            nouse = ['I ', 'am ', 'is ', 'was ', 'were ', 'you ', 'u ']

            nuts = ['oh ', 'ohh ', 'mm ', 'mmm ', 'ah ', 'ahh ']
            
            if any(word in user_message for word in hi_list):
                bot_reply = random.choice(hi_list_gf) + " " + random.choice(caller_list)
            elif any(word in user_message for word in how_list):
                bot_reply = random.choice(how_list_gf) 
            elif any(word in user_message for word in bye_list):
                bot_reply = random.choice(bye_list_gf) 
            elif any(word in user_message for word in nuts):
                bot_reply = random.choice(nuts) 
            else:
                bot_reply = random.choice(casual)

            # Debugging: Print bot's reply
            print(f"Bot's reply: {bot_reply}")

            # Extract the bot's reply
            return jsonify({"message": bot_reply})
        
        # Handle GET requests if needed
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return jsonify({"error": "Internal Server Error"})

@app.route("/home", methods=["GET","POST"])
def home():
    return render_template('chatui.html')

@app.route("/", methods=["GET","POST"])
def fun():
    return render_template('chatui.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

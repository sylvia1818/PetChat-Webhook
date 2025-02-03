from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()

    # Extract pet details from Dialogflow parameters
    parameters = req['queryResult']['parameters']
    pet_name = parameters.get('pet_name', 'your pet')
    pet_type = parameters.get('pet_type', 'pet')
    pet_age = parameters.get('pet_age', 'unknown age')
    pet_energy = parameters.get('pet_energy', 'unknown energy level')

    # Create dynamic response
    response_text = f"🐾 Awesome! I’ve saved {pet_name}’s profile. Now I’ll always keep their unique needs in mind when giving advice! 💡 Since this is your first pet profile, feel free to add more pets anytime—just say ‘Remember another pet’s details,’ and we’ll set them up too! ✨ I’m excited to get to know {pet_name} (and any other furry, feathered, or scaly friends you have)! Just ask me anything whenever you need pet advice. 🐾💛"

    return jsonify({"fulfillmentText": response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

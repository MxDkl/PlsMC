from flask import Flask, request, jsonify, send_file

from datapack import Datapack
from command import Command
from moderation import Moderation
from translation import Translation
from worldedit import WorldEdit


# Flask api routes
#==================================================================================================
app = Flask(__name__)


# Generates a minecraft command
@app.route('/api/plsmc/command/minecraft', methods=['GET','POST'])
def command():
    try:
        prompt = request.get_json()['prompt']
    except:
        return jsonify({"error": "No prompt field provided."})
    
    cmd = Command(prompt)
    return jsonify({"command": cmd.create()})


# Generates a minecraft datapack.
@app.route('/api/plsmc/datapack', methods=['GET','POST'])
def datapack():
    try:
        prompt = request.get_json()['prompt']
    except:
        return jsonify({"error": "No prompt field provided."})
    
    dp = Datapack(prompt)
    dp.create()
    path = dp.saveToFile()
    filename = path.split('/')[-1]
    return send_file(path, as_attachment=True)


# Moderates minecraft chat message
@app.route('/api/plsmc/chat/moderation', methods=['GET','POST'])
def moderation():
    try:
        message = request.get_json()['message']
    except:
        return jsonify({"error": "No message field provided."})
    
    mod = Moderation(message)
    return jsonify(mod.getModeration())


# Translates minecraft chat message
@app.route('/api/plsmc/chat/translation', methods=['GET','POST'])
def translate():
    try:
        message = request.get_json()['message']
        to_lang = request.get_json()['to']
        from_lang = request.get_json()['from']
    except:
        return jsonify({"error": "Incorrect fields provided. Please provide message, to, and from fields."})
    
    t = Translation(message, (to_lang, from_lang))
    return jsonify({"translation": t.getTranslation()})


# WorldEdit Command Generator
@app.route('/api/plsmc/command/worldedit', methods=['GET','POST'])
def worldedit():
    try:
        prompt = request.get_json()['prompt']
    except:
        return jsonify({"error": "No prompt field provided."})
    
    we = WorldEdit(prompt)
    return jsonify({"command": we.create()})
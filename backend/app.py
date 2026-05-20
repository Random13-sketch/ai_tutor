from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app) # This allows the HTML file to talk to this Python server

def get_db_connection():
    conn = sqlite3.connect('tutor.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/ask', methods=['POST'])
def ask_tutor():
    data = request.json
    user_id = data.get('user_id', 1)
    question = data.get('question')

    if not question:
        return jsonify({"error": "No question provided"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Save student's question to SQL
    cursor.execute("INSERT INTO ChatHistory (user_id, role, content) VALUES (?, 'student', ?)", (user_id, question))
    
    # 2. Simulated AI Logic (You can integrate a real LLM API here later)
    ai_answer = f"I see you're asking about '{question}'. As your AI Tutor, I recommend studying the core concepts of this topic first!"

    # 3. Save AI's answer to SQL
    cursor.execute("INSERT INTO ChatHistory (user_id, role, content) VALUES (?, 'tutor', ?)", (user_id, ai_answer))
    
    conn.commit()
    conn.close()

    return jsonify({"answer": ai_answer})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
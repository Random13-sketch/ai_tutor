// Allow pressing "Enter" to send
document.getElementById("user-input").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
});

async function sendMessage() {
    const inputField = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');
    const message = inputField.value.trim();

    if (!message) return; // Do nothing if input is empty

    // 1. Show User's Message
    chatBox.innerHTML += `
        <div class="message user-msg">
            <div class="bubble">${message}</div>
        </div>`;
    inputField.value = ''; // Clear input
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom

    // 2. Show "Typing..." indicator
    const typingIndicatorId = 'typing-' + Date.now();
    chatBox.innerHTML += `<div id="${typingIndicatorId}" class="typing">AI is thinking...</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        // 3. Send Request to Python Backend
        // ⚠️ CRITICAL: If you and Khadija are on DIFFERENT computers, 127.0.0.1 will NOT work here.
        // It must be your actual IP address or a hosted URL.
        const response = await fetch('http://127.0.0.1:5000/api/ask', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question: message, user_id: 1 })
        });

        const data = await response.json();
        
        // Remove typing indicator
        document.getElementById(typingIndicatorId).remove();

        // 4. Show Bot's Response
        if (data.answer) {
            chatBox.innerHTML += `
                <div class="message bot-msg">
                    <div class="bubble">${data.answer}</div>
                </div>`;
        } else {
            chatBox.innerHTML += `
                <div class="message bot-msg">
                    <div class="bubble" style="background: #ffcccc;">Error: ${data.error || "Unknown error"}</div>
                </div>`;
        }

    } catch (error) {
        // Remove typing indicator on error
        document.getElementById(typingIndicatorId).remove();
        
        chatBox.innerHTML += `
            <div class="message bot-msg">
                <div class="bubble" style="background: #ffcccc; color: #a00;">
                    Connection Error: Make sure the Python server is running!
                </div>
            </div>`;
        console.error("Fetch error:", error);
    }

    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom again
}
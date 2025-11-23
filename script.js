function showMessage() {
    const messages = [
        "Hello from our Python server! 🐍",
        "Static files are working! ✅",
        "JavaScript is executing! 🚀",
        "Server is responding! 👍",
        "All systems go! 🌟"
    ];
    
    const randomMessage = messages[Math.floor(Math.random() * messages.length)];
    document.getElementById('demo-message').textContent = randomMessage;
}

// Display current time
function updateTime() {
    const now = new Date();
    document.getElementById('current-time').textContent = now.toLocaleString();
}

// Update time every second
setInterval(updateTime, 1000);

console.log("JavaScript loaded successfully from static file!");
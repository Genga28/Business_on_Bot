const chatbot = document.getElementById("chatbot");
const messageInput = document.getElementById("message");

// Greeting message
displayMessage("Hello! I am the Calculator Chatbot. Can you provide the operations for me to calculate?", false);

function sendMessage() {
	const message = messageInput.value;
	const response = calculate(message);
	displayMessage(message, true);
	displayMessage(response, false);
	messageInput.value = "";
}

function displayMessage(message, isUser) {
	const div = document.createElement("div");
	if (isUser) {
		div.innerHTML = `<strong>You:</strong> ${message}`;
	} else {
		div.innerHTML = `<strong>Calculator Chatbot:</strong> ${message}`;
	}
	chatbot.appendChild(div);
	chatbot.scrollTop = chatbot.scrollHeight;
}

function calculate(message) {
	const operators = /[+\-*/]/;
	const tokens = message.split(operators);
	const operator = message.match(operators)[0];
	const num1 = parseFloat(tokens[0]);
	const num2 = parseFloat(tokens[1]);
	let result;
	switch (operator) {
		case "+":
			result = num1 + num2;
			break;
		case "-":
			result = num1 - num2;
			break;
		case "*":
			result = num1 * num2;
			break;
		case "/":
			result = num1 / num2;
			break;
		default:
			result = "I don't understand that. Please try again.";
	}
	return result;
}
async function send() {
    const msg = document.getElementById("message").value;

    const res = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: msg})
    });

    const data = await res.json();
    alert("IA: " + data.reply);
}

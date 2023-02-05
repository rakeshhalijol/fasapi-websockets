let ws = new WebSocket("ws://localhost:8000/ws");
ws.addEventListener("open",(e)=>{
    console.log("connected...")
});

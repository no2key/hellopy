window.onload = function(){
    var url = 'ws://localhost:9999/now';
    var socket = new WebSocket(url);

    socket.onopen = function(event){
        setInterval(send, 1000);
    }

    function send(){
        socket.send('hello');
    }

    socket.onclose = function(event){

    }

    socket.onerror = function(event){
        alert('error');
    }

    socket.onmessage = function(event){
        var data = event.data;
        data = JSON.parse(data);
        last.innerHTML = data['CNY']['sell'];
        buy.innerHTML = data['CNY']['buy'];
        sell.innerHTML = data['CNY']['sell'];
        h24.innerHTML = data['CNY']['24h'];
    }
}
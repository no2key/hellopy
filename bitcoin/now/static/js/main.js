window.onload = function(){

    setInterval(getBitcoinNow, 2500);

    function getBitcoinNow(){
        var url = "/now";
        var request = new XMLHttpRequest();

        request.open("Get",url);
        request.onload = function()
        {
            if(request.status = 200)
            {
                var data = request.responseText;
                data = JSON.parse(data);
                last.innerHTML = data['CNY']['sell'];
                buy.innerHTML = data['CNY']['buy'];
                sell.innerHTML = data['CNY']['sell'];
                h24.innerHTML = data['CNY']['24h'];
            }
        };
        request.send(null);
    }

}


var lineChartData = {
    labels : [],
    datasets : [
        {
			fillColor : "rgba(151,187,205,0.5)",
			strokeColor : "rgba(151,187,205,1)",
			pointColor : "rgba(151,187,205,1)",
			pointStrokeColor : "#fff",
			data : []
		}
    ]
}

var xmlhttp = new XMLHttpRequest();
function chart_now(){
    xmlhttp.open("GET", "http://localhost:8088/chartapi", true);
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4) {
            var result = JSON.parse(xmlhttp.responseText)['values'];
            var x = [];
            var y = [];
            for(var i=result.length-300; i<result.length; i++){
                x[i] = result[i]['x'];
                y[i] = result[i]['y'];
            }
            lineChartData.labels = x;
            lineChartData.datasets[0]['data'] = y;
            new Chart(document.getElementById("myChart").getContext("2d")).Line(lineChartData);
        }
    }
    xmlhttp.send();
}

//chart_now()
setInterval(chart_now, 2000);



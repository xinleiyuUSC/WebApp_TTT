
function myFunction() {
    
    var height = document.getElementById('input1').value;
    var time = document.getElementById('input2').value;
    var in_height = document.getElementById('input3').value;
    var in_time = document.getElementById('input4').value;
 
        const Http = new XMLHttpRequest();
        const url='http://127.0.0.1:5000/set?height='+height+'&time='+time+'&inHeight='+in_height+'&inTime='+in_time;
        Http.open("GET", url);
        Http.send();
    
        Http.onreadystatechange = (e) => {
        alert("Your input is: " + "\nheight: " + height + "\ntime: " + time + "\nincrement_height: " + in_height + "\nincrement_time: " + in_time);
    }
}

function getStart(){
    const Http = new XMLHttpRequest();
    const url='http://127.0.0.1:5000/start';
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
    alert("Your Program starts")
}
}

function stop(){
    const Http = new XMLHttpRequest();
    const url='http://127.0.0.1:5000/stop';
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
    alert("Your Program stopped")
}
}

function get_status(){
    const Http = new XMLHttpRequest();
    const url='http://127.0.0.1:5000/status';
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
    var status = JSON.parse(Http.responseText)
    alert("Your Program status: " + status)
    
}}


window.onload = function() {
    window.alert("ご登録ありがとうございます。")
}

window.onload = function() {
    console.log("Hello, world!");
}

/* アクセスした日時の表示 */
var now = new Date();
var target = document.getElementById("DateTimeDisp");

var Year = now.getFullYear();
var Month = now.getMonth()+1;
var Date = now.getDate();
var Hour = now.getHours();
var Min = now.getMinutes();
var Sec = now.getSeconds();

console.log(Year);

target.innerHTML = Year + "/" + Month + "/" + Date + " " + Hour + ":" + Min + ":" + Sec;


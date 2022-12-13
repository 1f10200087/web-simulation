window.onload = function alert() {
    window.alert("ご登録ありがとうございます。")
}

function pay_later() {
    window.alert("1週間以内にお振り込みがない場合は、ご自宅かお勤め先へご連絡をさせて頂く事となります。トラブルを回避する為、今すぐにお支払い下さい。")
}

// window.onload = function test() {

//     var countdown = null;
//     var remainTime = 604800000; //（ミリ秒で返ってくる)

//     function event() {
//         remainTime--;

//         console.log(remainTime);

//         // 日・時・分・秒を取得
//         var difDay  = Math.floor(remainTime / 1000 / 60 / 60 / 24)
//         var difHour = Math.floor(remainTime / 1000 / 60 / 60 ) % 24
//         var difMin  = Math.floor(remainTime / 1000 / 60) % 60
//         var difSec  = Math.floor(remainTime / 1000) % 60

//         //残りの日時を上書き
//         document.getElementById("countdown-day").textContent  = difDay
//         document.getElementById("countdown-hour").textContent = difHour
//         document.getElementById("countdown-min").textContent  = difMin
//         document.getElementById("countdown-sec").textContent  = difSec

//         //指定の日時になればカウントを止める
//         if(remainTime < 0) clearInterval(countdown)
//     }
//     countdown = setInterval(event, 1000); //1秒間に1度処理
// }

const day = document.getElementById("countdown-day"); // 日のHTMLタグを取得
const hour = document.getElementById("countdown-hour"); // 時間のHTMLタグを取得
const min = document.getElementById("countdown-min"); // 分のHTMLタグを取得
const sec = document.getElementById("countdown-sec"); // 秒のHTMLタグを取得
var countDownDate = new Date().getTime() + 604800000; // 今の時刻から1週間後の時間を取得
console.log(countDownDate);
var x = setInterval(function() {
    var now = new Date().getTime(); // 今の時刻取得
    var diff = countDownDate - now; // 差分

    var Day  = Math.floor(diff / 1000 / 60 / 60 / 24)
    var Hour = Math.floor(diff / 1000 / 60 / 60 ) % 24
    var Min = Math.floor(diff / 1000 / 60) % 60; // 分に直す
    var Sec = Math.floor(diff / 1000) % 60; // 秒に直す

    day.innerHTML = Day < 10 ? '0' + Day : Day;
    hour.innerHTML = Hour < 10 ? '0' + Hour : Hour;
    min.innerHTML = Min < 10 ? '0' + Min : Min;
    sec.innerHTML = Sec < 10 ? '0' + Sec : Sec;
})

/* アクセスした日時の表示 */
var now = new Date();
var target = document.getElementById("DateTimeDisp");

var Year = now.getFullYear();
var Month = now.getMonth()+1;
var Today_Date = now.getDate();
var Hour = now.getHours();
var Min = now.getMinutes();
var Sec = now.getSeconds();

console.log(Year);

target.innerHTML = Year + "/" + Month + "/" + Today_Date + " " + Hour + ":" + Min + ":" + Sec;


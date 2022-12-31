function answer_check(ques, event, no) {
var resp = event.target.value;
var correct_id = 'correct-' + no;
var wrong_id = 'wrong-' + no;
resutliscorrect = document.getElementById(correct_id);
resultiswrong = document.getElementById(wrong_id);
if (resp == ques) {
    resutliscorrect.style.display='block';
    resultiswrong.style.display='none';   
}
else {
    resutliscorrect.style.display='none';
    resultiswrong.style.display='block';   
}
}
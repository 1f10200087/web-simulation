function answer_check(ques, event) {
    var resp = event.target.value;
    
    if (ques == resp) {
        alert("correct!");
    }
    else {
        alert("wrong...");
    }
}
function identity_check() {
    var id_value = $(this).prop('id');
    var title_value = $('#'+id_value).attr('title');
    window.alert(title_value);
}

function OnLinkClick(ele) {
    let eles = ['header', 'icon', 'name', 'id', 'contents', 'address', 'birthday']

    for (let e of eles) {
        console.log(ele)
        let output = document.getElementById("output-"+e);
        if (ele == e) {
            output.style.display = "block";
        }
        else {
            output.style.display = "none";
        }
    }
    
    return false;
}
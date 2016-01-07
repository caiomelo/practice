function upDate(previewPic){
    var element = document.getElementById('image');
    var url = "url("+ previewPic.src + ")";
    element.style.backgroundImage = url;
    element.style.backgroundColor = "#CCEECC";
    element.innerHTML = previewPic.alt;
}

function unDo(){
    var element = document.getElementById('image');
    element.style.backgroundImage = "url('')";
    element.style.backgroundColor = "#8e68ff";
    element.innerHTML = "Hover over an image below to display here.";

}
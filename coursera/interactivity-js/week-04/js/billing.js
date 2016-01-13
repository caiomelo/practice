function billingFunction(element) {
    var billingName = document.getElementById("billingName");
    var billingZip = document.getElementById("billingZip");

    if(element.checked){
        billingName.value = document.getElementById("shippingName").value;
        billingZip.value = document.getElementById("shippingZip").value;

    } else {
        billingName.value = "";
        billingZip.value = "";
    }
}
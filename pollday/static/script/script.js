function toopen(button){
    var div = button.parentElement;
    var p_display = div.children[1]
    console.log(getComputedStyle(p_display).display)
    if (getComputedStyle(p_display).display == 'none'){
        p_display.style.display = 'block'
        button.value = '«'
    }else{
        p_display.style.display = 'none'
        button.value = '»'
    }
}
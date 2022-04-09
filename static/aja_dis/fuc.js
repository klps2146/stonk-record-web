open_click_times=0;
function click_change_tmg(){
    if (open_click_times==0){
        $(".d1").css("display", "");
        open_click_times++;
    }
    else if (open_click_times==1){
        $(".d1").css("display", "");
        $(".d2").css("display", "");
        document.getElementById("cfn").innerHTML="收起";
        open_click_times++;
    }
    else if (open_click_times==2){
        $(".d1").css("display", "none");
        $(".d2").css("display", "none");
        document.getElementById("cfn").innerHTML="展開";
        open_click_times=0;
    }
}

$(function() {
    $('#gotop').click(function(){
        $('html,body').animate({scrollTop: 0}, 300);
        return false;
    });
});

// React Start


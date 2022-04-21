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
    $("#creater").toggle(300);
    $("#creater_osd").toggle(300);
    $("#creater_background").toggle(0);
    $('#gotop').click(function(){
        $('html,body').animate({scrollTop: 0}, 300);
        return false;
    });
    $('#add_data_btn').click(function(){
        $("#creater").toggle(300);
        $("#creater_osd").toggle(300);
        $("#creater_background").toggle(30);
    });
    $(document).click(function(e){
        if (e.target.id=="creater_background"){
            $("#creater").toggle(300);
            $("#creater_osd").toggle(300);
            $("#creater_background").toggle(30);
        }
    });
});




$("#fcv").blur(function(){
    if(document.getElementById("fcv").options[0].selected){
        $(".res1").css("display", "block");
        $(".res2").css("display", "none");
    }
    else{
        $(".res1").css("display", "none");
        $(".res2").css("display", "block");
    }
    //     $(".cg1").click(function(){
    //     $(".res1").css("display", "block");
    //     $(".res2").css("display", "none");
    //         })
    //     $(".cg2").click(function(){
    //     $(".res1").css("display", "none");
    //     $(".res2").css("display", "block");
    // })
})
window.onload=function(){
    var Today=new Date();
    date=Today.getFullYear()+"/"+(Today.getMonth()+1)+"/"+Today.getDate();
    console.log(date);
    document.getElementById("date").value=date;
    document.getElementById("date1").value=date;
    document.getElementById("year").value=Today.getFullYear();
    document.getElementById("year1").value=Today.getFullYear();
}


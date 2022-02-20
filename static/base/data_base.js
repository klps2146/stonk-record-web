window.onload=function(){ 
    var Today=new Date();
    date=Today.getFullYear()+"/"+(Today.getMonth()+1)+"/"+Today.getDate();
    document.getElementById("date").value=date;
    document.getElementById("year").value=Today.getFullYear();
    // if (Today.getMonth()+1==1||Today.getMonth()+1==2||Today.getMonth()+1==3){
    //     document.getElementById("Q1").setAttribute("selected","");
    // }
    // if (Today.getMonth()+1==4||Today.getMonth()+1==5||Today.getMonth()+1==6){
    //     document.getElementById("Q2").setAttribute("selected","");
    // }
    // if (Today.getMonth()+1==7||Today.getMonth()+1==8||Today.getMonth()+1==9){
    //     document.getElementById("Q3").setAttribute("selected","");
    // }
    // if (Today.getMonth()+1==10||Today.getMonth()+1==11||Today.getMonth()+1==12){
    //     document.getElementById("Q4").setAttribute("selected","");
    // }   
}
function logout(){
  Swal.fire({
    title: '登出?',
    text: "需要重新登入",
    icon: 'question',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: '登出',
    cancelButtonText: "取消",
  }).then((result) => {
    if (result.isConfirmed) {
      location.href="/signout";
    }
  })
}
$(document).ready(function(){
    // $("#cli").hide();
    $(".onmouse_c0").mouseover(function(){
      $(".onmouse_c0").css("color", "rgb(214, 143, 10)")
    })
    $(".onmouse_c0").mouseout(function(){
      $(".onmouse_c0").css("color", "white")
    })
    $(".onmouse_c1").mouseover(function(){
      $(".onmouse_c1").css("color", "rgb(214, 143, 10)")
    })
    $(".onmouse_c1").mouseout(function(){
      $(".onmouse_c1").css("color", "white")
    })
    $(".onmouse_c2").mouseover(function(){
      $(".onmouse_c2").css("color", "rgb(214, 143, 10)")
    })
    $(".onmouse_c2").mouseout(function(){
      $(".onmouse_c2").css("color", "white")
    })
    $(".onmouse_c3").mouseover(function(){
      $(".onmouse_c3").css("color", "rgb(214, 143, 10)")
    })
    $(".onmouse_c3").mouseout(function(){
      $(".onmouse_c3").css("color", "white")
    })
    $(".onmouse_c4").mouseover(function(){
      $(".onmouse_c4").css("color", "rgb(214, 143, 10)")
    })
    $(".onmouse_c4").mouseout(function(){
      $(".onmouse_c4").css("color", "white")
    })
    $(".onmouse_c5").mouseover(function(){
      $(".onmouse_c5").css("color", "gray")
    })
    $(".onmouse_c5").mouseout(function(){
      $(".onmouse_c5").css("color", "white")
    })
    $(".onmouse_c5").mouseover(function(){
      $(".onmouse_c5").css("color", "gray")
    })
    $(".onmouse_c5").mouseout(function(){
      $(".onmouse_c5").css("color", "white")
    })
    $("#more_info").click(function(){
      $("#cli").fadeToggle(150);
    })
  
  }) 

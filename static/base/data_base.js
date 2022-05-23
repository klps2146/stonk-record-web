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
      $(".onmouse_c0").css("color", "#4e4e4e")
    })
    $(".onmouse_c1").mouseover(function(){
      $(".onmouse_c1").css("color", "rgb(214, 143, 10)")
    })
    $(".onmouse_c1").mouseout(function(){
      $(".onmouse_c1").css("color", "#4e4e4e")
    })
    $(".onmouse_c2").mouseover(function(){
      $(".onmouse_c2").css("color", "rgb(214, 143, 10)")
    })
    $(".onmouse_c2").mouseout(function(){
      $(".onmouse_c2").css("color", "#4e4e4e")
    })
    $(".onmouse_c3").mouseover(function(){
      $(".onmouse_c3").css("color", "rgb(214, 143, 10)")
    })
    $(".onmouse_c3").mouseout(function(){
      $(".onmouse_c3").css("color", "#4e4e4e")
    })
    $(".onmouse_c4").mouseover(function(){
      $(".onmouse_c4").css("color", "rgb(214, 143, 10)")
    })
    $(".onmouse_c4").mouseout(function(){
      $(".onmouse_c4").css("color", "#4e4e4e")
    })
    $(".onmouse_c5").mouseover(function(){
      $(".onmouse_c5").css("color", "rgb(214, 143, 10)")
    })
    $(".onmouse_c5").mouseout(function(){
      $(".onmouse_c5").css("color", "#4e4e4e")
    })
    $("#more_info").click(function(){
      if ($("#cli").css("display")!="block"){
        $("#cli").css("display", "block");
      }
      else{
        $("#cli").css("display", "none");
      }
    })
    

    // user panel

    $("#user_name").mouseover(function(){
      $("#user_name").css("background-color", "#eaeaea");
    })
    $("#user_name").mouseout(function(){
      $("#user_name").css("background-color", "white");
    })
    $("#signout").mouseover(function(){
      $("#signout").css("background-color", "#eaeaea");
    })
    $("#signout").mouseout(function(){
      $("#signout").css("background-color", "white");
    })
    $("#password_changing").mouseover(function(){
      $("#password_changing").css("background-color", "#eaeaea");
    })
    $("#password_changing").mouseout(function(){
      $("#password_changing").css("background-color", "white");
    })
    $("#setting").mouseover(function(){
      $("#setting").css("background-color", "#eaeaea");
    })
    $("#setting").mouseout(function(){
      $("#setting").css("background-color", "white");
    })
    $("#feedback").mouseover(function(){
      $("#feedback").css("background-color", "#eaeaea");
    })
    $("#feedback").mouseout(function(){
      $("#feedback").css("background-color", "white");
    })
    $("#source").mouseover(function(){
      $("#source").css("background-color", "#eaeaea");
    })
    $("#source").mouseout(function(){
      $("#source").css("background-color", "white");
    })

    // tell hide or show the user panel
    $(document).mouseup(function(e){
      var _con=$("#personal_panel");
      if (e.target.id=="loginUserBtn"){
        _con.slideToggle(100);
      }
      if (!_con.is(e.target)&&_con.has(e.target).length===0){
        if (e.target.id!="loginUserBtn"){
          _con.slideUp(100);
        }
      }
    })
}) 

function personal_panel(){
  // if ($("#personal_panel").css("display")==""){
  //   $("#personal_panel").css("display", "none");
  // }
  // else{
  //   $("#personal_panel").css("display", "");
  // }
  // $("#personal_panel").slideToggle(100);
}

// $(document).mouseup( function ( e ){
//   var _con = $( ' 目標區域' );    // 設置目標區域
//  if (!_con.is(e.target) && _con.has(e.target). length === 0 ){ // Mark 1 
//    some code...    // 功能代碼
//  }
// });


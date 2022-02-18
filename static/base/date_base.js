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



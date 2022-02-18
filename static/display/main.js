window.onload=function(){ 
    var Today=new Date();
    date=Today.getFullYear()+"/"+(Today.getMonth()+1)+"/"+Today.getDate();
    document.getElementById("date").value=date;
}

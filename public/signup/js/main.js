function chec(){
    let issue=0;
    let user=document.getElementById("usn").value;
    let account=document.getElementById("account").value;
    let pwd=document.getElementById("pwd").value;
    let checkbox=document.querySelector("[name=term]:checked");

    if (checkbox){
        document.getElementById("tfc").style.color="#6E6E6E";
    }
    else{
        issue+=1;
        document.getElementById("tfc").style.color="#FF0000";
    }

    if (user==""){
        document.getElementById("user_cau").style.display="flex";
        issue+=1;
    }
    else{
        document.getElementById("user_cau").style.display="none";
    }
    
    if (account==""){
        document.getElementById("acc_cau").style.display="flex";
        issue+=1;
    }
    else{
        document.getElementById("acc_cau").style.display="none";
    }

    if (pwd=="" || pwd.length<8){
        document.getElementById("pwd_m").style.color="#FF0000";
        issue+=1;
    }
    else{
        document.getElementById("pwd_m").style.color="#FFFFFF";
    }
    if (issue!=0){
        return false;
    }
    else{
        return true;
    }
}
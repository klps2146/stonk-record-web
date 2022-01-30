function checkr(){
    if (document.getElementById("getc").value==""){
        alert("輸入公司名稱(刪除整個公司資料)")
        return false;
    }
    else{
        if (window.confirm("確定要刪除 "+String(document.getElementById("getc").value)+" 所有內容 [[將無法恢復]]")){
            return true;
        }
        else{
            document.getElementById("getc").value="";
            return false;
        }
    }
    return false;
} 

function sub(){
    if (document.getElementById("a").value==""||document.getElementById("b").value==""  ){
        alert("輸入公司名稱或年分(刪除某個年份)")
        return false;
    }
    else{
        if (window.confirm("確定要刪除 "+String(document.getElementById("a").value)+" "+String(document.getElementById("b").value)+"的資料 [[將無法恢復]]")){
            return true;
        }
        else{
            document.getElementById("getc").value="";
            return false;
        }
    }
    return false;
}
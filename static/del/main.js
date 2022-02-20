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
}

function fc() {
    $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
    var form_data = new FormData();
    form_data.append('company', $("#cy").val());
    form_data.append('year', $("#yr").val());
    form_data.append("company_del", "");
    Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
        }).then(function(result){
        if (result.isConfirmed) {
            $.ajax({
                type: "POST",
                url: $SCRIPT_ROOT + "/del",
                data: form_data,
                contentType: false,
                processData: false,
                dataType: "json",
                success: function(data){
                    Swal.fire(
                        'Deleted!',
                        'Your file has been deleted.',
                        'success'
                    )
                },
                error: function(data){
                    Swal.fire(
                        "Error",
                        "Couldn't find the targeted company and the year.",
                        "error"
                    )
                }
            })
        };
    })
}
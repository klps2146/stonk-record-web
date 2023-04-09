window.onload=function(){
    $("#delet_btn").click(function(){
        Swal.fire({
        title: '你確定要刪除帳號嗎？',
        text: "這個動作將無法回復！",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: '刪除',
        cancelButtonText: '取消'
        }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
              title: '你真的要刪除帳號嗎？',
              text: "這個動作真的真的無法回復！",
              icon: 'warning',
              showCancelButton: true,
              confirmButtonColor: '#d33',
              cancelButtonColor: '#3085d6',
              confirmButtonText: '確定刪除',
              cancelButtonText: '取消'
            }).then((result)=>{
                if (result.isConfirmed){
                    Swal.fire({
                        title: '請輸入密碼以確認身分',
                        input: 'password',
                        inputAttributes: {
                        autocapitalize: 'off'
                        },
                        showCancelButton: true,
                        confirmButtonText: '確定',
                        showLoaderOnConfirm: true,
                        preConfirm: (datas)=>{
                            let ppr=new FormData();
                            ppr.append("dpcheck", "key_reuest");
                            $.ajax({
                                type: "POST",
                                url: "/delet_account",
                                data: ppr,
                                contentType: false,
                                processData: false,
                                dataType: "json",
                                success: function(cssde){
                                    let ce=cssde.slice(6, -1);
                                    let publicKey=forge.pki.publicKeyFromPem((ce));
                                    let secretMessage=toString(datas);
                                    let encrypted=publicKey.encrypt(secretMessage, "RSA-OAEP", {
                                        md: forge.md.sha256.create(),
                                        mgf1: forge.mgf1.create()
                                    });
                                    let base64=forge.util.encode64(encrypted);
                                    alert(base64);
                                    let output=new FormData();
                                    output.append("ppas", base64);
                                    output.append("dpcheck", "del_for_ttt_hpcks");
                                    $.ajax({
                                        type: "POST",
                                        url: "/delet_account",
                                        data: output,
                                        contentType: false,
                                        processData: false,
                                        dataType: "json",
                                        success: function(res){
                                            
                                        },
                                    })
                                },
                            })
                        },
                    })

                }
            });
        }
        });
    });
};
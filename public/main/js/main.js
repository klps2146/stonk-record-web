state=1;

function clicke(){
    var checked = document.querySelector('[name=EPS_check]:checked');
    if (checked){
        state+=1;
        document.getElementById("EPS_1").style.display="none";
        document.getElementById("EPS_2").style.display="none";
        document.getElementById("EPS_3").style.display="none";
        document.getElementById("EPS_4").style.display="none";
        document.getElementById("EPS_1").value="";
        document.getElementById("EPS_2").value="";
        document.getElementById("EPS_3").value="";
        document.getElementById("EPS_4").value="";
        document.getElementById("m_1").style.display="inline";
        document.getElementById("m_2").style.display="inline";
        document.getElementById("m_3").style.display="inline";
        document.getElementById("m_4").style.display="inline";
        document.getElementById("m_5").style.display="inline";
        document.getElementById("m_6").style.display="inline";
        document.getElementById("m_7").style.display="inline";
        document.getElementById("m_8").style.display="inline";
        document.getElementById("m_9").style.display="inline";
        document.getElementById("m_10").style.display="inline";
        document.getElementById("m_11").style.display="inline";
        document.getElementById("m_12").style.display="inline";
    }
    else{
        state-=1;
        document.getElementById("EPS_1").style.display="inline";
        document.getElementById("EPS_2").style.display="inline";
        document.getElementById("EPS_3").style.display="inline";
        document.getElementById("EPS_4").style.display="inline";
        document.getElementById("m_1").value="";
        document.getElementById("m_2").value="";
        document.getElementById("m_3").value="";
        document.getElementById("m_4").value="";
        document.getElementById("m_5").value="";
        document.getElementById("m_6").value="";
        document.getElementById("m_7").value="";
        document.getElementById("m_8").value="";
        document.getElementById("m_9").value="";
        document.getElementById("m_10").value="";
        document.getElementById("m_11").value="";
        document.getElementById("m_12").value="";
        document.getElementById("m_1").style.display="none";
        document.getElementById("m_2").style.display="none";
        document.getElementById("m_3").style.display="none";
        document.getElementById("m_4").style.display="none";
        document.getElementById("m_5").style.display="none";
        document.getElementById("m_6").style.display="none";
        document.getElementById("m_7").style.display="none";
        document.getElementById("m_8").style.display="none";
        document.getElementById("m_9").style.display="none";
        document.getElementById("m_10").style.display="none";
        document.getElementById("m_11").style.display="none";
        document.getElementById("m_12").style.display="none";
    }
}


function checkm(){
    var issue=0;
    var eps_1=document.form.EPS_1.value;
    var eps_2=document.form.EPS_2.value;
    var eps_3=document.form.EPS_3.value;
    var eps_4=document.form.EPS_4.value;

    var m_1=document.form.m_1.value;
    var m_2=document.form.m_2.value;
    var m_3=document.form.m_3.value;
    var m_4=document.form.m_4.value;
    var m_5=document.form.m_5.value;
    var m_6=document.form.m_6.value;
    var m_7=document.form.m_7.value;
    var m_8=document.form.m_8.value;
    var m_9=document.form.m_9.value;
    var m_10=document.form.m_10.value;
    var m_11=document.form.m_11.value;
    var m_12=document.form.m_12.value;

    var dividend_rate=document.form.dividend_rate.value;
    var share=document.form.share.value;
    // try{
    //     eps_unit=parseInt(eps);
    //     if (eps_unit>1000){
    //         alert("EPS數字過大");
    //         issue+=1;
    //     }
    // }
    // catch{
    //     alert("EPS應為數字而非"+typeof(eps));
    //     eps="";
    // }
    // if (state==1){
    //     if (eps_1.length<=0 | eps_2.length<=0 | eps_3.length<=0 | eps_4.length<=0){
    //     issue+=1;
    //     alert("EPS不可為空");
    // }
    // else{
    //     if (m_1.length<=0 |
    //         m_2.length<=0 |
    //         m_3.length<=0 |
    //         m_4.length<=0 |
    //         m_5.length<=0 |
    //         m_6.length<=0 |
    //         m_7.length<=0 |
    //         m_8.length<=0 |
    //         m_9.length<=0 |
    //         m_10.length<=0 |
    //         m_11.length<=0 |
    //         m_12.length<=0
    //         ){
    //             issue+=1;
    //             alert("EPS不可為空");
    //         }
    // }
    // }
    if (dividend_rate.length<=0){
        issue+=1;
        alert("配息率不可為空");
    }
    if (share.length<=0){
        issue+=1;
        alert("股價不可為空");
    }
    console.log(share.length);
    if (issue==0){
        return true;
    }
    else{
        return false;
    }
}
 
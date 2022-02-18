function logout(){
    if (window.confirm("確定登出？")){
        window.location.href='/signout';
    }
}
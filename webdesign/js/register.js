function regConfirm() {
    var email = document.getElementById("email").value;
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var passwordconf = document.getElementById("passwordconf").value;

    if (password == passwordconf) {
        
        //User auth -> redirect to main stream
        
        window.location.href = 'stream.html';
    } else alert("Passwords do not match!");

}
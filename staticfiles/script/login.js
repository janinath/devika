
function validateForm(){
    var email=document.getElementById("email").value
    var password=document.getElementById("password").value 
    

    if (email===""||password===""){
        document.getElementById("Error").innerHTML="Invalid email or password"
       
        
        return false
    }
    
    
    else{

    return true
    }

}


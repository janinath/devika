function validateForm(){
    var email=document.getElementById("email").value
    var password=document.getElementById("password").value 
    

    if (email===""||password===""){
        document.getElementById("Error").innerHTML="All fields must be filled out"
       
        
        return false
    }
    
    
    else{

    return true
    }

}
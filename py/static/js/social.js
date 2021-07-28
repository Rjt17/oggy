function statusChangeCallback(response) {  // Called with the results from FB.getLoginStatus().
    // The current login status of the person.
    if (response.status === 'connected') {   // Logged into your webpage and Facebook.
      loginFb();  
    } else {                                 // Not logged into your webpage or we are unable to tell.
      
    }
}


function checkLoginState() {               
    FB.getLoginStatus(function(response) {   
      statusChangeCallback(response);
    });
}


window.fbAsyncInit = function() {
    FB.init({
      appId      : '2687153301548264',
      cookie     : true,                     
      xfbml      : true,                    
      version    : 'v8.0' 
    });
    
    
    FB.getLoginStatus(function(response) {  
      statusChangeCallback(response);        
    });
};

function loginFb() { 
    FB.api('/me', function(response) {
      //console.log('Successful login for: ' + response.name);
      
        $.ajax({
            type: 'POST',
            url: "ajax",
            crossDomain:true,
            data:{"method":"facebookLogin","res":response},
            success: function(resultData) 
            { 
                location.href('');
            }
        });
          
    });
}
const usernameField = document.querySelector('#usernameField');
const feedbackArea = document.querySelector('.invalid_feedback');
const emailField = document.querySelector('#emailField');
const emailfeedbackArea = document.querySelector('.emailfeedbackArea');
const usernameSuccessOutput = document.querySelector('.usernameSuccessOutput');


emailField.addEventListener('keyup', (e)=>{

    const emailVal = e.target.value;

    emailField.classList.remove("is-invalid");
    emailfeedbackArea.style.display = "none";

    if(emailVal.length > 0){
    fetch("/authentication/validate-email",{
        body: JSON.stringify({email: emailVal}),
        method:"POST",

    })
    .then(res=>res.json())
    .then(data=>{
        console.log('data', data)
        if(data.email_error){
            emailField.classList.add("is-invalid");
            emailfeedbackArea.style.display = "block";
            emailfeedbackArea.innerHTML=(data.email_error);
        }
    });
  } 

})





usernameField.addEventListener("keyup", (e) => {
    console.log('77777', 77777);

    const usernameVal = e.target.value;
    usernameSuccessOutput.textContent= 'Checking ${usernameVal}'

    usernameField.classList.remove("is-invalid");
    feedbackArea.style.display = "none";

    if(usernameVal.length > 0){
    fetch("/authentication/validate-username",{
        body: JSON.stringify({username: usernameVal}),
        method:"POST",

    })
    .then(res=>res.json())
    .then(data=>{
        console.log('data', data)
        usernameSuccessOutput.style.display = "none";
        if(data.username_error){
            usernameField.classList.add("is-invalid");
            feedbackArea.style.display = "block";
            feedbackArea.innerHTML=(data.username_error);
        }
    });
  } 
})
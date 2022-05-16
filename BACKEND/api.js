// "async"란 비동기. 기존 줄 순서대로 실행이 되던 방식과는 다르게 어긋나게 진행하도록 하는 명령어


async function handleSignin() {
    // console.log('회원가입버튼반응')

    const signupData = {
        email = document.getElementById("floatingInput").value;
        password = document.getElementById("floatingPassword").value
    }
    console.log(email + password)

    const response = await fetch('http://localhost:5000/signup', {
        method: 'POST',
        body: json.stringify(signupData)
    })


}
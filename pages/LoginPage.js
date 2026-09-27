import page from "@playwright/test"

export class LoginPage{
    constructor(page)
    {
        this.page=page;
        this.username=page.getByPlaceholder("Enter Email")
        this.password=page.getByPlaceholder("Enter Password")
        this.loginbutton=page.getByText("Sign in",{exact:true})
        this.newUserSignUp=page.getByText("New user? Signup",{exact:true})
        this.errorMessage=page.locator(".errorMessage")

    }
    async LoginToApplication(username,password){
        await this.username.fill(username)
        await this.password.fill(password)
        await this.loginbutton.click()
    }
    async newUserSignUp(){
        await this.newUserSignUp.click()
    }
    async ErrorMessage(){
        return await this.errorMessage.textContent()

    }
}



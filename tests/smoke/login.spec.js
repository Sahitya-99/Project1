import {test,expect} from '@playwright/test'
import { LoginPage } from '../../pages/LoginPage'
import { DashBoardPage} from '../../pages/DashBoardPage'
import user from '../../test_data/users_data.json'

test.describe("this is starting of test",{tags:['smoke','login']},()=>{
    test("login to new user",async({page})=>
{
    page.goto('https://freelance-learn-automation.vercel.app/login')
    const loginPage=new LoginPage(page)
    await loginPage.LoginToApplication(user.username,user.password)
    const dashBoardPage= new DashBoardPage(page)
    await dashBoardPage.Signout()
})

})




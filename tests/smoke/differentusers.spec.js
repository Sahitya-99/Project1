import {test,expect} from '@playwright/test'
import { LoginPage } from '../../pages/LoginPage'
import { DashBoardPage} from '../../pages/DashBoardPage'
import multiuser from '../../test_data/multi_users.json'

test.describe("this is data driven tests",{tags:['data_driven','login']},()=>{
    for (const user of multiuser)
    {
    test(`login to multi user ${user.id}`,async({page})=>
        {
            await page.goto('https://freelance-learn-automation.vercel.app/login')
            const loginPage=new LoginPage(page)
            await loginPage.LoginToApplication(user.username,user.password)
            expect(await loginPage.ErrorMessage()).toBe(user.message)
})

}


})
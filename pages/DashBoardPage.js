import {page} from "@playwright/test"

export class DashBoardPage{
    constructor(page)
    {
        this.page=page
        this.menuIcon=page.getByAltText("menu")
        this.signout=page.getByText("Sign out",{exact:true})
    }
    async Signout()
    {
        await this.menuIcon.click()
        await this.signout.click()
    }
}
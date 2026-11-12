import { getUsers } from './scripts/api.js'
import { renderUsers } from './scripts/renderUsers.js'
import { addUser } from './scripts/addUser.js'

async function main(){
    const users = await getUsers()

    console.log(users)

    users.forEach(element => {
        renderUsers(element)
    })

    addUser()
}

main()

export async function getUsers(){
    try {
        const responce = await fetch('https://jsonplaceholder.typicode.com/users')
        if (!responce.ok){
            throw new Error(`Status code: ${responce.status}`)
        }
        return await responce.json()
    } catch (error){
        console.error(error)
        return
    }
}

export async function deleteUser(userId){
    try {
        const responce = await fetch(
            `https://jsonplaceholder.typicode.com/users/${userId}`,
            {
                method : 'DELETE',
                headers : {
                    'Content-Type' : 'application/json'
                }
            }
        )
        if (!responce.ok){
            throw new Error(`Status code: ${responce.status}`)
        }
        console.log('Successfuly deleted')
    } catch (error){
        console.error(error)
    }
}

export async function postUser(users){
    try {
        const responce = await fetch(
            'https://jsonplaceholder.typicode.com/users',
            {
                method : "POST",
                headers : {
                    'Content-Type' : 'application/json'
                },
                body : JSON.stringify(users)
            }
        )
        if (!responce.ok){
            throw new Error(`Status code: ${responce.status}`)
        }
        console.log(await responce.json())
    } catch (error){
        console.error(error)
    }
}

export async function patchUser(user){
    try {
        const responce = await fetch(
            `https://jsonplaceholder.typicode.com/users/${user.id}`,
            {
                method : 'PATCH',
                headers : {
                    'Content-Type' : 'application/json'
                },
                body : JSON.stringify(user)
            }
        )
        if (!responce.ok){
            throw new Error(`Status code: ${responce.status}`)
        }
        console.log(await responce.json())
    } catch (error){
        console.error(error)
    }
}
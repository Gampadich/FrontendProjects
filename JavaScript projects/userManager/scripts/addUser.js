import { postUser } from "./api.js"
import { renderUsers } from "./renderUsers.js"

export function addUser(){
    const usersBox = document.getElementById('users')
    const addBtn = document.getElementById('addBtn')

    addBtn.addEventListener('click', () => {
        const newUser = document.createElement('li')
        const inputBox = document.createElement('div')
        const nameInp = document.createElement('input')
        const emailInp = document.createElement('input')
        const addressInp = document.createElement('input')
        const buttonBox = document.createElement('div')
        const saveBtn = document.createElement('button')
        const cancelBtn = document.createElement('button')
        const error = document.createElement('p')
        error.innerText = 'Please fill all fields...'
        error.style.display = 'none'
        inputBox.classList.add('textBox')
        buttonBox.classList.add('buttonBox')
        nameInp.placeholder = "Name..."
        emailInp.placeholder = "Email..."
        addressInp.placeholder = "City..."
        saveBtn.innerText = 'Save'
        saveBtn.classList.add('saveBtn')
        cancelBtn.innerText = 'Cancel'
        cancelBtn.classList.add('delete')

        inputBox.append(nameInp, emailInp, addressInp)
        buttonBox.append(saveBtn, cancelBtn)
        newUser.append(inputBox, buttonBox)
        usersBox.prepend(error, newUser)

        cancelBtn.addEventListener('click', () => {
            newUser.remove()
        })

        saveBtn.addEventListener('click', async () => {
            if(nameInp.value.trim() !== '' && emailInp.value.trim() !== '' && addressInp.value.trim() !== ''){
                error.style.display = 'none'
                const userObj = {
                    name : nameInp.value.trim(),
                    email : emailInp.value.trim(),
                    address : {
                        city : addressInp.value.trim()
                    }
                }
                await postUser(userObj)
                newUser.remove()
                renderUsers(userObj)
            } else {
                error.style.display = 'block'
            }
        })
    })
}
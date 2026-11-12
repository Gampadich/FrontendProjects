import { deleteUser, patchUser } from "./api.js"

export function renderUsers(user){
    const usersContainer = document.getElementById('users')
    const userBox = document.createElement('li')
    const textBox = document.createElement('div')
    const buttonBox = document.createElement('div')
    const userName = document.createElement('span')
    const userEmail = document.createElement('span')
    const userCity = document.createElement('span')
    const deleteButton = document.createElement('button')
    const editBtn = document.createElement('button')
    deleteButton.innerText = 'Delete'
    deleteButton.classList.add('delete')
    editBtn.innerText = 'Edit'
    editBtn.classList.add('edit')
    textBox.classList.add('textBox')
    userName.innerText = user.name
    userEmail.innerText = user.email
    userCity.innerText = user.address.city
    buttonBox.classList.add('buttonBox')
    textBox.append(userName, userEmail, userCity)
    buttonBox.append(editBtn, deleteButton)
    userBox.append(textBox, buttonBox)
    usersContainer.append(userBox)

    deleteButton.addEventListener('click', () => {
        userBox.remove()
        deleteUser(user.id)
    })

    let isEditPressed = false
    let nameInp
    let emailInp
    let cityInp

    editBtn.addEventListener('click', () => {
        if (!isEditPressed){
            nameInp = document.createElement('input')
            emailInp = document.createElement('input')
            cityInp = document.createElement('input')
            nameInp.placeholder = 'Name...'
            nameInp.value = userName.textContent.trim()
            userName.innerText = ''
            userName.append(nameInp)
            emailInp.placeholder = 'Email...'
            emailInp.value = userEmail.textContent.trim()
            userEmail.innerText = ''
            userEmail.append(emailInp)
            cityInp.placeholder = 'City...'
            cityInp.value = userCity.textContent.trim()
            userCity.innerText = ''
            userCity.append(cityInp)
            editBtn.innerText = 'Save'
            editBtn.classList.remove('edit')
            editBtn.classList.add('saveBtn')
            isEditPressed = true
        } else {
            if (nameInp.value.trim() === ''
                || nameInp.value.trim() === user.name
                && emailInp.value.trim() === ''
                || emailInp.value.trim() === user.email
                && cityInp.value.trim() === ''
                || cityInp.value.trim() === user.address.city
            ) {
                nameInp.remove()
                userName.innerText = user.name
                emailInp.remove()
                userEmail.innerText = user.email
                cityInp.remove()
                userCity.innerText = user.address.city
            } else {
                const userObj = {
                    id : user.id, 
                    name : nameInp.value.trim(),
                    email : emailInp.value.trim(),
                    address : {
                        city : cityInp.value.trim()
                    }
                }
                patchUser(userObj)
                userName.innerText = nameInp.value
                nameInp.remove()
                userEmail.innerText = emailInp.value
                emailInp.remove()
                userCity.innerText = cityInp.value
                cityInp.remove()
            }
            editBtn.classList.remove('saveBtn')
            editBtn.classList.add('edit')
            editBtn.innerText = 'Edit'
            deleteButton.innerText = 'Delete'
            isEditPressed = false
        }
    })
}
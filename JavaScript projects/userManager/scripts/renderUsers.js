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
    userName.setAttribute('data-test-id', 'name')
    userEmail.innerText = user.email
    userEmail.setAttribute('data-test-id', 'email')
    userCity.innerText = user.address.city
    userCity.setAttribute('data-test-id', 'city')
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
            let username = nameInp.value
            let email = emailInp.value
            let city = cityInp.value
            if (nameInp.value.trim() === '' || nameInp.value.trim() === user.name){
                username = user.name
            }
            if (emailInp.value.trim() === '' || emailInp.value.trim() === user.email){
                email = user.email
            }
            if (cityInp.value.trim() === '' || cityInp.value.trim() === user.address.city){
                city = user.address.city
            }
            userCity.innerText = user.address.city
            const userObj = {
                id : user.id,
                name : username,
                email : email,
                address : {
                    city : city
                }
            }
            patchUser(userObj)
            userName.innerText = nameInp.value
            nameInp.remove()
            userEmail.innerText = emailInp.value
            emailInp.remove()
            userCity.innerText = cityInp.value
            cityInp.remove()
            editBtn.classList.remove('saveBtn')
            editBtn.classList.add('edit')
            editBtn.innerText = 'Edit'
            deleteButton.innerText = 'Delete'
            isEditPressed = false
        }
    })
}
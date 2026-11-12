const tasks = document.getElementById('tasks')
const taskInp = document.getElementById('taskInp')
const addTaskBtn = document.getElementById('addTask')
const error = document.getElementById('error')

let total = 0
let completed = 0
let remaining = 0

const tasksArr = JSON.parse(localStorage.getItem('tasks') || '[]')
console.log(tasksArr)

tasksArr.forEach(element => {
    addTaskToTasks(element)
});


function addTaskToTasks(taskArr){
    const task = document.createElement('li')
    const text = document.createElement('span')
    const buttonsDiv = document.createElement('div')
    const deleteBtn = document.createElement('button')
    deleteBtn.classList.add('deleteButton')
    deleteBtn.innerText = 'Delete'
    const doneButton = document.createElement('button')
    doneButton.classList.add('doneButton')
    doneButton.innerText = 'Done'
    const editBtn = document.createElement('button')
    editBtn.classList.add('edit')
    editBtn.innerText = 'Edit'
    text.innerText = taskArr.title
    buttonsDiv.append(editBtn)
    buttonsDiv.append(doneButton)
    buttonsDiv.append(deleteBtn)
    task.append(text)
    task.append(buttonsDiv)
    tasks.append(task)
    remaining++
    total++
    updateStats()

    if (taskArr.isDone === true){
        text.classList.toggle('completed')
        completed++
        remaining--
        updateStats()
        doneButton.disabled = true
        editBtn.disabled = true
        doneButton.classList.remove('doneButton')
    }

    doneButton.addEventListener('click', () => {
        taskArr.isDone = true
        saveTask()
        text.classList.toggle('completed')
        completed++
        remaining--
        updateStats()
        doneButton.disabled = true
        editBtn.disabled = true
        doneButton.classList.remove('doneButton')
        editBtn.classList.remove('edit')
    })

    deleteBtn.addEventListener('click', () => {
        if(text.classList.contains('completed')){
            completed--
        } else{
            remaining--
        }
        total--
        task.remove()
        updateStats()
        const index = tasksArr.findIndex(item => item.id === taskArr.id)
        tasksArr.splice(index, 1)
        saveTask()
    })

    let isEditing = false
    let prevText
    let editInp

    editBtn.addEventListener('click', () => {
        if (!isEditing){
            editBtn.classList.remove('edit')
            editBtn.classList.add('doneButton')
            editBtn.innerText = 'Save'
            prevText = text.innerText
            text.innerText = ''
            editInp = document.createElement('input')
            editInp.value = prevText
            text.append(editInp)
            isEditing = true
        } else {
            const newTitle = editInp.value.trim()
            if (newTitle !== ''){
                taskArr.title = newTitle
                text.innerText = newTitle
            } else {
                taskArr.title = prevText
                text.innerText = prevText
            }
            saveTask()
            editBtn.classList.remove('doneButton')
            editBtn.classList.add('edit')
            editInp.remove()
            editBtn.innerText = 'Edit'
            isEditing = false
        }
    })
}

function saveTask(){
    localStorage.setItem('tasks', JSON.stringify(tasksArr))
}

function updateStats(){
    const totalElem = document.getElementById('total')
    const completedElem = document.getElementById('completed')
    const remainingElem = document.getElementById('remaining')

    totalElem.innerText = `Total tasks: ${total}`
    completedElem.innerText = completed
    remainingElem.innerText = `Remaining: ${remaining}`
}

addTaskBtn.addEventListener('click', () => {
    if (taskInp.value.trim() !== ''){
        error.innerText = ''
        const task = {
            id : Date.now(),
            title : taskInp.value.trim(),
            isDone : false
        }
        tasksArr.push(task)
        saveTask()
        addTaskToTasks(task)
        taskInp.value = ''
    } else {
        error.innerText = 'Please enter a task'
    }
})
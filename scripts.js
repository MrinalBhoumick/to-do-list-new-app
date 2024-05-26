document.addEventListener('DOMContentLoaded', function() {
    const taskInput = document.getElementById('new-task');
    const addButton = document.getElementById('add-button');
    const taskList = document.getElementById('task-list');

    addButton.addEventListener('click', function() {
        const taskText = taskInput.value.trim();
        if (taskText !== '') {
            addTask(taskText);
            taskInput.value = '';
        }
    });

    taskList.addEventListener('click', function(e) {
        if (e.target.tagName === 'BUTTON' && e.target.classList.contains('delete')) {
            const taskItem = e.target.parentElement;
            taskList.removeChild(taskItem);
        } else if (e.target.tagName === 'INPUT' && e.target.type === 'checkbox') {
            const taskItem = e.target.parentElement;
            taskItem.classList.toggle('completed');
        }
    });

    function addTask(taskText) {
        const taskItem = document.createElement('li');

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';

        const span = document.createElement('span');
        span.textContent = taskText;

        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.classList.add('delete');

        taskItem.appendChild(checkbox);
        taskItem.appendChild(span);
        taskItem.appendChild(deleteButton);

        taskList.appendChild(taskItem);
    }
});

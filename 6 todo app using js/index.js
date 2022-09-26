const $addTodo=document.getElementById('addTodo');
const $todoList=document.getElementById('todoList');
$addTodo.addEventListener('keypress',(e)=>{
    if(e.code==="Enter" && e.target.value!==""){
        let todo=e.target.value;
        let $todoItem=document.createElement('li');
        let todoId=new Date().getTime();
        $todoItem.innerHTML=`
        
            <input id="${todoId}" type="checkbox">
            <label for="${todoId}">${todo}</label>
               
        `;
        $todoList.appendChild($todoItem);
        
        //console.log($todoItem);
        $addTodo.value="";

    }
});

$todoList.addEventListener('click',(e)=>{
    if(e.target.checked){
        e.target.parentElement.classList.add("completed");
    }else{
        e.target.parentElement.classList.remove("completed");
    }
});
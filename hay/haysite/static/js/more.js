var textField = document.getElementById('question-wrapper');
console.log(textField)

textField.addEventListener('click', function(){
    document.getElementById('no').classList.add('hidden');
    document.getElementById('submit').classList.remove('hidden');
})
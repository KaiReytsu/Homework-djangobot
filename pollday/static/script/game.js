// Добавить файл js с игрой
// "угадай число".
// Вы загадываете число в диапазоне.
// Компьютер задает вопросы,
// пользователь выбирает "да" или "нет".
// В базу данных необходимо сохранить
// дату-время отгадывания,
// продолжительность игры,
// и количество попыток.
// Можно вывести на одтельной странице 
// таблицу этой статистики.
// Костыль - сделать форму со спрятанными
// полями, оставив снаружи только 
// копочку Submit.
var start_of_range;
var end_of_range;

function mean(start_num, end_num){
    var mean_num;
    var middle = 2;
    mean_num = (end_num - start_num)/middle;
    mean_num = parseInt(mean_num + start_num);
    return mean_num
}

function startgame(){
    start_of_range = parseInt(document.getElementById('start').value); 
    end_of_range = parseInt(document.getElementById('end').value);
    var q_text = document.getElementById('question');
    var yes_or_no = document.getElementById('yes_or_no');
    if (end_of_range > start_of_range){
        q_text.innerHTML = 'Ваше число больше ' + mean(start_of_range, end_of_range) + '?';
        yes_or_no.style.display = 'block';
    } else{
        q_text.innerHTML = 'Упс, диапазон неверен. Конец диапазона должен быть больше начала диапазона'
    }
}

function more_or_less(button_value){
    var q_text = document.getElementById('question');
    var yes_or_no = document.getElementById('yes_or_no');
    var difference = end_of_range - start_of_range;
    yes_or_no.style.display = 'block';
    if (button_value.value == 'Да'){
        start_of_range = mean(start_of_range, end_of_range);
        console.log('start', start_of_range, 'end', end_of_range)
        if (difference == 1){
            start_of_range +=1;
        }
    } else if(button_value.value == 'Нет'){
        end_of_range = mean(start_of_range, end_of_range);
        if (difference == 1){
            end_of_range -=1;
        }
        console.log('start', start_of_range, 'end', end_of_range)
    }
    if (start_of_range == end_of_range){
        q_text.innerHTML = 'Вы загадали ' + start_of_range;
        yes_or_no.style.display = 'none';
    } else {
        q_text.innerHTML = 'Ваше число больше ' + mean(start_of_range, end_of_range) + '?';
    }
    
}
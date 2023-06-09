// 2. Cоздать функцию greeting, которая принимает в качестве аргумента имя человека и выводит приветствие, используя переданное ей имя, в консоль.

// Необходимо у пользователя запросить имя и вызвать функцию greeting, передав туда полученное от пользователя значение.

function greeting(user_name){
    alert(`Привет, ${user_name}!!!`);
}

function answerToQuestion(userAnswer){
    switch (userAnswer) {
        case "хорошо":
        case "отлично":
        case "замечательно":
            alert("Класс, рад за тебя");
            break;
        case "плохо":
            alert("Блин, ну ты держись");
            break;
        default:
            alert("Ууу, как всё запущено.");
            break;
    }
}

let name = prompt("Как твоё имя? ");
greeting(name);

let ans = prompt("Как дела? ").toLowerCase();
answerToQuestion(ans);

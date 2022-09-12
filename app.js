document 
//document로 해당 html 프로퍼티 와 element 내용들을 가져올 수 있다.

document.title = "Hello! From JS"

document.getElementsById("title"); 

// id 로 element 가져오기
const title = document.getElementsById("title"); 

title.innerText = "Got you"
console.log(title.id);
console.log(title.className);

// class name 으로 가져오기
const hellos = document.getElementsByClassName("hello");
console.log(hellos);


// querySelector ** 스트링 안에 .을 찍는다. 여러가지 있을 경우 첫번째 것만 가져온다. 모두 가져오려면 querySelectorAll사 용
const title = document.querySelector(".title h1")

event
// 누군가가 title을 클릭 했을때


const title = document.querySelector("div.title :first-child h1")

function handtitleclick() {
    console.log("title was clickded!");
}


title.addEventListener("click", handtitleclick);
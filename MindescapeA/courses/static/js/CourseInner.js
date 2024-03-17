  // sidebar part
$(document).ready(function() {
  $('.btn').click(function() {
    $(this).toggleClass("click");
    $('.sidebar').toggleClass("show");
  });
  
  $('.feat-btn').click(function() {
    $('nav ul .feat-show').toggleClass("show");
    $('nav ul .first').toggleClass("rotate");
  });
  
  $('.serv-btn').click(function() {
    $('nav ul .serv-show').toggleClass("show1");
    $('nav ul .second').toggleClass("rotate");
  });
  
  $('nav ul li').click(function() {
    $(this).addClass("active").siblings().removeClass("active");
  });
// add lesson part
  $('.addLessonBtn').click(function() {
    $('#createLessonModal').css('display', 'block');
  });
});
// add section part
document.getElementById("createSectionBtn").addEventListener("click", function() {
  document.getElementById("createSectionModal").style.display = "block";
});

document.getElementsByClassName("close")[0].addEventListener("click", function() {
  document.getElementById("createSectionModal").style.display = "none";
});

document.getElementsByClassName("close")[1].addEventListener("click", function() {
  document.getElementById("createLessonModal").style.display = "none";
});

window.addEventListener("click", function(event) {
  if (event.target == document.getElementById("createSectionModal")) {
    document.getElementById("createSectionModal").style.display = "none";
  }
  if (event.target == document.getElementById("createLessonModal")) {
    document.getElementById("createLessonModal").style.display = "none";
  }
});
// for sectiom
document.getElementById("sectionForm").addEventListener("submit", function(event) {
  event.preventDefault();
  var sectionTitle = document.getElementById("sectionTitle").value;
  addNewSection(sectionTitle);
  document.getElementById("createSectionModal").style.display = "none";
});
// for the lesson
document.getElementById("lessonForm").addEventListener("submit", function(event) {
  event.preventDefault();
  var lessonTitle = document.getElementById("lessonTitle").value;
  addNewLesson(lessonTitle);
  document.getElementById("createLessonModal").style.display = "none";
});
// add the created section to the sidebar
function addNewSection(title) {
  var ul = document.querySelector(".sidebar ul");
  var li = document.createElement("li");
  var a = document.createElement("a");
  var textNode = document.createTextNode(title);
  a.appendChild(textNode);
  li.appendChild(a);
  ul.appendChild(li);
}
// add the created lesson to its section 
function addNewLesson(title) {
  var ul = document.querySelector(".sidebar ul .active ul");
  var li = document.createElement("li");
  var a = document.createElement("a");
  var textNode = document.createTextNode(title);
  a.appendChild(textNode);
  li.appendChild(a);
  ul.appendChild(li);
}

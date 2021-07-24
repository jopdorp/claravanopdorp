console.log("hello world");
console.log("time before $.get call", new Date())
$.get("https://assets.calendly.com/assets/external/widget.css", {}, function(result, status){
  console.log("time in $.get callback function", new Date())

  console.log(result);
  console.log(status);
})

$(document).ready(function(){
  $(".nav-item").click(function(e){
    console.log("a nav-item element was clicked!");
  });
});

console.log("time after $.get call", new Date())

$(document).ready(function() {
  $('td').each(function() {
    var cellText = $(this).text().toLowerCase();
    if (cellText.includes('sp') || cellText.includes('sx') || cellText.includes('qi')
    || cellText.includes('qa') || cellText.includes('t') || cellText.includes('b')) {
      $(this).addClass('strong');
    } else if (cellText.includes('days') || cellText.includes('hrs') || cellText.includes('secs') || cellText.includes('mins')) {
      $(this).addClass('fragile');
    } else if (cellText.includes('m')) {
      $(this).addClass('medium');
    } else {
      $(this).addClass('weak');
    }
  });
});


document.addEventListener('DOMContentLoaded', function () {
    var first_section_button = document.querySelector("#headingOne button");
    first_section_button.addEventListener('click', function(){
        first_a = document.querySelector("#first-collapse")
        console.log(first_a)
        first_a.scrollIntoView()
    });
    var second_section_button = document.querySelector("#headingTwo button");
    second_section_button.addEventListener('click', function(){
        second_a = document.getElementById("#second-collapse")
        second_a.scrollIntoView()
    });
    var third_section_button = document.querySelector("#headingThree button");
    third_section_button.addEventListener('mouseover', function(){
        third_a = document.getElementById("#third-collapse")
        third_a.scrollIntoView()
    });

//    // Smooth scroll to #headingOne on click over button in #headingOne
//    var button_1 = document.querySelector('#headingOne .btn');
//    button_1.addEventListener('click', function() {
//        var targetElement = document.getElementById('headingOne');
//        if (targetElement) {
//            targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
//        }
//    });
//    // Smooth scroll to #headingTwo on click over button in #headingTwo
//    var button_2 = document.querySelector('#headingTwo .btn');
//    button_2.addEventListener('click', function() {
//        var targetElement = document.getElementById('headingTwo');
//        if (targetElement) {
//            targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
//        }
//    });
//
//    var button_3 = document.querySelector('#headingThree .btn');
//    button_3.addEventListener('click', function() {
//        var targetElement = document.getElementById('headingThree');
//        if (targetElement) {
//            targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
//        }
//    });

    // Add more event listeners for other buttons as needed
});

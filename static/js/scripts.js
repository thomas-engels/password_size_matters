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
    var buttons = document.querySelectorAll('.explanations .card-header .btn');
    buttons.forEach(function(button) {
        button.addEventListener('mouseenter', function() {
            button.click();
        });
    });
});
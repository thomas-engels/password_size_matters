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

$(document).ready(function() {
    $('a.dropdown-menu').on('click', function(event) {
        if (this.hash !== '') {
            event.preventDefault();

            const hash = this.hash;

            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 800, function(){
                window.location.hash = hash;
            });
        }
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var links = document.querySelectorAll('.introduction .nav-link');
    console.log(links);
    var card_bodies = document.querySelectorAll('.introduction .card-body');
    console.log(card_bodies);
    var card = document.querySelector('.card');
    console.log(card)
    var table = document.querySelector('#main-section')
    console.log(table)
    var button = document.querySelector('.main .btn')
    console.log(button)

    links.forEach(function(link){
        link.addEventListener('click', function(event){

            event.preventDefault();

            links.forEach(function(link){
                link.classList.remove('active');
            });

            link.classList.add('active');

            card_bodies.forEach(function(card_body){
                card_body.classList.remove('active');
            });

            // Show Tab by querying the links target-attribute; which returns the target card body element
            var target = document.querySelector(link.getAttribute('data-target'));
            // Simply add the target card body element
            target.classList.add('active');

            card.scrollIntoView({ behavior: 'smooth' });
        });
    });
});
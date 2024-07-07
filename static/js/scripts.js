$(document).ready(function() {
  $('td').each(function() {
    var cellText = $(this).text().toLowerCase();
    if (cellText.includes('sp') || cellText.includes('sx') || cellText.includes('qi')
    || cellText.includes('qa') || cellText.includes('t') || cellText.includes('b') || cellText.includes('oc')) {
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

document.addEventListener("DOMContentLoaded", function() {
    var nav_links = document.querySelectorAll('.dropdown-item')
    var sections = document.querySelectorAll('h3')
    var parents = []
    for (let i = 0; i < sections.length; i++) {
        parents.push(sections[i].parentElement.parentElement)
    };
    for (let i = 0; i < sections.length; i++) {
        nav_links[i].addEventListener('click', function(event) {
            event.preventDefault();
            parents[i].scrollIntoView({ behavior: 'smooth'} );
        });
    }

});

document.addEventListener("DOMContentLoaded", function() {
    var links = document.querySelectorAll('.introduction .nav-link');

    var card_bodies = document.querySelectorAll('.introduction .card-body');

    var card = document.querySelector('.card');




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

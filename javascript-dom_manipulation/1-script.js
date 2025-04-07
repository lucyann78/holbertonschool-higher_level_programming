/// Obtener el elemento con id 'red_header'
const redHeader = document.getElementById('red_header');
redHeader.addEventListener('click', function() {
    const header = document.querySelector('header');
    header.style.color = '#FF0000';
});


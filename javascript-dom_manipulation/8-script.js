document.addEventListener('DOMContentLoaded', () => {
    const helloDiv = document.getElementById('hello');
  
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        helloDiv.textContent = data.hello;
      })
      .catch(error => {
        helloDiv.textContent = 'Failed to fetch greeting';
        console.error('There was a problem with the fetch operation:', error);
      });
  });
  
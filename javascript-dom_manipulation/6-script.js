const characterDiv = document.getElementById('character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    characterDiv.textContent = data.name;
  })
  .catch(error => {
    characterDiv.textContent = 'Failed to fetch character name';
    console.error('There was a problem with the fetch operation:', error);
  });

const form = document.querySelector('form');
const regionInput = document.getElementById('region');
const populationOutput = document.getElementById('population');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const region = regionInput.value;
    const response = await fetch(`/api/population?region=${region}`);
    const data = await response.json();
    populationOutput.innerHTML = `${data.region}: ${data.population}`;
});

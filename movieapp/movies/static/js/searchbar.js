const searchInput = document.getElementById('searchInput');
const tiles = document.querySelectorAll('.movie-tile');
const noResults = document.getElementById('noResults');

searchInput.addEventListener('input', function () {
const query = this.value.toLowerCase();
let visibleCount = 0;

tiles.forEach(tile => {
    const name = tile.dataset.name;
    const isVisible = name.includes(query);
    tile.parentElement.style.display = isVisible ? 'block' : 'none'; // parent <a>
    if (isVisible) visibleCount++;
});

noResults.style.display = visibleCount === 0 ? 'block' : 'none';
  });
let selectedBike1 = null;
let selectedBike2 = null;

const search1Input = document.getElementById('search1');
const search2Input = document.getElementById('search2');
const results1Div = document.getElementById('results1');
const results2Div = document.getElementById('results2');
const selected1Div = document.getElementById('selected1');
const selected2Div = document.getElementById('selected2');
const comparisonTable = document.getElementById('comparison-table');

async function searchMotorcycles(query, resultsDiv, searchNum) {
    if (query.length < 2) {
        resultsDiv.classList.remove('active');
        return;
    }
    
    try {
        const response = await fetch(`/api/search?q=${encodeURIComponent(query)}&limit=10`);
        const motorcycles = await response.json();
        
        if (motorcycles.length === 0) {
            resultsDiv.innerHTML = '<div class="search-result-item">No results found</div>';
            resultsDiv.classList.add('active');
            return;
        }
        
        resultsDiv.innerHTML = motorcycles.map(bike => `
            <div class="search-result-item" onclick="selectBike(${bike.id}, ${searchNum})">
                <strong>${bike.brand} ${bike.model}</strong> (${bike.year || 'N/A'})
            </div>
        `).join('');
        
        resultsDiv.classList.add('active');
    } catch (error) {
        console.error('Search error:', error);
    }
}

async function selectBike(bikeId, searchNum) {
    try {
        const response = await fetch(`/api/motorcycle/${bikeId}`);
        const bike = await response.json();
        
        if (searchNum === 1) {
            selectedBike1 = bike;
            selected1Div.innerHTML = `<strong>Selected:</strong> ${bike.brand} ${bike.model} (${bike.year || 'N/A'})`;
            selected1Div.classList.add('active');
            results1Div.classList.remove('active');
            search1Input.value = '';
        } else {
            selectedBike2 = bike;
            selected2Div.innerHTML = `<strong>Selected:</strong> ${bike.brand} ${bike.model} (${bike.year || 'N/A'})`;
            selected2Div.classList.add('active');
            results2Div.classList.remove('active');
            search2Input.value = '';
        }
        
        if (selectedBike1 && selectedBike2) {
            showComparison();
        }
    } catch (error) {
        console.error('Error selecting bike:', error);
    }
}

function showComparison() {
    const bike1Header = document.getElementById('bike1-header');
    const bike2Header = document.getElementById('bike2-header');
    const specsBody = document.getElementById('specs-body');
    
    bike1Header.textContent = `${selectedBike1.brand} ${selectedBike1.model}`;
    bike2Header.textContent = `${selectedBike2.brand} ${selectedBike2.model}`;
    
    const specs = [
        { label: 'Year', key: 'year' },
        { label: 'Category', key: 'category' },
        { label: 'Rating', key: 'rating' },
        { label: 'Displacement (cc)', key: 'displacement' },
        { label: 'Power (hp)', key: 'power' },
        { label: 'Torque (Nm)', key: 'torque' },
        { label: 'Engine Cylinder', key: 'engine_cylinder' },
        { label: 'Gearbox', key: 'gearbox' },
        { label: 'Fuel Capacity (L)', key: 'fuel_capacity' },
        { label: 'Cooling System', key: 'cooling_system' },
        { label: 'Dry Weight (kg)', key: 'dry_weight' },
        { label: 'Seat Height (mm)', key: 'seat_height' },
        { label: 'Front Brakes', key: 'front_brakes' },
        { label: 'Rear Brakes', key: 'rear_brakes' }
    ];
    
    specsBody.innerHTML = specs.map(spec => `
        <tr>
            <td><strong>${spec.label}</strong></td>
            <td>${selectedBike1[spec.key] || 'N/A'}</td>
            <td>${selectedBike2[spec.key] || 'N/A'}</td>
        </tr>
    `).join('');
    
    comparisonTable.style.display = 'block';
    comparisonTable.scrollIntoView({ behavior: 'smooth' });
}

if (search1Input) {
    search1Input.addEventListener('input', (e) => searchMotorcycles(e.target.value, results1Div, 1));
}

if (search2Input) {
    search2Input.addEventListener('input', (e) => searchMotorcycles(e.target.value, results2Div, 2));
}

document.addEventListener('click', (e) => {
    if (!e.target.closest('.search-box')) {
        results1Div.classList.remove('active');
        results2Div.classList.remove('active');
    }
});

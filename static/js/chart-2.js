        const ctx = document.getElementById('myChart').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'bar', // Or 'line', 'pie', etc.
            data: {
                labels: {{ labels | tojson }}, // Jinja2 tojson filter
                datasets: [{
                    label: 'My Dataset',
                    data: {{ data | tojson }}, // Jinja2 tojson filter
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });

const ctx = document.getElementById('7-day');

const DATA_COUNT = 6;
const labels = [];

const datapoints = [1, 3, 3, 2, 4, 4, 1];
const data = {
  labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
  datasets: [
 {
      label: 'Your responses',
      data: datapoints,
      borderColor: '#986b94',
      fill: false,
      cubicInterpolationMode: 'monotone',
      tension: 0.4
    },
  ]
};



const config = {
    type: 'line',
    data: data,
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: "Here's your responses from the last week"
        },
      },
      interaction: {
        intersect: false,
      },
      scales: {
        x: {
          display: true,
          title: {
            display: true
          }
        },
        y: {
          display: true,
          title: {
            display: true,
            text: 'Value'
          },
          suggestedMin: 0,
          suggestedMax: 5
        }
      }
    },
  };

  const myChart = new Chart(
    document.getElementById('7-day'),
    config
  );
  
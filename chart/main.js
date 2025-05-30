(async () => {
  new Chart(document.getElementById("chart"), {
    type: "line",
    data: {
      labels: ["24.05", "25.05", "26.05", "27.05", "28.05", "29.05", "30.05"],
      datasets: [
        {
          label: "Rafał Trzaskowski",
          data: [45.06, 46.15, 47.29, 48.85, 50.41, 54.45, 50],
          borderColor: "rgb(255, 102, 0)",
        },
        {
          label: "Karol Nawrocki",
          data: [54.94, 53.85, 52.71, 51.15, 49.59, 45.55, 50],
          borderColor: "rgb(0, 43, 127)",
        },
      ],
    },
    options: {
      scales: {
        y: {
          min: 0,
          max: 100,
          ticks: {
            stepSize: 10,
            callback: (value) => value + "%",
          },
        },
      },
      plugins: {
        tooltip: {
          callbacks: {
            label: (context) => {
              const label = context.dataset.label;
              const value = context.parsed.y;
              return label + ": " + value + "%";
            },
          },
        },
      },
    },
  });
})();

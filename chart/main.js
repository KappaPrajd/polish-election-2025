(async () => {
  new Chart(document.getElementById("chart"), {
    type: "line",
    data: {
      labels: ["24.05", "25.05", "26.05"],
      datasets: [
        {
          label: "Rafał Trzaskowski",
          data: [45.06, 46.15, 47.29],
          borderColor: "rgb(255, 102, 0)",
        },
        {
          label: "Karol Nawrocki",
          data: [54.94, 53.85, 52.71],
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

function getUrlParameter(name) {
  name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
  var regex = new RegExp("[\\?&]" + name + "=([^&#]*)");
  var results = regex.exec(location.search);
  return results === null
    ? ""
    : decodeURIComponent(results[1].replace(/\+/g, " "));
}

function fail() {
  document.getElementById("ct").innerHTML = "No Data to Display";
}

function plotPriceBedCorrelation(data) {
  var xData = [1, 2, 3, 4, 5, 6, 7, 8];
  var yData = [
    data.filter(t => t.beds == 1).map(t => t.price),
    data.filter(t => t.beds == 2).map(t => t.price),
    data.filter(t => t.beds == 3).map(t => t.price),
    data.filter(t => t.beds == 4).map(t => t.price),
    data.filter(t => t.beds == 5).map(t => t.price),
    data.filter(t => t.beds == 6).map(t => t.price),
    data.filter(t => t.beds == 7).map(t => t.price),
    data.filter(t => t.beds == 8).map(t => t.price)
  ];
  var colors = [
    "rgba(93, 164, 214, 0.5)",
    "rgba(255, 144, 14, 0.5)",
    "rgba(44, 160, 101, 0.5)",
    "rgba(255, 65, 54, 0.5)",
    "rgba(207, 114, 255, 0.5)",
    "rgba(127, 96, 0, 0.5)",
    "rgba(255, 140, 184, 0.5)",
    "rgba(79, 90, 117, 0.5)"
  ];

  var data = [];

  for (var i = 0; i < xData.length; i++) {
    var result = {
      type: "box",
      y: yData[i],
      name: xData[i],
      fillcolor: "cls",
      marker: {
        size: 2
      },
      line: {
        width: 1
      }
    };
    data.push(result);
  }

  layout = {
    title: "Number of Beds",
    yaxis: {
      range: [0, 800],
      title: "price"
    },

    margin: {
      l: 50,
      r: 30,
      b: 30,
      t: 80
    },
    paper_bgcolor: "rgb(243, 243, 243)",
    plot_bgcolor: "rgb(243, 243, 243)",
    showlegend: false
  };
  Plotly.newPlot("bedCorr", data, layout);
}

function plotPriceBedroomsCorrelation(data) {
  var xData = [1, 2, 3, 4, 5, 6];
  var yData = [
    data.filter(t => t.bedrooms == 1).map(t => t.price),
    data.filter(t => t.bedrooms == 2).map(t => t.price),
    data.filter(t => t.bedrooms == 3).map(t => t.price),
    data.filter(t => t.bedrooms == 4).map(t => t.price),
    data.filter(t => t.bedrooms == 5).map(t => t.price),
    data.filter(t => t.bedrooms == 6).map(t => t.price)
  ];
  var colors = [
    "rgba(93, 164, 214, 0.5)",
    "rgba(255, 144, 14, 0.5)",
    "rgba(44, 160, 101, 0.5)",
    "rgba(255, 65, 54, 0.5)",
    "rgba(207, 114, 255, 0.5)",
    "rgba(127, 96, 0, 0.5)",
    "rgba(255, 140, 184, 0.5)",
    "rgba(79, 90, 117, 0.5)"
  ];

  var data = [];

  for (var i = 0; i < xData.length; i++) {
    var result = {
      type: "box",
      y: yData[i],
      name: xData[i],
      fillcolor: "cls",
      marker: {
        size: 2
      },
      line: {
        width: 1
      }
    };
    data.push(result);
  }

  layout = {
    title: "Number of Bedrooms",
    yaxis: {
      range: [0, 800],
      title: "price"
    },

    margin: {
      l: 50,
      r: 30,
      b: 30,
      t: 80
    },
    paper_bgcolor: "rgb(243, 243, 243)",
    plot_bgcolor: "rgb(243, 243, 243)",
    showlegend: false
  };
  Plotly.newPlot("bedroomCorr", data, layout);
}

function plotPriceBathroomsCorrelation(data) {
  var xData = [1, 2, 3, 4, 5, 6];

  var yData = [
    data.filter(t => t.bathrooms == 1).map(t => t.price),
    data.filter(t => t.bathrooms == 2).map(t => t.price),
    data.filter(t => t.bathrooms == 3).map(t => t.price),
    data.filter(t => t.bathrooms == 4).map(t => t.price),
    data.filter(t => t.bathrooms == 5).map(t => t.price),
    data.filter(t => t.bathrooms == 6).map(t => t.price)
  ];
  var colors = [
    "rgba(93, 164, 214, 0.5)",
    "rgba(255, 144, 14, 0.5)",
    "rgba(44, 160, 101, 0.5)",
    "rgba(255, 65, 54, 0.5)",
    "rgba(207, 114, 255, 0.5)",
    "rgba(127, 96, 0, 0.5)",
    "rgba(255, 140, 184, 0.5)",
    "rgba(79, 90, 117, 0.5)"
  ];

  var data = [];

  for (var i = 0; i < xData.length; i++) {
    var result = {
      type: "box",
      y: yData[i],
      name: xData[i],
      fillcolor: "cls",
      marker: {
        size: 2
      },
      line: {
        width: 1
      }
    };
    data.push(result);
  }

  layout = {
    title: "Number of Bathrooms",
    yaxis: {
      range: [0, 800],
      title: "price"
    },

    margin: {
      l: 50,
      r: 30,
      b: 30,
      t: 80
    },
    paper_bgcolor: "rgb(243, 243, 243)",
    plot_bgcolor: "rgb(243, 243, 243)",
    showlegend: false
  };
  Plotly.newPlot("bathCorr", data, layout);
}

function plotRatioCorrelation(data) {
  var yData = []
  var xData = []
  for (var i = 75; i < 101; ++i) {
    xData.push(i)
    yData.push(data.filter(t => t.review_scores_rating == i).map(t => t.renting_ratio))
  }

  var data = [];

  for (var i = 0; i < xData.length; i++) {
    var result = {
      type: "box",
      y: yData[i],
      name: xData[i],
      fillcolor: "cls",
      marker: {
        size: 2
      },
      line: {
        width: 1
      }
    };
    data.push(result);
  }
  console.log(data)
  layout = {
    title: "Review Score",
    yaxis: {
      range: [0, 1],
      title: "ratio"
    },

    margin: {
      l: 50,
      r: 30,
      b: 30,
      t: 80
    },
    paper_bgcolor: "rgb(243, 243, 243)",
    plot_bgcolor: "rgb(243, 243, 243)",
    showlegend: false
  };
  Plotly.newPlot("ratio", data, layout);
}

function displayRoomTypes(dta) {
  new Chart(document.getElementById("bar-chart-horizontal"), {
    type: "horizontalBar",
    data: {
      labels: ["Entire Home/Apt", "Private Room", "Shared Room"],
      datasets: [
        {
          backgroundColor: ["#0A0", "#AA0", "#A00"],
          data: [
            dta.filter(d => d.room_type === 'Entire').length,
            dta.filter(d => d.room_type === 'Room').length,
            dta.filter(d => d.room_type === 'Shared').length
          ]
        }
      ]
    },
    options: {
      legend: {display: false},
      title: {
        display: true,
        text: "Room type on a 1000 rooms sample"
      }
    }
  });
}

const average = arr => arr.reduce( ( p, c ) => p + c, 0 ) / arr.length;

function displayRoomAvailability(dta) {
  mean = average(dta.map(d => d.renting_ratio))
  new Chart(document.getElementById("doughnut-chart"), {
    type: "doughnut",
    data: {
      labels: ["Available", "Booked"],
      datasets: [
        {
          backgroundColor: ["#0A0", "#A00"],
          data: [
            ((1 - mean) * 100).toFixed(2),
            (mean * 100).toFixed(2)
          ]
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: "Availability"
      }
    }
  });
}

function displayHostsRooms(dta) {
  new Chart(document.getElementById("bar-chart"), {
    type: "bar",
    data: {
      labels: ["1", "2", "3", "4", "5"],
      datasets: [
        {
          backgroundColor: [
            "#3e95cd",
            "#8e5ea2",
            "#3cba9f",
            "#e8c3b9",
            "#c45850"
          ],
          data: [
            dta.filter(d => d.host_total_listings_count == 1).length,
            dta.filter(d => d.host_total_listings_count == 2).length,
            dta.filter(d => d.host_total_listings_count == 3).length,
            dta.filter(d => d.host_total_listings_count == 4).length,
            dta.filter(d => d.host_total_listings_count == 5).length
          ]
        }
      ]
    },
    options: {
      legend: {display: false},
      title: {
        display: true,
        text: "Number of listings per host on a 1000 rooms sample"
      }
    }
  });
}

function setInnerHtml(fields) {
  document.getElementById("price_night").innerHTML =
    "The average price per night is " + average(fields.map(f => f.price)).toFixed(2);
  document.getElementById("review_avg").innerHTML =
    "The mean review score is "+ average(fields.map(f => f.review_scores_rating)).toFixed(2);
  document.getElementById("income").innerHTML =
    "The estimated income over a year for a property is " + average(fields.map(f => f.price * f.renting_ratio * 365)).toFixed(2);
}

(function() {
  const city = getUrlParameter("city");
  if (!city) return fail();
  const url =
    "https://api.thomas-lemoullec.com/airbnb-advisor/dashboard/" +
    (city === "hong-kong" ? "hk" : city.substring(0, 2)) +
    "?fields=id,beds,price,bedrooms,bathrooms,renting_ratio,review_scores_rating,room_type,host_total_listings_count";
  axios
    .get(url)
    .then(function(response) {
      console.log(response);
      if (!response || !response.data) return fail();
      document.getElementById("bg").src = "./images/" + city + ".jpg";
      plotPriceBedCorrelation(response.data);
      plotPriceBedroomsCorrelation(response.data)
      plotPriceBathroomsCorrelation(response.data)
      plotRatioCorrelation(response.data)
      displayRoomTypes(response.data);
      displayRoomAvailability(response.data);
      displayHostsRooms(response.data);
      setInnerHtml(response.data);
      document.getElementById("city").innerHTML =
        city === "hong-kong" ? "hong kong" : city;
      const fields = response.data[0];
    })
    .catch(function(error) {
      console.log(error);
      fail();
    });
})();

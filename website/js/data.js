function getUrlParameter(name) {
  name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
  var regex = new RegExp("[\\?&]" + name + "=([^&#]*)");
  var results = regex.exec(location.search);
  return results === null
    ? ""
    : decodeURIComponent(results[1].replace(/\+/g, " "));
}

function displayRoomTypes(fields) {
  new Chart(document.getElementById("bar-chart-horizontal"), {
    type: "horizontalBar",
    data: {
      labels: ["Entire Home/Apt", "Private Room", "Shared Room"],
      datasets: [
        {
          backgroundColor: ["#0A0", "#AA0", "#A00"],
          data: [
            fields.entire_home_number,
            fields.private_room_number,
            fields.shared_room_number
          ]
        }
      ]
    },
    options: {
      legend: {display: false},
      title: {
        display: true,
        text: "Room type"
      }
    }
  });
}

function displayRoomAvailability(fields) {
  new Chart(document.getElementById("doughnut-chart"), {
    type: "doughnut",
    data: {
      labels: ["Available", "Booked"],
      datasets: [
        {
          backgroundColor: ["#0A0", "#A00"],
          data: [
            fields.available_listing_average,
            100 - fields.available_listing_average
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

function displayHostsRooms(fields) {
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
            fields.host_with_one_listing_number,
            fields.host_with_two_listing_number,
            fields.host_with_three_listing_number,
            fields.host_with_four_listing_number,
            fields.host_with_five_listing_number
          ]
        }
      ]
    },
    options: {
      legend: {display: false},
      title: {
        display: true,
        text: "Listings per Host"
      }
    }
  });
}

function setInnerHtml(fields) {
  document.getElementById("listings").innerHTML =
    fields.listing_number + " listings";
  document.getElementById("host_nbr").innerHTML = fields.host_number + " hosts";
  document.getElementById("price_night").innerHTML =
    fields.average_price.toFixed(2) + "$ by night (average)";
  document.getElementById("review_avg").innerHTML =
    fields.review_per_month_average.toFixed(2) + " reviews per month";
  document.getElementById("income").innerHTML =
    fields.estimated_income.toFixed(2) + "$ of estimated monthly income";
  const total = (fields.single_listing_number / fields.listing_number) * 100;
  document.getElementById("percent").innerHTML =
    total.toFixed(2) + "% of single listings";
}

function fail() {
  document.getElementById("ct").innerHTML = "No Data to Display";
}

(function() {
  const city = getUrlParameter("city");
  if (!city)
    return fail()
  const url = "https://api.thomas-lemoullec.com/airbnb-advisor/dashboard/" + (city === "hong-kong" ? "hk" : city.substring(0, 2))
  axios
    .get(url)
    .then(function(response) {
      if (!response || !response.data)
        return fail()
      document.getElementById("bg").src = "./images/" + city + ".jpg";
      document.getElementById("city").innerHTML =
          city === "hong-kong" ? "hong kong" : city;
      const fields = response.data[0];
      displayRoomTypes(fields);
      displayRoomAvailability(fields);
      displayHostsRooms(fields);
      setInnerHtml(fields);

    })
    .catch(function(error) {
      fail()
    });
})();

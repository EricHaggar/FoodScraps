var markers = [];

function initMap() {

  var db = firebase.database();
  var companies = [];
  var iconURL;
  var overallScores = [];
  var scoresMedian = 0;

  var centerMap = {
    lat: 40,
    lng: -97.307654
  };

  var map = new google.maps.Map(
    document.getElementById('map'), {
      zoom: 3.7,
      center: centerMap
    });

  db.ref("companies").on('value', function (snap) {
    snap.forEach(function (childNodes) {

      //marker loop iterates over all companies in the database
      company = {};
      company['name'] = childNodes.key;
      company['lat'] = childNodes.val().latitude;
      company['lng'] = childNodes.val().longitude;
      company['sizeScore'] = childNodes.val().sizeScore;
      company['reviewScore'] = childNodes.val().reviewScore;
      company['revenueScore'] = childNodes.val().revenueScore;
      company['recallScore'] = childNodes.val().recallScore;
      company['overallScore'] = childNodes.val().overallScore;
      companies.push(company);
    });

    

    // Populate an array of overallScores
    for (var i = 0; i < companies.length; i++) {
      overallScores.push(companies[i].overallScore);
    }

    scoresMedian = calculateMedian(overallScores);

    for (var i = 0; i < companies.length; i++) {

      var latLng = {
        lat: companies[i].lat,
        lng: companies[i].lng
      };

      if (companies[i].overallScore < scoresMedian) {

        iconURL = "http://maps.google.com/mapfiles/ms/icons/red-dot.png";

      } else {
        
        iconURL = "http://maps.google.com/mapfiles/ms/icons/blue-dot.png";

      }


      var marker = new google.maps.Marker({
        position: latLng,
        map: map,
        icon: iconURL,
        title: companies[i].name,
        sizeScore: companies[i].sizeScore,
        reviewScore: companies[i].reviewScore,
        revenueScore: companies[i].revenueScore,
        recallScore: companies[i].recallScore,
        overallScore: companies[i].overallScore

      });

      markers.push(marker);
    }

    for (var i = 0; i < markers.length; i++) {

      var addListener = function (i) {

        google.maps.event.addListener(markers[i], 'click', function () {

          activeMarker = markers[i];
          clearAnimation(activeMarker);
          markers[i].setAnimation(google.maps.Animation.BOUNCE);

          var main = document.getElementById("marker");
          var name = document.getElementById("name");

          main.style.visibility = "visible";
          name.innerHTML = markers[i].title;
          map.setCenter(markers[i].position);
          map.setZoom(8);

          var progress = document.getElementById("reviewScore");

          if (markers[i].reviewScore == 0) {
            reviewScorePercentage = 5;
          } else {
            reviewScorePercentage = markers[i].reviewScore * 10;
          }
          progress.style.width = reviewScorePercentage + "%";
          progress.style.backgroundColor = "hsl(" + reviewScorePercentage + ", 100%, 42%)";

          var progress = document.getElementById("sizeScore");

          if (markers[i].sizeScore == 0) {
            sizeScorePercentage = 5;
          } else {
            sizeScorePercentage = markers[i].sizeScore * 10;
          }
          progress.style.width = sizeScorePercentage + "%";
          progress.style.backgroundColor = "hsl(" + sizeScorePercentage + ", 100%, 42%)";

          var progress = document.getElementById("revenueScore");

          if (markers[i].revenueScore == 0) {
            revenueScorePercentage = 5;
          } else {
            revenueScorePercentage = markers[i].revenueScore * 10;
          }
          progress.style.width = revenueScorePercentage + "%";
          progress.style.backgroundColor = "hsl(" + revenueScorePercentage + ", 100%, 42%)";

          var progress = document.getElementById("recallScore");

          if (markers[i].recallScore == 0) {
            recallScorePercentage = 5;
          } else {
            recallScorePercentage = markers[i].recallScore * 10;
          }
          progress.style.width = recallScorePercentage + "%";
          progress.style.backgroundColor = "hsl(" + recallScorePercentage + ", 100%, 42%)";

          var progress = document.getElementById("overallScore");

          if (markers[i].overallScore == 0) {
            markers[i].overallScore = 5;
          }
          progress.style.width = markers[i].overallScore + "%";
          progress.style.backgroundColor = "hsl(" + markers[i].overallScore + ", 100%, 42%)";

        });

      }

      addListener(i);

    }

  });
}


function calculateMedian(overallScores) {

  var numOfCompanies = overallScores.length;
  var median = 0;

  // Sort the array of overallScores
  overallScores = overallScores.sort(function (a, b) { return a - b; });

  if (numOfCompanies % 2 === 0) { // Even number

    // Middle numbers average
    median = (overallScores[numOfCompanies / 2 - 1] + overallScores[numOfCompanies/2])/2;

  } else { // Odd number 

    // Middle number
    median = overallScores[(numOfCompanies-1)/2];
  }

  return median;

}

// Clears animation of the all markers except the activeMarker
function clearAnimation(activeMarker) {

  for (var i = 0; i < markers.length; i++) {
    if (markers[i].title != activeMarker.title) {
      markers[i].setAnimation(null);
    }
  }
}







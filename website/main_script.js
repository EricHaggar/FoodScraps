function initMap() {

  var db = firebase.database();
  var companies = [];
  var markers = [];

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

      //This loop iterates over all companies in the database
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


    for (var i = 0; i < companies.length; i++) {

      var latLng = {
        lat: companies[i].lat,
        lng: companies[i].lng
      };

      var marker = new google.maps.Marker({
        position: latLng,
        map: map,
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
          clearAnimation();
          var main = document.getElementById("marker");
          var name = document.getElementById("name");
     
          main.style.visibility = "visible";
          name.innerHTML = markers[i].getTitle();
          map.setCenter(markers[i].getPosition());
          map.setZoom(8);

          var progress = document.getElementById("reviewScore");
          reviewScorePercentage = markers[i].reviewScore * 10;
          progress.style.width = reviewScorePercentage + "%";
          progress.style.backgroundColor = "hsl(" + reviewScorePercentage + ", 100%, 42%)";

          var progress = document.getElementById("sizeScore");
          sizeScorePercentage = markers[i].sizeScore * 10;
          progress.style.width = sizeScorePercentage + "%";
          progress.style.backgroundColor = "hsl(" + sizeScorePercentage + ", 100%, 42%)";

          var progress = document.getElementById("revenueScore");
          revenueScorePercentage = markers[i].revenueScore * 10;
          progress.style.width = revenueScorePercentage + "%";
          progress.style.backgroundColor = "hsl(" + revenueScorePercentage + ", 100%, 42%)";

          var progress = document.getElementById("recallScore");
          recallScorePercentage = markers[i].recallScore * 10;
          progress.style.width = recallScorePercentage + "%";
          progress.style.backgroundColor = "hsl(" + recallScorePercentage + ", 100%, 42%)";

          var progress = document.getElementById("overallScore");
          progress.style.width = markers[i].overallScore + "%";
          progress.style.backgroundColor = "hsl(" + overallScore + ", 100%, 42%)";

          markers[i].setAnimation(google.maps.Animation.BOUNCE);

        });
      }

      addListener(i);
    }

  });

  function clearAnimation() {
    //TO BE COMPLETED
  }
}

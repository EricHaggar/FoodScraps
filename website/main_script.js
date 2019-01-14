function initMap() {

  var db = firebase.database();

  var arr = [];
  var markers = [];

  var centerMap = {
    lat: 40,
    lng: -97.307654
  };

  // The map, centered at Uluru
  var map = new google.maps.Map(
    document.getElementById('map'), {
      zoom: 3.7,
      center: centerMap
    });

  firebase.database().ref("companies").on('value', function(snap) {
    snap.forEach(function(childNodes) {

      //This loop iterates over children of user_id

      var obj = {};
      obj['name'] = childNodes.key;
      obj['coordinatex'] = childNodes.val().latitude;
      obj['coordinatey'] = childNodes.val().longitude;
      obj['sizeScore'] = childNodes.val().sizeScore;
      obj['reviewScore'] = childNodes.val().reviewScore;
      obj['revenueScore'] = childNodes.val().revenueScore;
      obj['recallScore'] = childNodes.val().recallScore;
      obj['overallScore'] = childNodes.val().overallScore;
      arr.push(obj);
    });

    for (var i = 0; i < arr.length; i++) {

      var latx = arr[i].coordinatex;
      var longy = arr[i].coordinatey;

      pos = {
        lat: latx,
        lng: longy
      };

      var marker = new google.maps.Marker({
        position: pos,
        map: map,
        title: arr[i].name,
        size: arr[i].sizeScore,
        review: arr[i].review,
        revenue: arr[i].revenue,
        recall: arr[i].recall,
        overall: arr[i].overall
      });

      markers.push(marker);
    }



    for (var i = 0; i < markers.length; i++) {

      console.log(markers[i].getPosition().toString());
      console.log(markers[i].getTitle());
      var title = markers[i].getTitle().toString();

      var addListener = function(i) {

        let sizeNum = arr[i].sizeScore;

        google.maps.event.addListener(markers[i], 'click', function() {
          clearAnimation();
          var main = document.getElementById("marker");
          var name = document.getElementById("name");
          var desc = document.getElementById("desc");
          var severity = document.getElementById("severity");
          var reasons = document.getElementById("reasons");

          main.style.visibility = "visible";
          name.innerHTML = markers[i].getTitle();
          //map.setCenter(markers[i].getPosition());
          map.setCenter(markers[i].getPosition());
          map.setZoom(8);

          var progress = document.getElementById("reviewScore");
          console.log(markers[i].size*10+"%");
          progress.style.width = ((markers[i].size * 10)+"%");
          progress.style.backgroundColor = "hsl("+markers[i].size*10+", 81%, 40%)";


          var progress = document.getElementById("progressBar2");
          progress.style.width = "40%";
          progress.style.backgroundColor = "#ffce52";

          ;

          var progress = document.getElementById("progressBar3");
          progress.style.width = "20%";
          progress.style.backgroundColor = "#8fde51";

          ;

          var progress = document.getElementById("progressBar4");
          progress.style.width = "90%";
          progress.style.backgroundColor = "#ff3f1e";

          ;

          var progress = document.getElementById("progressBar5");
          progress.style.width = "64%";
          progress.style.backgroundColor = "#ff9d40";

          markers[i].setAnimation(google.maps.Animation.BOUNCE);



        });
      }

      addListener(i);
    }


  });

  function clearAnimation() {
    //mcCain.setAnimation(null);
  }
}

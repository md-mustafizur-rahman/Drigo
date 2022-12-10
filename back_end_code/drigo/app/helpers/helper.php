<?php
function getDistance($userLatitude,  $userLongitude, $productLatitude,  $productLongitude)
{
    $userFinalLatitude = number_format((float)$userLatitude, 15);
    $userFinalLongitude = number_format((float)$userLongitude, 15);
    $productFinalLatitude = number_format((float)$productLatitude, 15);
    $productFinalLongitude = number_format((float)$productLongitude, 15);



    // echo "userLatitude " .  $userFinalLatitude;
    // echo "<br>";
    // echo "userLongitude " .  $userFinalLongitude;
    // echo "<br>";
    // echo "productLongitude " .   $productFinalLatitude;
    // echo "<br>";
    // echo "productLongitude " .  $productFinalLongitude;



    //distanitation latitude longittude
    //23.808314291592204, 90.37023242945203
    //23.824957365782822, 90.34835823188375
    //23.724340855774862, 90.38742162066357

    // Calculation
    // var lat1 = position.coords.latitude.toFixed(15);
    // var lat2 = 23.724340855774862;
    // var lon1 = position.coords.longitude.toFixed(15);
    // var lon2 = 90.38742162066357;

    $R = 6371;
    // Radius of the earth in km
    $dLat = deg2rad($productFinalLatitude - $userFinalLatitude); // deg2rad below
    $dLon = deg2rad($productFinalLongitude - $userFinalLongitude);
    // Haversine Formula
    $a =
        sin($dLat / 2) * sin($dLat / 2) +
        cos(deg2rad($userFinalLatitude)) * cos(deg2rad($userFinalLongitude)) *
        sin($dLon / 2) * sin($dLon / 2);

    $c = 2 * atan2(sqrt($a), sqrt(1 - $a));
    $d = $R * $c; // Distance in km
    // x.innerHTML += "<br />";
    echo  number_format($d, 3) . " km";
}

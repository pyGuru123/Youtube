function logEndpoints() {
  Logger.log(sendMsgEndpoint);
  Logger.log(updatesEndpoint);
}

function getCryptoPrice(coin) {
  const url = "https://api.coincap.io/v2/assets";
  var response = JSON.parse(UrlFetchApp.fetch(url));
  var coins = response["data"]
  for (var i=0; i<coins.length; i++) {
    if (coins[i]["id"] == coin) {
      var info = `${coins[i]["name"]} - ${coins[i]["symbol"]} - ${coins[i]["priceUsd"]}`;
      return info;
    }
  }
}

function getDogPic() {
  const url = "https://dog.ceo/api/breeds/image/random";
  var response = JSON.parse(UrlFetchApp.fetch(url));
  return response["message"];
}

function test() {
  getDogPic()
}
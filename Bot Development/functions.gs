function get_shiva_images() {
  var url1 = "https://tg-api-pyguru123.vercel.app/api/v1/sanatan/today";
  var url2 = "https://tg-api-pyguru123.vercel.app/api/v1/sanatan/mahadev";

  var response = JSON.parse(UrlFetchApp.fetch(url1));
  date = response.date;
  sunrise = response.sunrise;
  sunset = response.sunset;
  importance = response.importance;

  var string = `
  ${date}

  ${sunrise}
  ${sunset}
  ${importance}
  `
  if (string) {
    var response2 = JSON.parse(UrlFetchApp.fetch(url2));
    var url = response2.url;
    if (url) {
      return [string, url];
    }
  }
}

function test() {
  Logger.log(get_shiva_images())
}

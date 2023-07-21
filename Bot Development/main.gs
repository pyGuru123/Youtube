function sendShivaPhoto() {
    var [caption, url] = get_shiva_images();

    var payload = {
      "chat_id": chat_id,
      "photo": url,
      "caption": caption
    };

    var options = {
      "method": "post",
      "payload": payload
    }

    var response = UrlFetchApp.fetch(sendPhotoEndpoint, options=options)
    Logger.log(response);
}
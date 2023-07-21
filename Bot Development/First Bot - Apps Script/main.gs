const webhook = "https://script.google.com/macros/s/AKfycbya1Rp-6cZ52iDYW13cEr03LKKZ1JcnCTiyxxyIq0eaa_FSFKy_rgbuORoPn39oeZfj/exec";

function setTelegramWebhook() {
   var url = setWebhookEndpoint + webhook;
   var response = UrlFetchApp.fetch(url);
   Logger.log(response);
}

function deleteTelegramWebhook(webhook) {
   var response = UrlFetchApp.fetch(delWebhookEndpoint);
   Logger.log(response);
}

function sendMsg(chat_id, text) {
  var payload = {
    "chat_id": chat_id,
    "text": text
  }

  var options = {
    "method": "post",
    "contentType": "application/json",
    "payload": JSON.stringify(payload)
  }

  var response = JSON.parse(UrlFetchApp.fetch(sendMsgEndpoint, options=options));
  Logger.log(response);
}

function sendPic(chat_id, url) {
  var payload = {
    "chat_id": chat_id,
    "photo": url
  }

  var options = {
    "method": "post",
    "contentType": "application/json",
    "payload": JSON.stringify(payload)
  }

  Logger.log(options);

  var response = JSON.parse(UrlFetchApp.fetch(sendPhotoEndpoint, options=options));
  Logger.log(response);
}

function reply(content) {
  var chat_id = content.message.chat.id;
  var text = content.message.text;

  if (text.startsWith("/dog")) {
    var url = getDogPic();
    sendPic(chat_id, url);
  }
  else {
    result = getCryptoPrice(text);
    sendMsg(chat_id, result);
  }
}


function doPost(e) {
  var content = JSON.parse(e.postData.contents);
  reply(content);
}

function test2() {
  var content = {"update_id":522188852,
"message":{"message_id":14,"from":{"id":704647574,"is_bot":false,"first_name":"Satoru","last_name":"Gojou","username":"itspyguru","language_code":"en"},"chat":{"id":704647574,"first_name":"Satoru","last_name":"Gojou","username":"itspyguru","type":"private"},"date":1689877531,"text":"/dog","entities":[{"offset":0,"length":4,"type":"bot_command"}]}};

  reply(content);
}
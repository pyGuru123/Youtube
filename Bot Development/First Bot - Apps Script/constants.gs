const token = "5648863748:AAEt95hen-MYVxxxxxxxxxxxxxxxxxxxxxxxxxxxx";

const sendMsgEndpoint = "https://api.telegram.org/bot" + token + "/sendMessage";
const sendPhotoEndpoint = 'https://api.telegram.org/bot' + token + '/sendPhoto';
const updatesEndpoint = "https://api.telegram.org/bot" + token + "/getUpdates";
const setWebhookEndpoint = "https://api.telegram.org/bot" + token + "/setWebhook?url=";
const delWebhookEndpoint = "https://api.telegram.org/bot" + token + "/deleteWebhook";
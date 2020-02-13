TOKEN = '829018748:AAHnZnTx9gHDKaVn7d30nZ0vso5Wpnx8ESI'
NGROK_URL = 'https://7a1e29dd.ngrok.io'
BASE_TELEGRAM_URL = 'https://api.telegram.org/bot{}'.format(TOKEN)
LOCAL_WEBHOOK_ENDPOINT = '{}/webhook'.format(NGROK_URL)
TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_URL, LOCAL_WEBHOOK_ENDPOINT)
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_URL + '/sendMessage?chat_id={}&text={}'


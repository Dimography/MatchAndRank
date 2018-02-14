const VK = require('vksdk');
const vk = new VK({
    'appId': 6251781,
    'appSecret': 'w277T55opWMUdaVDjfSB',
    'language': 'ru'
});

vk.on('serverTokenReady', function (_o) {
    // Here will be server access token 
    console.log('serverTokenReady');
    vk.setToken(_o.access_token);
});

vk.setSecureRequests(true);

// Request server API method 
vk.request('secure.getSMSHistory', {}, function (_dd) {
    console.log(_dd);
});

// Request 'users.get' method 
vk.request('users.get', { 'user_id': 1 }, function (_o) {
    console.log(_o);
});

module.exports = vk;
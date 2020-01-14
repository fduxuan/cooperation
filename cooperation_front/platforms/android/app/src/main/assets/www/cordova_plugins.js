cordova.define('cordova/plugin_list', function(require, exports, module) {
  module.exports = [
    {
      "id": "cordova-plugin-qqsdk.QQSDK",
      "file": "plugins/cordova-plugin-qqsdk/www/qq.js",
      "pluginId": "cordova-plugin-qqsdk",
      "clobbers": [
        "QQSDK"
      ]
    }
  ];
  module.exports.metadata = {
    "cordova-plugin-whitelist": "1.3.4",
    "cordova-plugin-qqsdk": "0.9.7"
  };
});
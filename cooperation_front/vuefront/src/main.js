// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'
import "./assets/icons/iconfont.css"
import VueCordova from 'vue-cordova'


Vue.use(VueCordova)
//Vue.use(THREE)
// add cordova.js only if serving the app through file://
if (window.location.protocol === 'file:' || window.location.port === '3000') {
  var cordovaScript = document.createElement('script')
  cordovaScript.setAttribute('type', 'text/javascript')
  cordovaScript.setAttribute('src', 'cordova.js')
  document.body.appendChild(cordovaScript)
}

Vue.prototype.$ajax = axios

Vue.use(ElementUI)


Vue.config.productionTip = false





/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
